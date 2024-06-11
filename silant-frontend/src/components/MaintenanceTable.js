import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './MaintenanceTable.css';
import apiClient from '../apiClient';

const MaintenanceTable = () => {
  const [maintenances, setMaintenances] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMaintenances = async () => {
      try {
        const response = await apiClient.get('/maintenances/');
        setMaintenances(response.data);
      } catch (error) {
        console.error('Error fetching maintenances:', error);
        setError('Error fetching maintenances');
      }
    };

    fetchMaintenances();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  if (maintenances.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div className="maintenance-table-container">
      <div className="maintenance-table-wrapper">
        <table className="maintenance-fixed-header">
          <thead>
            <tr>
              <th>№ Машины</th>
              <th>Вид ТО</th>
              <th>Дата проведения ТО</th>
              <th>Наработка, м/час</th>
              <th>№ заказ-наряда</th>
              <th>Дата заказ-наряда</th>
              <th>Организация</th>
              <th>Сервисная компания</th>
            </tr>
          </thead>
          <tbody>
            {maintenances.map((maintenance, index) => (
              <tr key={index}>
                <td>{maintenance.machine.serial_number || 'N/A'}</td>
                <td>
                  {maintenance.maintenance_type ? (
                    <Link to={`/dictionary/${maintenance.maintenance_type.id}`}>
                      {maintenance.maintenance_type.name}
                    </Link>
                  ) : (
                    'N/A'
                  )}
                </td>
                <td>{maintenance.maintenance_date || 'N/A'}</td>
                <td>{maintenance.runtime_hours || 'N/A'}</td>
                <td>{maintenance.order_number || 'N/A'}</td>
                <td>{maintenance.order_date || 'N/A'}</td>
                <td>{maintenance.organization || 'N/A'}</td>
                <td>
                  {maintenance.service_company ? (
                    <Link to={`/dictionary/${maintenance.service_company.id}`}>
                      {maintenance.service_company}
                    </Link>
                  ) : (
                    'N/A'
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MaintenanceTable;













