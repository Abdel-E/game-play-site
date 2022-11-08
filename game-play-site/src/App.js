import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Upload your python game in .exe format and play it here!
        </p>
        <button className="uploadButton" onClick={() => alert('Uploaded!')}>Upload your exe!</button>
      </header>
    </div>
  );
}

export default App;
