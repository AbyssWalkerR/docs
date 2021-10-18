import React, {useState} from 'react'
import AddTask from '../TaskAdd/AddTask'
import './task.css'
import {AiFillDelete} from 'react-icons/ai'
import {AiFillEdit} from 'react-icons/ai'

function Task({tasks,completeTask,removeTask, updateTask}) {
    const [edit,setEdit] = useState({
        id: null,
        value:'',
        value2:''
    });

    const submitUpdate = a => {
        updateTask(edit.id,a);
        setEdit({
            id: null,
            value:'',
            value2:''
        });
    } 

    if(edit.id) {
        return <AddTask edit={edit} onSubmit={submitUpdate} />;
    }

    return tasks.map((task, index) => (
        <div className={task.isComplete ? 'task complete' : 'task'} key={index}>
            <div key={task.id} onClick={() => completeTask(task.id)}>
            <div>Имя: {task.text}</div>
             {task.isComplete ? <div>Завершено</div> : <div>Нажать для завершения</div>}
             <div>Описание: {task.text2}</div>
            
            </div>
            <div className="icons">
                <AiFillDelete 
                onClick={() => removeTask(task.id)}
                className='delete-icon'
                />
                <AiFillEdit 
                onClick={() => setEdit({id: task.id, value: task.text, value2: task.text2})}
                className='edit-icon'
                />
                </div>   
        </div>
    ))
}

export default Task
