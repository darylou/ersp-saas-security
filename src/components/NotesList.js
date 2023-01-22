import { useState } from 'react'
import uniqid from 'uniqid'
import Note from './Note.js'

const initialList = [
    {
        id:uniqid('id-'),
        title:'Untitled',
        content:'Start your first note here. Don\'t have anything to write about? Here are some ideas: your iconic school chancellor, how you\'re feeling today, unsent confessions, or your favorite brand of pickles.',
        isEditing: false,
        color:getRandomColor()
    }
]

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

export default function NotesList() {

    const[list, setList] = useState(initialList)

    function addNote() {
        const newNote = {id:uniqid('id-'), title:'Untitled', content:'', isEditing:true, color:getRandomColor()}
        const newList = [...list, newNote]
        setList(newList)
    }

    function editNote(id) {
        const newList = list.map((item) => {
            if(item.id !== id) return item
            return {...item, isEditing:true}
        })
        setList(newList)
    }

    function saveNote(id, newTitle, newContent) {
        const t = newTitle
        const c = newContent

        const newList = list.map((item) => {
            if(item.id !== id) return item
            return {...item, title:t, content:c, isEditing:false}
        })
        
        setList(newList)        
    }

    function deleteNote(id) {
        const newList = list.filter((item) => item.id !== id)
        setList(newList)
    }

    return (
        <div className='page_body'>
            <button onClick={addNote}>Add Note</button>
            <div className='notes_list'>
                {list.map((note) => (
                    <Note 
                        note={note}
                        onEdit={editNote}
                        onSave={saveNote}
                        onDelete={deleteNote}
                    />
                ))}
            </div>
        </div>
    )
}