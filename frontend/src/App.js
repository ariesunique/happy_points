import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

// import logo from './logo.svg';
import './stylesheets/App.css';
import QuestionView from './components/QuestionView';
import Header from './components/Header';
import QuizView from './components/QuizView';
import Points from './components/Points';
import PointsView from './components/PointsView';


class App extends Component {
  render() {
    return (
    <div className="App">
      <Header path />
      <Router>
        <Switch>
          <Route path="/" exact component={PointsView} />
          <Route path="/list" exact component={PointsView} />
          <Route path="/add" component={Points} />
          <Route path="/play" component={QuizView} />
        </Switch>
      </Router>
    </div>
  );

  }
}

export default App;
