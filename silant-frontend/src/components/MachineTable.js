import React from 'react';

const MachineTable = ({ data }) => (
  <table>
    <thead>
      <tr>
        <th>Зав. № машины</th>
        <th>Модель</th>
        <th>Модель двигателя</th>
        <th>Модель трансмиссии</th>
        <th>Модель ведущего моста</th>
        <th>Модель рулевого моста</th>
      </tr>
    </thead>
    <tbody>
      {data.map(machine => (
        <tr key={machine.serial_number}>
          <td>{machine.serial_number}</td>
          <td>{machine.model}</td>
          <td>{machine.engine_model}</td>
          <td>{machine.transmission_model}</td>
          <td>{machine.drive_axle_model}</td>
          <td>{machine.steer_axle_model}</td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default MachineTable;
