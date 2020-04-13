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
    const { numHappy, numSad, date } = this.props;  
    return (
        <div className="Question-holder">
        <span class="Points-status">
        <label>{date}</label>
        &nbsp;
        <label>{numHappy} <img className="small" alt="" src="happy-face.png"/></label>
        &nbsp;
        <label>{numSad} <img className="small" alt="" src="sad-face.png"/></label>
        </span>
        </div>
    );
  }
}

export default Points;
