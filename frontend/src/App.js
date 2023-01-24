import { useState } from 'react'
import './App.css'
import Draggable from 'react-draggable'
import Sparkles from './components/Sparkles.js'
import NotesList from './components/NotesList.js'
import amongus from './imgs/amongus.png'
import Arrow from './imgs/drag_sticker_arrow.svg'

function App() {
  const[prompt, setPrompt] = useState(true)

  function removePrompt() {
    const newPrompt = false
    setPrompt(newPrompt)
  }

  return (
    <div className="App">
      <Draggable>
        <img className='sticker amongus' src={amongus} alt='' draggable='false' onMouseDownCapture={removePrompt} />
      </Draggable>
      {prompt && 
        <>
        <span className='drag_prompt'>DRAG ME!</span>
        <img className='drag_arrow' src={Arrow}/>
        </>
      }
      <h1><Sparkles>My Notes</Sparkles></h1>
      <NotesList />
    </div>
  );
}

export default App;
