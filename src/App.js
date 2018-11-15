import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>
            Turret View
          </p>
          <div className="Video" />
          <div className="Controls" />
        </header>
      </div>
    );
  }
}

export default App;
