import React, { useState, useEffect } from 'react';
import apiClient from '../apiClient';  
import MachineTable from './MachineTable';
import MaintenanceTable from './MaintenanceTable';
import ComplaintTable from './ComplaintTable';
import './MainPage.css';

const MainPage = () => {
  const [activeTab, setActiveTab] = useState('info');
  const [machines, setMachines] = useState([]);
  const [maintenances, setMaintenances] = useState([]);
  const [complaints, setComplaints] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const machinesResponse = await apiClient.get('/machines/');
        console.log('Machines data:', machinesResponse.data);
        setMachines(machinesResponse.data);

        const maintenancesResponse = await apiClient.get('/maintenances/');
        console.log('Maintenances data:', maintenancesResponse.data);
        setMaintenances(maintenancesResponse.data);

        const complaintsResponse = await apiClient.get('/complaints/');
        console.log('Complaints data:', complaintsResponse.data);
        setComplaints(complaintsResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="main-container">
      <h2>Информация о комплектации и технических характеристиках Вашей техники</h2>
      <div className="tabs">
        <button onClick={() => setActiveTab('info')}>Общая инфо</button>
        <button onClick={() => setActiveTab('to')}>ТО</button>
        <button onClick={() => setActiveTab('complaints')}>Рекламации</button>
      </div>
      {activeTab === 'info' && <MachineTable data={machines} />}
      {activeTab === 'to' && <MaintenanceTable data={maintenances} />}
      {activeTab === 'complaints' && <ComplaintTable data={complaints} />}
    </div>
  );
};

export default MainPage;


