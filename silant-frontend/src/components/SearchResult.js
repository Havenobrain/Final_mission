import React from 'react';

const SearchResult = ({ data }) => {
  return (
    <div className="search-results">
      <p>Информация о комплектации и технических характеристиках Вашей техники</p>
      <table>
        <thead>
          <tr>
            <th>Поле</th>
            <th>Значение</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key}>
              <td>{key}</td>
              <td>{value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SearchResult;