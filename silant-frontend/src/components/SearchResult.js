import React from 'react';
import './SearchResult.css';

const fieldNames = {
  serial_number: 'Зав. № машины',
  model: 'Модель',
  engine_model: 'Модель двигателя',
  transmission_model: 'Модель трансмиссии',
  drive_axle_model: 'Модель ведущего моста',
  steer_axle_model: 'Модель рулевого моста'
};

const SearchResult = ({ data }) => {
  return (
    <div className="search-results">
      <p>Информация о комплектации и технических характеристиках Вашей техники</p>
      <table className="result-table">
        <thead>
          <tr>
            <th>Поле</th>
            <th>Значение</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key}>
              <td>{fieldNames[key] || key}</td>
              <td>{value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SearchResult;


