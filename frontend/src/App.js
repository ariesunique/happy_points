import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

// import logo from './logo.svg';
import './stylesheets/App.css';
import Header from './components/Header';
import PointsView from './components/PointsView';


class App extends Component {
  render() {
    return (
    <div className="App">
      <Header path />
      <Router>
        <Switch>
          <Route path="/" exact component={PointsView} />
        </Switch>
      </Router>
    </div>
    );
  }
}

export default App;
