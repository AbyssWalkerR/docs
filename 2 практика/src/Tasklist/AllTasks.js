import React, {useState} from 'react'
import { RiTaskLine } from 'react-icons/ri';
import Task from '../Task/Task';
import AddTask from '../TaskAdd/AddTask'

function AllTasks() {

    const [tasks, setTasks] = useState([]);
    

    

    const addTasks = task => {
        if(!task.text || /^\s*$/.test(task.text)) {
            return;
        }
        if(!task.text2 || /^\s*$/.test(task.text2)) {
            return;
        }

        const newTask = [task, ...tasks];
        setTasks(newTask);
    }; 
    

    const updateTask = (taskId, newValue) => {
        if((!newValue.text || /^\s*$/.test(newValue.text)) && (!newValue.text2 || /^\s*$/.test(newValue.text2))) {
            return;
        }

        
        setTasks(function (prev) {
                return prev.map(function (item) {
                        if(item.id === taskId){
                            if(!newValue.text) {
                                newValue.text=item.text;
                                
                            }
                            if(!newValue.text2) {
                                newValue.text2=item.text2;
                                
                            }
                            return (
                                newValue
                                
                            );
                        }
                        else { 
                            return (
                                item
                                
                            );
                        }
                    
                    
                    });
            });
    };


    const removeTask = id=> {
        const removeArr = [...tasks].filter(task => task.id !== id)

        setTasks(removeArr)
    };





    const completeTask = id => {
        let updatedTasks = tasks.map(task => {
            if(task.id === id) {
                task.isComplete = !task.isComplete;
            }
            return task;
        });
        setTasks(updatedTasks);
    }

    return (
        <div>
            <h1> Task App</h1>
            <AddTask  onSubmit={addTasks}/>
            <Task 
            tasks={tasks}
            completeTask={completeTask}
            removeTask={removeTask}
            updateTask={updateTask}
            />
        </div>
    );
}

export default AllTasks;
