import React, { Component } from 'react';
import './App.css';
import Home from './components/scenes/Home';
import Cat from './components/cat/Cat';
import TextBox from './components/TextBox';
import Button from './components/form/Button'

class App extends Component {

  constructor(props) {
    super(props)

    this.state = {
      foods: [],
      inputValue: ''
    }
    this.addFood = this.addFood.bind(this);
    this.updateInputValue = this.updateInputValue.bind(this);

  }

  addFood() {
    const foods = this.state.foods;

    if (this.state.inputValue) {
      foods.push(this.state.inputValue);

      this.setState({
        foods: foods,
        inputValue: ''
      })
    }
  }

  updateInputValue(value) {
    this.setState({
      inputValue: value
    });
  }

  render() {
    return (
      <Home>
        <div>
          <Cat color='Black'/>
        </div>
        <TextBox value={this.state.inputValue}
                 onChange={this.updateInputValue}/>
        <Button onClick={this.addFood}
                text='ADD'/>
        <ul>
          {this.state.foods.map((food, index) => (
            <li key={'foods:' + index}> {food}</li>
          ))}
        </ul>
      </Home>
    );
  }
}

export default App;
