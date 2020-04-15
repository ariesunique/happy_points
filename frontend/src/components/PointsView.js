import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/Points.css';
import Points from './Points';
import $ from 'jquery';

class PointsView extends Component {
  constructor(){
    super();
    this.state = {
      currentDate: "",  
      points: [],  
      page: 1,
      totalEntries: 0,
      totalPoints: 0  
    }
  }

  componentDidMount() {
    this.getPoints();
  }
    
  getPoints = () => {
      this.setState({
          currentDate: "04-13-20",
          totalEntries: 3,
          totalPoints: 10,
          points: [{
              date: "04-01-20",
              numHappy: 5,
              numSad: 3,
              totalPoints: 2,
              notes: [ "talking back", "being rude"]
              },
          {
              date: "04-02-20",
              numHappy: 5,
              numSad: 0,
              totalPoints: 5,
              notes: ["excellent work"]
          },
           {
              date: "04-03-20",
              numHappy: 4,
              numSad: 1,
              totalPoints: 3,
              notes: ["listening the first time", "being a good helper"]
          }        
          ]
      })
  }
  
  selectPage(num) {
    this.setState({page: num}, () => this.getPoints());
  }

  createPagination(){
    let pageNumbers = [];
    let maxPage = Math.ceil(this.state.totalEntries / 10)
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
        <div className="Points-form-list-container">        
              <div className="Points-form" id="add-points">
                <h2>Add a Happy or Sad Face</h2>
                <div className="Points-form-row">
                    <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="small" onClick={() => this.props.questionAction('DELETE')}/>
                    <img src="happy-face.png" alt="" className="medium"/>
                    <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="small" onClick={() => this.props.questionAction('DELETE')}/>
                </div>
                <br/>
                <div className="Points-form-row">
                    <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="small" onClick={() => this.props.questionAction('DELETE')}/>
                    <img src="sad-face.png" alt="" className="medium" />
                    <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="small" onClick={() => this.props.questionAction('DELETE')}/>
                </div>
              <form onSubmit={this.handleSubmit}>
                  <label>Happy Faces:  <input placeholder="0" disabled="disabled" /></label>
                  <label>Sad Faces: <input placeholder="0" disabled="disabled" /></label>
                  <label>
                  Notes:
                  <textarea value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
              </form>
              </div>         
            <div className="Points-list">
              <h2 class="points-header">Points this week: <label id="score">{this.state.totalPoints}</label></h2>
              {this.state.points.map((p, ind) => (
                <Points
                  key={p.id}
                  numHappy={p.numHappy}
                  numSad={p.numSad}
                  date={p.date}
                  notes={p.notes}
                />
              ))}
              <div className="pagination-menu">
                {this.createPagination()}
              </div>
            </div>
      </div>
    );
  }
}

export default PointsView;
