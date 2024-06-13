import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import WelcomePage from './components/WelcomePage';
import MainPage from './components/MainPage';
import Login from './components/Login';
import DictionaryItem from './components/DictionaryItem';
import MachineTable from './components/MachineTable';
import MaintenanceTable from './components/MaintenanceTable';
import ComplaintTable from './components/ComplaintTable';
import './App.css';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <Router>
      <div className="app-container">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<WelcomePage />} />
            <Route path="/main" element={isLoggedIn ? <MainPage /> : <Navigate to="/login" />} />
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
            <Route path="/machinetable" element={<MachineTable />} />
            <Route path="/maintenancetable" element={<MaintenanceTable />} />
            <Route path="/complainttable" element={<ComplaintTable />} />
            <Route path="/dictionary/:model/:name" element={<DictionaryItem />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;




