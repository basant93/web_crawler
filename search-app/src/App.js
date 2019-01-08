import React, { Component } from 'react';

import './App.css';
import Main from './component/Main'

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>This is a React App.</h1>
        <Main></Main>
      </div>
    );
  }
}

export default App;
