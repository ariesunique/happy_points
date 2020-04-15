import React, { Component } from 'react';
//import logo from '../logo.svg';
import '../stylesheets/Header.css';

class Header extends Component {

  navTo(uri){
    window.location.href = window.location.origin + uri;
  }

  render() {
    return (
      <div className="App-header">
        <h1 onClick={() => {this.navTo('')}}>Happy Points</h1> 
      </div>
    );
  }
}

export default Header;
