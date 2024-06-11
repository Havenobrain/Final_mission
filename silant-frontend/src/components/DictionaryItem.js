import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import apiClient from '../apiClient';

const DictionaryItem = () => {
  const { id } = useParams();
  const [item, setItem] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchItem = async () => {
      try {
        const response = await apiClient.get(`/dictionary/${id}/`);
        setItem(response.data);
      } catch (error) {
        console.error('Error fetching dictionary item:', error);
        setError('Error fetching dictionary item');
      }
    };

    fetchItem();
  }, [id]);

  if (error) {
    return <div>{error}</div>;
  }

  if (!item) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{item.name}</h2>
      <p>{item.description || "Описание"}</p>
    </div>
  );
};

export default DictionaryItem;







