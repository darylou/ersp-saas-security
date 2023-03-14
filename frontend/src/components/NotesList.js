import { useEffect, useState } from 'react'
import uniqid from 'uniqid'
import Note from './Note.js'
import axios from 'axios'

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

export default function NotesList() {

    const[list, setList] = useState([])

    useEffect(() => {
        updateList()
        },[]);

    function updateList() {
        var json, size;
        axios.get("http://msa.seclab.cs.ucsb.edu/api/paste").then((res) => {
            json = JSON.parse(JSON.stringify(res.data))
            size = Object.keys(res.data).length

            var newList = [];

            for (var i = 0; i < size / 3; i++) {
                const newNote = {
                    id:json[`post_id_${i}`], 
                    title:json[`post_title_${i}`],
                    content:json[`post_body_${i}`],
                    isEditing: false,
                    color:getRandomColor()
                }
                newList = [...newList, newNote]
            }
            console.log(newList)
            setList(newList)
            return newList
        }).catch((err) => {
            console.log("what")
        })
        return []
    }

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
        console.log(id)
        const t = newTitle
        const c = newContent

        const newList = list.map((item) => {
            if(item.id !== id) return item
            return {...item, title:t, content:c, isEditing:false}
        })
        
        axios.post(`http://msa.seclab.cs.ucsb.edu/api/paste/${id}/${t}/${c}`, {
            'id': id,
            'title': t,
            'body': c
        }).then(res => {
            console.log(res.data)
            window.location.reload(false);
        }).catch(err => {

        })

        // Don't need to update here, use the get request instead
        // updateList(newList) 
    }

    function deleteNote(id) {
        axios.delete(`http://msa.seclab.cs.ucsb.edu/api/paste/${id}`).catch((err) => {
            console.log(err)
        }).finally(
            updateList()
            
        )
        window.location.reload(false);
    }

    return (
        <div className='page_body'>
            <button id='addNote' className='btn' onClick={addNote}>Add Note</button>
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