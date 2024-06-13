import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './ComplaintTable.css';
import apiClient from '../apiClient';

const ComplaintTable = () => {
  const [complaints, setComplaints] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchComplaints = async () => {
      try {
        const response = await apiClient.get('/complaints/');
        setComplaints(response.data);
      } catch (error) {
        console.error('Error fetching complaints:', error);
        setError('Error fetching complaints');
      }
    };

    fetchComplaints();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  if (complaints.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div className="complaint-table-container">
      <div className="complaint-table-wrapper">
        <table className="complaint-fixed-header">
          <thead>
            <tr>
              <th>№ Машины</th>
              <th>Дата отказа</th>
              <th>Наработка, м/час</th>
              <th>Узел отказа</th>
              <th>Описание отказа</th>
              <th>Способ восстановления</th>
              <th>Используемые запасные части</th>
              <th>Дата восстановления</th>
              <th>Время простоя техники</th>
              <th>Сервисная компания</th>
            </tr>
          </thead>
          <tbody>
            {complaints.map((complaint, index) => (
              <tr key={index}>
                <td>{complaint.machine.serial_number || 'N/A'}</td>
                <td>{complaint.complaint_date || 'N/A'}</td>
                <td>{complaint.operating_hours || 'N/A'}</td>
                <td>
                  {complaint.failure_node ? (
                    <Link to={`/dictionary/failure_node/${encodeURIComponent(complaint.failure_node.name)}`}>
                      {complaint.failure_node.name}
                    </Link>
                  ) : ('N/A')}
                </td>
                <td>{complaint.failure_description || 'N/A'}</td>
                <td>
                  {complaint.recovery_method ? (
                    <Link to={`/dictionary/recovery_method/${encodeURIComponent(complaint.recovery_method.name)}`}>
                      {complaint.recovery_method.name}
                    </Link>
                  ) : 'N/A'}
                </td>
                <td>{complaint.parts_used || 'N/A'}</td>
                <td>{complaint.recovery_date || 'N/A'}</td>
                <td>{complaint.downtime || 'N/A'}</td>
                <td>{complaint.service_company || 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ComplaintTable;

















