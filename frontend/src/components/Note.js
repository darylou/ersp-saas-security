import React, { useState } from 'react'
import EditNote from './EditNote'
import '../App.css'


export default function Note({ note, onEdit, onSave, onDelete }) {

    return (
        <>
        {note.isEditing && <EditNote note={note} id={note.id} saveNote={onSave} />}
        <div className='note'>
            <div className='note_content'>
                <h1 className='h1_underline' style={{ textDecorationColor : note.color }}>
                    {note.title ? note.title : "Untitled"}
                </h1>
                {/* {!state && <img src={plus_img} alt='+' onClick={handleOnToggle}></img>}
                {state && <img src={minus_img} alt='-' onClick={handleOnToggle}></img>} */}
                {note.content ? <p>{note.content}</p> : <p className='p_italic'>Note is empty.</p>}
                <div className='btn_modify_container'>
                    <p className='btn_modify' onClick={() => onEdit(note.id)}>Edit</p>
                    <p className='btn_modify' onClick={() => onDelete(note.id)}>Delete</p>
                </div>
            </div>
        </div>
        </>
    )
    
}
