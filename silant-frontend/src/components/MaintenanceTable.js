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
        console.log('Fetched Maintenances:', response.data);
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
                    <Link to={`/dictionary/maintenance_type/${encodeURIComponent(maintenance.maintenance_type.name)}`}>
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
                <td>
                  {maintenance.organization ? (
                    <Link to={`/dictionary/organization/${encodeURIComponent(maintenance.organization.name)}`}>
                      {maintenance.organization.name}
                    </Link>
                  ) : (
                    'N/A'
                  )}
                </td>
                <td>{maintenance.service_company || 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MaintenanceTable;





























