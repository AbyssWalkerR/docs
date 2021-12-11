from os import error
import yaml
import mysql.connector
import traceback

class ServStart():
    

    def __init__(self):
        self.conf = yaml.load(open('pass.yml'),Loader=yaml.FullLoader)
        self.dhost = self.conf['mysq']['user']
        self.dpwd = self.conf['mysq']['pass']
        self.datab = self.conf['mysq']['database']

        try: 
            self.con= mysql.connector.connect(host="localhost",
                    user=self.dhost,
                    passwd=self.dpwd,
                    database=self.datab)
            print("Подключено к БД")
        except Exception as e:
            traceback.print_exc()
            self.con.close()
            print("Неудачное соединение")



    def conclose(self):
        try:
            self.con.close()
            print("Соединение закрыто")
        except Exception as e:
            traceback.print_exc()
            print("Неудачное закрытие соединения")