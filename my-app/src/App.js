import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import TodoListHeader from './TodoListHeader';
import TodoList from "./TodoList";
class App extends Component{
  render(){
    const todoList = [
      'React practice',
      'game time'
    ];
    return (
      <div className="App">
        <TodoListHeader />
        <TodoList />
      </div>
    );
  }
}

export default App;
