import React, {useState} from 'react'
import './addtask.css'

function AddTask(props) {
  const [input,setInput] = useState(
    props.edit ? {
      nam: props.edit.value,
      desc: props.edit.value2
  } : {
    nam: '',
    desc:''
  }
  
  );
  
  const hChange = e => {
    setInput({
      ...input,
      [e.target.name]: e.target.value
    });
  }

  const handleSub = e => {
    e.preventDefault();

    props.onSubmit({
      id: Math.floor(Math.random()* 10000),
      text: input.nam,
      text2: input.desc
    });

    setInput({
      nam: '',
      desc: ''
    });
  };
  
    return (
        <form className='tasks-add' onSubmit={handleSub}> 
        {props.edit ? (
          <>
            <input type='text' placeholder='Update name' value={input.nam}
            name='nam'
            className='task-input_1 edit'
            onChange={hChange}
            /> 

            <input type='text' placeholder='Update description' value={input.desc}
            name='desc'
            className='task-input_2 edit'
            onChange={hChange}
            /> 
            <p></p>
            <button className='task-button edit'>Update task</button>
          </>
        ) : (
          <>
            <input type='text' placeholder='Add name' value={input.nam}
            name='nam'
            className='task-input_1'
            onChange={hChange}
            /> 

            <input type='text' placeholder='Add description' value={input.desc}
            name='desc'
            className='task-input_2'
            onChange={hChange}
            /> 
            <p></p>
            <button className='task-button'>Add task</button>
          </>

        )} 
        
        
        </form>
    );
}

export default AddTask;
