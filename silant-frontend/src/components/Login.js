import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    console.log('Attempting to log in with:', { username, password });
    axios.post('http://localhost:8000/api/token/', {
      username,
      password,
    })
    .then(response => {
      console.log('Login successful, response:', response);
      const { access } = response.data;
      console.log('Received token:', access); 
      localStorage.setItem('token', access);
      console.log('Token saved to localStorage:', localStorage.getItem('token')); 
      if (onLogin) {
        onLogin();
      }
      navigate('/main');
    })
    .catch(error => {
      console.error('Login error', error);
      if (error.response) {
        console.error('Error response data:', error.response.data);
      }
      setError('Invalid credentials');
    });
  };

  return (
    <div>
      <h2>Авторизация</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <input
        type="text"
        placeholder="Логин"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Войти</button>
    </div>
  );
};

export default Login;



