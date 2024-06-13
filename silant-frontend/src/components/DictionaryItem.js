import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import apiClient from '../apiClient';
import './DictionaryItem.css';

const DictionaryItem = () => {
  const { model, name } = useParams();
  const [item, setItem] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log('Fetching item for model:', model, 'and name:', name); 
    if (model && name) {
      const fetchItem = async () => {
        try {
          const response = await apiClient.get(`/dictionary/${model}/${name}/`);
          console.log('Fetched item:', response.data); 
          setItem(response.data);
        } catch (error) {
          console.error('Error fetching dictionary item:', error);
          setError('Error fetching dictionary item');
        }
      };

      fetchItem();
    } else {
      console.error('Invalid parameters:', { model, name });
    }
  }, [model, name]);

  if (error) {
    return <div>{error}</div>;
  }

  if (!item) {
    return <div>Loading...</div>;
  }

  return (
    <div className="dictionary-item-container">
      <h2>Информация об элементе</h2>
      <table className="dictionary-item-table">
        <tbody>
          <tr>
            <td className="label">Название:</td>
            <td className="value">{item.name}</td>
          </tr>
          <tr>
            <td className="label">Описание:</td>
            <td className="value">{item.description || "Нет описания"}</td>
          </tr>
          {item.model && (
            <tr>
              <td className="label">Модель:</td>
              <td className="value">{item.model}</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default DictionaryItem;














