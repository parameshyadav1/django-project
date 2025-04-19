// frontend/src/App.js
import React, { useState } from 'react';  // Add useState import
import './App.css';

function App() {  // Remove unused 'App' warning
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  // Example addTodo function (remove if not needed)
  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, input]);
      setInput('');
    }
  };

  return (
    <div className="App">
      <h1>Todo App</h1>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={addTodo}>Add Todo</button>  {/* Using addTodo */}
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>{todo}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;