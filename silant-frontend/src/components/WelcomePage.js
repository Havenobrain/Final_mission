import React, { useState } from 'react';
import axios from 'axios';
import SearchResult from './SearchResult';
import './WelcomePage.css';

const WelcomePage = () => {
  const [serialNumber, setSerialNumber] = useState('');
  const [machine, setMachine] = useState(null);
  const [error, setError] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault(); 
    try {
      const response = await axios.get(`http://localhost:8000/api/machines/?serial_number=${serialNumber}`);
      if (response.data.length > 0) {
        setMachine(response.data[0]); 
        setError('');
      } else {
        setMachine(null);
        setError('Машина с указанным номером не найдена');
      }
    } catch (error) {
      console.error('There was an error fetching the machine data!', error);
      setError('Ошибка при получении данных. Пожалуйста, попробуйте еще раз.');
      setMachine(null);
    }
  };

  return (
    <div className="welcome-container">
      <p>Проверьте комплектацию и технические характеристики техники Силант</p>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Заводской номер"
          value={serialNumber}
          onChange={(e) => setSerialNumber(e.target.value)}
          className="serial-input"
        />
        <button type="submit" className="search-button">Поиск</button>
      </form>
      {error && <p className="error-message">{error}</p>}
      {machine && <SearchResult data={machine} />}
    </div>
  );
};

export default WelcomePage;




