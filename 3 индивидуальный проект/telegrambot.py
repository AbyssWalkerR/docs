from os import error
import time
from telegram import forcereply, message, messageid, replymarkup
from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler, Filters,InlineQueryHandler
import telegram
from telegram.parsemode import ParseMode
import yaml
import traceback
import threading
import re

from servstart import ServStart 
import daw as WQ





class TelBot(ServStart):
    def __init__(self):
        super().__init__()
        try:
            self.t.is_alive()
            pass
        except:
            self.t = threading.Thread(target=self.async_work)
            self.t.start()
        self.d=[]
        self.__conf = yaml.load(open('pass.yml'),Loader=yaml.FullLoader)
        self.__bot_token=self.__conf['bot']['api']
        self._updater = Updater(token=self.__bot_token, use_context=True)
        self.__dispatcher=self._updater.dispatcher
        self.__cur = self.con.cursor()
        self.mn()
        print("Старт бота")

    
    def async_work(self):
        self.t = threading.currentThread()
        while getattr(self.t, "do_run", True):
            for ke in WQ.miltiplefunc:
                try:
                    getattr(WQ.Agreg,WQ.miltiplefunc.get(ke, 'waw'))()
                except Exception as e:
                    traceback.print_exc()
                    print(ke)
            print ("current time %s" % time.asctime())
            time.sleep(180)
        print("Остановка потока.")


    def start(self,update: telegram.Update, context: CallbackContext):
        
        try:
            news=[]
            w=context.args[0]
            if(re.match(r'[0-9]+', w)):
                self.w=int(w)
                print(self.d)
                print(self.w)
                if(self.w>0 and self.w<21):
                    print('www')
                    if(not self.d):
                        self.__cur.execute("""select title, link, image, description,
                         date,id from general order by date desc limit %s""",(self.w,))
                        news = self.__cur.fetchall()
                    else:
                        format_strings = ','.join(['%s'] * len(self.d))
                        q=("""select title, link, image, description,
                         date,id from general where id not in (%s) order by date desc limit %%s"""% format_strings)
                        self.__cur.execute(q,tuple(self.d)+(self.w,))
                        news=self.__cur.fetchall()
                    
                    try:
                        for k in news:
                            self.d.append(k[5])
                            if(not k[2]):
                                ph="https://tl.rulate.ru/i/book/19/10/18925.jpg"
                            else:
                                ph=k[2]
                            te=("<b>{text}</b>\n"
                                "<i>{desc}</i>\n"
                                "<i>Дата публикации: {date}</i>\n"
                                "<a href='{link}'>Ссылка на оригинал статьи</a>").format(
                                                text=k[0],link=k[1],desc=k[3],date=k[4])
                            context.bot.send_photo(chat_id=update.effective_chat.id, photo=ph,caption=te,parse_mode=ParseMode.HTML)
                    except Exception as e:
                        traceback.print_exc()
                else:
                    teqq="Введите число новостей от 1 до 20"
                    context.bot.send_message(chat_id=update.effective_chat.id,text=teqq)
                    return
            else:
                teqq="Введите число новостей от 1 до 20"
                context.bot.send_message(chat_id=update.effective_chat.id,text=teqq)
                return
            return
        except:
            teqq="Введите число новостей от 1 до 20"
            context.bot.send_message(chat_id=update.effective_chat.id,text=teqq)
            return
         
    
    def inline(self,update: telegram.Update, context: CallbackContext):
        query = update.inline_query.query
        if not query:
            return
        results = []
        
        self.__cur = self.con.cursor()
        self.__cur.execute("""select id,title, link, image, description,
        DATE_FORMAT(date, '%Y-%m-%d %T') as date from general order by date desc limit 5""")
        news = self.__cur.fetchall()   
        for k in news:
            results.append(
                telegram.InlineQueryResultArticle(
                    id=k[0],
                    thumb_url=k[3],
                    title=k[1],
                    description=k[4],
                    input_message_content=telegram.InputTextMessageContent(
                        message_text=k[2]
                    )
                )
            )
        context.bot.answer_inline_query(update.inline_query.id, results)

    
    def unknown(self,update: telegram.Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Такой команды нет, напишите / для просмотра команд")

    def mn(self):
        self.__start_handler = CommandHandler('start', self.start)
        self.__dispatcher.add_handler(self.__start_handler)
        self.__inline_handler = InlineQueryHandler(self.inline)
        self.__dispatcher.add_handler(self.__inline_handler)
        self__unknown_handler = MessageHandler(Filters.command, self.unknown)
        self.__dispatcher.add_handler(self__unknown_handler)
        try:
            self._updater.start_polling()
        except Exception as e:
            traceback.print_exc()
            print('Попробовать снова через 15 сек')
            time.sleep(15)
