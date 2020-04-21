import React, { Component } from 'react';
import $ from 'jquery';

import '../stylesheets/Points.css';

class Points extends Component {
  constructor(props){
    super();
    this.state = {
      date: "today",
      totalPoints: 0,  
      numHappy: 0,
      numSad: 0,  
      notes: [],
    }
  }

  componentDidMount(){
  }


  submitQuestion = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/questions', //TODO: update request URL
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        question: this.state.question,
        answer: this.state.answer,
        difficulty: this.state.difficulty,
        category: this.state.category
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("add-question-form").reset();
        return;
      },
      error: (error) => {
        alert('Unable to add question. Please try your request again')
        return;
      }
    })
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  render() {
    const { numHappy, numSad, date, notes, totalPoints } = this.props;
    const listItems = notes.map((item) =>
      <li className="point-item" key={item}>{item}</li>
    );
    return (
        <div className="Points-holder">
        <span className="points">{date}</span>
        <span className="narrow">
            {numHappy} <img className="small" alt="" src="happy-face.png"/>
        </span>
        <span className="narrow">
            {numSad} <img className="small" alt="" src="sad-face.png"/>
        </span>      
        <span className="notes">
            <ul>
                {listItems}              
            </ul>
        </span>
        <span className="narrow">
            <label className="score">{totalPoints}</label>
        </span>
        </div>
    );
  }
}

export default Points;
