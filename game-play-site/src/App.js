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
          gameFile={require('./assets/pong.exe')}
          title="Pong"
          thumbnail={thumbnail}
          description="A classic game of Pong"
        />
        <GameBlock
          gameFile={require('./assets/jet.exe')}
          title="Jet Fighter"
          thumbnail={require('./assets/jet-thumb.png')}
          description="A action packed game of jet fighting"
        />
        <GameBlock
          gameFile={require('./assets/motel.exe')}
          title="Motel Madness"
          thumbnail={require('./assets/motel-thumb.png')}
          description="A mysterious motel search"
        />
        <GameBlock
          gameFile={require('./assets/rocio.exe')}
          title="Haunted House Adventure"
          thumbnail={require('./assets/haunted-thumb.png')}
          description="A deep dive into a haunted house"
        />
      </div>
    </div>
  );
}

export default App;
