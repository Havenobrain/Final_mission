import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
});

apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

apiClient.interceptors.response.use(response => {
  return response;
}, async error => {
  const originalRequest = error.config;

  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    const refreshToken = localStorage.getItem('refresh_token');
    try {
      const response = await axios.post('http://localhost:8000/api/token/refresh/', { refresh: refreshToken });
      localStorage.setItem('token', response.data.access);
      originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
      return apiClient(originalRequest);
    } catch (err) {
      console.error('Refresh token is expired or invalid:', err);
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
      window.location.href = '/login';
    }
  }

  return Promise.reject(error);
});

export default apiClient;


