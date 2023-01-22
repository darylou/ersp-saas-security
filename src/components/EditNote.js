import { useState, useEffect } from 'react'
import '../App.css'

export default function EditNote({note, id, saveNote}) {

    // Set a slight delay in displaying the editor
    // const [isDisplayed, setIsDisplayed] = useState(false);

    // useEffect(() => {
    //   setInterval(() => {
    //     setIsDisplayed(true);
    //   }, 0);
    // }, []);

    const [title, setTitle] = useState(note.title)
    const [content, setContent] = useState(note.content)
    
    const handleTitleChange = (e) => {
        setTitle(e.target.value)
    }

    const handleContentChange = (e) => {
        setContent(e.target.value)
    }

    return (
        (<div className="edit_background">
        <div className='note_editor'>
            <div className='horizontally_centered'>
                <label for="title"><p className='note_editor_title_label'>Title</p></label>
                <div>
                    <input className='note_editor_title_editor' id='title' type='text' defaultValue={note.title} onChange={handleTitleChange} />
                </div>
                {/* <label for="content"><p className='note_editor_title_label'>Content</p></label> */}
                <div>
                    <textarea className='note_editor_content_editor' id='content' type='text' defaultValue={note.content} onChange={handleContentChange}/>
                </div>
                <button className="save_btn" onClick={() => saveNote(id, title, content)}>Save</button>
            </div>
        </div>
        </div>)
    )

}