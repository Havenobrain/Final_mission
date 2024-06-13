import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import MachineTable from './MachineTable';
import MaintenanceTable from './MaintenanceTable';
import ComplaintTable from './ComplaintTable';
import './MainPage.css';
import apiClient from '../apiClient';

const MainPage = () => {
  const [activeTab, setActiveTab] = useState('info');
  const [maintenances, setMaintenances] = useState([]);
  const [complaints, setComplaints] = useState([]);
  const navigate = useNavigate();

  const fetchData = useCallback(async () => {
    try {
      await fetchMaintenances();
      await fetchComplaints();
    } catch (error) {
      console.error('Error fetching data:', error);
      navigate('/login'); 
    }
  }, [navigate]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
    } else {
      fetchData();
    }
  }, [navigate, fetchData]);

  const fetchMaintenances = async () => {
    try {
      const response = await apiClient.get('/maintenances/');
      const data = response.data;
      console.log('Maintenances data:', data);
      setMaintenances(data);
    } catch (error) {
      console.error('Error fetching maintenances:', error);
      throw error; 
    }
  };

  const fetchComplaints = async () => {
    try {
      const response = await apiClient.get('/complaints/');
      const data = response.data;
      console.log('Complaints data:', data);
      setComplaints(data);
    } catch (error) {
      console.error('Error fetching complaints:', error);
      throw error; 
    }
  };

  return (
    <div className="main-container">
      <h2>Информация о комплектации и технических характеристиках Вашей техники</h2>
      <div className="tabs">
        <button onClick={() => setActiveTab('info')}>Общая инфо</button>
        <button onClick={() => setActiveTab('to')}>ТО</button>
        <button onClick={() => setActiveTab('complaints')}>Рекламации</button>
      </div>
      {activeTab === 'info' && <MachineTable />}
      {activeTab === 'to' && <MaintenanceTable data={maintenances} />}
      {activeTab === 'complaints' && <ComplaintTable data={complaints} />}
    </div>
  );
};

export default MainPage;



















