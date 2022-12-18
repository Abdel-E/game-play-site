import "./gameblock.css";

export default function GameBlock(game) {
  const download = () => {
    let gameFile = game.gameFile;
    let gameName = game.title;
    // using Java Script method to get PDF file
    fetch(gameFile).then((response) => {
      response.blob().then((blob) => {
        // Creating new object of PDF file
        const fileURL = window.URL.createObjectURL(blob);
        // Setting various property values
        let alink = document.createElement("a");
        alink.href = fileURL;
        alink.download = gameName + ".exe";
        alink.click();
      });
    });
  };

  return (
    <div className="gameblock">
      <div>
        <img src={game.thumbnail} alt={game.name} />
      </div>
      <div className="row">
        <div>
          <h3>{game.title}</h3>
          <p>{game.description}</p>
        </div>
        <div className="buttonDiv">
          <button className="downloadButton" onClick={download}>
            Click to Download!
          </button>
        </div>
      </div>
    </div>
  );
}
