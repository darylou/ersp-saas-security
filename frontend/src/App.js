import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {

  function handleClick() {
    axios.get('http://127.0.0.1/api/paste').then(res => {
      console.log(res.data)
    })
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={handleClick}>
          Click Me!
        </button>
      </header>
    </div>
  );
}

export default App;
