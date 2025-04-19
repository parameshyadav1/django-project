import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Todo() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    const res = await axios.get('/api/todos/');
    setTodos(res.data);
  };

  const addTodo = async () => {
    await axios.post('/api/todos/', { title, completed: false });
    fetchTodos();
    setTitle('');
  };

  return (
    <div>
      <input value={title} onChange={(e) => setTitle(e.target.value)} />
      <button onClick={addTodo}>Add</button>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Todo;