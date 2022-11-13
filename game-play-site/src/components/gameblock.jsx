import "./gameblock.css";

export default function GameBlock(game) {
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
        <div className="downloadButton">
          <a href={game.downloadLink} download>
            Click to Download!
          </a>
        </div>
      </div>
    </div>
  );
}
