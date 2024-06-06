import React, { useState } from 'react';
import axios from 'axios';
import SearchResult from './SearchResult';
import './WelcomePage.css';

const WelcomePage = () => {
  const [serialNumber, setSerialNumber] = useState('');
  const [searchResult, setSearchResult] = useState(null);

  const handleSearch = () => {
    axios.get(`/api/machines?serial_number=${serialNumber}`)
      .then(response => {
        setSearchResult(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the machine data!', error);
        setSearchResult(null);
      });
  };

  return (
    <div className="welcome-container">
      <p>Проверьте комплектацию и технические характеристики техники Силант</p>
      <input
        type="text"
        placeholder="Заводской номер"
        value={serialNumber}
        onChange={(e) => setSerialNumber(e.target.value)}
        className="serial-input"
      />
      <button onClick={handleSearch} className="search-button">Поиск</button>
      {searchResult && <SearchResult data={searchResult} />}
    </div>
  );
};

export default WelcomePage;