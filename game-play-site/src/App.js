import './App.css';
import React from 'react';

import thumbnail from './assets/pong-thumb.png';

import GameBlock from './components/gameblock';

function App(game) {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Play other Students Games!</h1>
      </header>
      <div className="gameList">
        <GameBlock
          title="Pong"
          thumbnail={thumbnail}
          description="A classic game of Pong"
          downloadLink="./assets/pong.exe"
        />
      </div>
    </div>
  );
}

export default App;
