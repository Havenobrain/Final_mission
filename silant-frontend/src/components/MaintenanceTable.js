import React from 'react';
import './MaintenanceTable.css';

const MaintenanceTable = ({ data }) => {
  console.log('Maintenance data in MaintenanceTable:', data);

  return (
    <table>
      <thead>
        <tr>
          <th>Машина</th>
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
        {data.map(maintenance => (
          <tr key={maintenance.id}>
            <td>{maintenance.machine.serial_number}</td>
            <td>{maintenance.maintenance_type.name}</td>
            <td>{maintenance.maintenance_date}</td>
            <td>{maintenance.runtime_hours}</td>
            <td>{maintenance.order_number}</td>
            <td>{maintenance.order_date}</td>
            <td>{maintenance.organization.name}</td>
            <td>{maintenance.service_company.username}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default MaintenanceTable;

