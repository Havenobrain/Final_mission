import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';
import logo from '../assets/logo.png';

const Header = () => {
  const navigate = useNavigate();

  const handleAuthClick = () => {
    navigate('/login');
  };

  return (
    <header className="header">
      <div className="logo-container">
        <img src={logo} alt="Silant Logo" className="logo" />
      </div>
      <div className="contact-info">
        <p>+7-8352-20-12-09, telegram</p>
      </div>
      <nav>
        <ul className="nav-links">
          <li><Link to="/" className="nav-link">Главная</Link></li>
          <li><Link to="/main" className="nav-link">Информация</Link></li>
        </ul>
      </nav>
      <button className="auth-button" onClick={handleAuthClick}>Авторизация</button>
    </header>
  );
};

export default Header;




