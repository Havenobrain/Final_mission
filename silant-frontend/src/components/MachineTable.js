import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './MachineTable.css';
import apiClient from '../apiClient';

const MachineTable = () => {
  const [machines, setMachines] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMachines = async () => {
      try {
        const response = await apiClient.get('/machines/');
        console.log('Fetched Machines:', response.data);
        setMachines(response.data);
      } catch (error) {
        console.error('Error fetching machines:', error);
        setError('Error fetching machines');
      }
    };

    fetchMachines();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  if (machines.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div className="machine-table-container">
      <div className="machine-table-wrapper">
        <table className="machine-fixed-header">
          <thead>
            <tr>
              <th>№ Машины</th>
              <th>Модель</th>
              <th>Модель двигателя</th>
              <th>№ двигателя</th>
              <th>Модель трансмиссии</th>
              <th>№ трансмиссии</th>
              <th>Модель ведущего моста</th>
              <th>№ ведущего моста</th>
              <th>Модель рулевого моста</th>
              <th>№ рулевого моста</th>
              <th>Дата поставки</th>
              <th>Клиент</th>
              <th>Конечный пользователь</th>
              <th>Адрес доставки</th>
              <th>Дополнительные опции</th>
              <th>Сервисная компания</th>
            </tr>
          </thead>
          <tbody>
            {machines.map((machine, index) => (
              <tr key={index}>
                <td>{machine.serial_number || 'N/A'}</td>
                <td>
                  <Link to={`/dictionary/model/${machine.model}`}>
                    {machine.model || 'N/A'}
                  </Link>
                </td>
                <td>
                  <Link to={`/dictionary/engine_model/${machine.engine_model}`}>
                    {machine.engine_model || 'N/A'}
                  </Link>
                </td>
                <td>{machine.engine_number || 'N/A'}</td>
                <td>
                  <Link to={`/dictionary/transmission_model/${machine.transmission_model}`}>
                    {machine.transmission_model || 'N/A'}
                  </Link>
                </td>
                <td>{machine.transmission_number || 'N/A'}</td>
                <td>
                  <Link to={`/dictionary/drive_axle_model/${machine.drive_axle_model}`}>
                    {machine.drive_axle_model || 'N/A'}
                  </Link>
                </td>
                <td>{machine.drive_axle_number || 'N/A'}</td>
                <td>
                  <Link to={`/dictionary/steer_axle_model/${machine.steer_axle_model}`}>
                    {machine.steer_axle_model || 'N/A'}
                  </Link>
                </td>
                <td>{machine.steer_axle_number || 'N/A'}</td>
                <td>{machine.supply_date || 'N/A'}</td>
                <td>{machine.client || 'N/A'}</td>
                <td>{machine.end_user || 'N/A'}</td>
                <td>{machine.delivery_address || 'N/A'}</td>
                <td>{machine.additional_options || 'N/A'}</td>
                <td>{machine.service_company || 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MachineTable;












