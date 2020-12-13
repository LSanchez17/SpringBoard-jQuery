import React from "react";
import Board from "./Board";
import "./App.css";

/** Simple app that just shows the LightsOut game. */

function App() {
  return (
    <div className="App">
      <Board nrows={5} ncols={5} chanceLightStartsOn={() => Math.random()}/>
    </div>
  );
}

export default App;
