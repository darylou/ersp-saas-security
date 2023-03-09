import React, {useState,useEffect} from 'react';
import {useNavigate,useLocation} from 'react-router-dom'
import Draggable from 'react-draggable'
import Sparkles from '../components/Sparkles.js'
import NotesList from '../components/NotesList.js'
import amongus from '../imgs/amongus.png'
import Arrow from '../imgs/drag_sticker_arrow.svg'

function Home() {
    const[prompt, setPrompt] = useState(true)
    const navigate = useNavigate();
    const location = useLocation();

    useEffect(() => {
        try {
            if (!location.state.authenticated) {
                navigate("/")
            }
        } catch (error) {
            navigate("/")
        }
    }, []);

    function removePrompt() {
        const newPrompt = false
        setPrompt(newPrompt)
    }

    function logout() {
        navigate("/",{state:{authenticated:false}})
    }

    return (
        <div className='home'>
            <Draggable>
                <img className='sticker amongus' src={amongus} alt='' draggable='false' onMouseDownCapture={removePrompt} />
            </Draggable>
            {prompt && 
                <>
                <span className='drag_prompt'>DRAG ME!</span>
                <img className='drag_arrow' src={Arrow}/>
            </>
            }
            <div className='header'>
                <h1><Sparkles>My Notes</Sparkles></h1>
                <p className='logout' onClick={logout}>Logout</p>
            </div>
            <NotesList />
        </div>
    )
}

export default Home;