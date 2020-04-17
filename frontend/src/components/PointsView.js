import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/Points.css';
import Points from './Points';
//import $ from 'jquery';

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
          happy: 0,
          sad: 0,
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

    onClickHappyPlus = () => {
        if (this.state.happy < 3) {
            this.setState({
                happy: this.state.happy + 1
            })
        }
    }

    onClickHappyMinus = () => {
        if (this.state.happy > 0) {
            this.setState({
                happy: this.state.happy - 1
            })
        }
    }

    onClickSadPlus = () => {
        if (this.state.sad < 3) {
            this.setState({
                sad: this.state.sad + 1
            })
        }
    }

    onClickSadMinus = () => {
        if (this.state.sad > 0) {
            this.setState({
                sad: this.state.sad - 1
            })
        }
    }

  render() {
    return (
        <div className="Points-form-list-container">        
              <div className="Points-form" id="add-points">
                <h2>Add a Happy or Sad Face</h2>
                <div className="Points-form-row">
                    <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="small" onClick={this.onClickHappyPlus}/>
                    <img src="happy-face.png" alt="" className="medium"/>
                    <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="small" onClick={this.onClickHappyMinus}/>
                </div>
                <br/>
                <div className="Points-form-row">
                    <img src="https://img.icons8.com/android/24/000000/plus.png" alt="" className="small" onClick={this.onClickSadPlus}/>
                    <img src="sad-face.png" alt="" className="medium" />
                    <img src="https://img.icons8.com/android/24/000000/minus.png" alt="" className="small" onClick={this.onClickSadMinus}/>
                </div>
              <form className="happyface-form" onSubmit={this.handleSubmit}>
                    
                  <div><span className="formtext">Happy:</span><input class="forminput" id="happy-input" name="happy-input" placeholder={this.state.happy}  /></div>
                  <div><span className="formtext">Sad:</span><input class="forminput" id="sad-input" name="sad-input" placeholder={this.state.sad}  /></div>
                  <div><span className="formtext">
                  Notes:
                  </span>
                  <textarea name="notes-input" value={this.state.value} onChange={this.handleChange} />
                  </div>
                    <div class="newline"><input class="button" type="submit" value="Submit" /></div>
              </form>
              </div>         
            <div className="Points-list">
              <h2 class="points-header">Points this week: <label class="score">{this.state.totalPoints}</label></h2>
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
