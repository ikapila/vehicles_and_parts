// src/services/api.js
// API service for backend communication

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export async function apiRequest(endpoint, method = 'GET', data = null, token = null) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;
  const options = {
    method,
    headers,
  };
  if (data) options.body = JSON.stringify(data);
  const response = await fetch(`${API_URL}${endpoint}`, options);
  if (!response.ok) throw new Error(await response.text());
  return response.json();
}
