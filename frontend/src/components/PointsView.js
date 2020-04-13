import React, { Component } from 'react';

import '../stylesheets/App.css';
import Points from './Points';
import $ from 'jquery';

class PointsView extends Component {
  constructor(){
    super();
    this.state = {
      points: [],  
      page: 1,
      totalEntries: 0  
    }
  }

  componentDidMount() {
    this.getPoints();
  }
    

  getPoints = () => {
      this.setState({
          totalEntries: 1,
          points: [{
              date: "04-01-20",
              numHappy: 5,
              numSad: 3,
              totalPoints: 2
              },
          {
              date: "04-02-20",
              numHappy: 5,
              numSad: 0,
              totalPoints: 5
          },
           {
              date: "04-03-20",
              numHappy: 4,
              numSad: 1,
              totalPoints: 3
          }        
          ]
      })
  }
  
  getQuestions = () => {
    $.ajax({
      url: `/points?page=${this.state.page}`, //TODO: update request URL
      type: "GET",
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          categories: result.categories,
          currentCategory: result.current_category })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  selectPage(num) {
    this.setState({page: num}, () => this.getQuestions());
  }

  createPagination(){
    let pageNumbers = [];
    let maxPage = Math.ceil(this.state.totalQuestions / 10)
    for (let i = 1; i <= maxPage; i++) {
      pageNumbers.push(
        <span
          key={i}
          className={`page-num ${i === this.state.page ? 'active' : ''}`}
          onClick={() => {this.selectPage(i)}}>{i}
        </span>)
    }
    return pageNumbers;
  }

  getByCategory= (id) => {
    $.ajax({
      url: `/categories/${id}/questions`, //TODO: update request URL
      type: "GET",
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  submitSearch = (searchTerm) => {
    $.ajax({
      url: `/questions`, //TODO: update request URL
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({searchTerm: searchTerm}),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
  }

  questionAction = (id) => (action) => {
    if(action === 'DELETE') {
      if(window.confirm('are you sure you want to delete the question?')) {
        $.ajax({
          url: `/questions/${id}`, //TODO: update request URL
          type: "DELETE",
          success: (result) => {
            this.getQuestions();
          },
          error: (error) => {
            alert('Unable to load questions. Please try your request again')
            return;
          }
        })
      }
    }
  }

  render() {
    return (

        <div className="question-view">
        
      <div id="add-points">
        <h2>Add a Happy or Sad Face</h2>
        <div>
            <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
            <img className="points" alt="" src="happy-face.png"/>
            <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
        </div>
        <br/>
        <div>
            <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
            <img className="points" alt="" src="sad-face.png"/>
            <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
        </div>
      </div>      

      
      
        <div className="questions-list">
          <h2>Points this week</h2>
          {this.state.points.map((p, ind) => (
            <Points
              key={p.id}
              numHappy={p.numHappy}
              numSad={p.numSad}
              date={p.date}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default PointsView;
