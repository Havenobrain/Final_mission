import React from 'react';
import './Footer.css';
import logo from '../assets/silant.png';

const Footer = () => (
  <footer className="footer">
    <div className="contact-info">+7-8352-20-12-09, Telegram</div>
    <img src={logo} alt="Силант" className="footer-logo" />
    <div className="year-info">Мой Силант 2022</div>
  </footer>
);

export default Footer;
