import React, { useState } from 'react';
import { apiRequest } from '../services/api';

export default function EditVehicleForm({ token, vehicle, onUpdated, onCancel }) {
  const [name, setName] = useState(vehicle.name);
  const [model, setModel] = useState(vehicle.model);
  const [stock, setStock] = useState(vehicle.stock);
  const [price, setPrice] = useState(vehicle.price);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await apiRequest(`/vehicles/${vehicle.id}`, 'PUT', { name, model, stock, price }, token);
      if (onUpdated) onUpdated();
    } catch (err) {
      setError('Failed to update vehicle');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 10 }}>
      <input type="text" value={name} onChange={e => setName(e.target.value)} required />
      <input type="text" value={model} onChange={e => setModel(e.target.value)} required />
      <input type="number" value={stock} onChange={e => setStock(Number(e.target.value))} required />
      <input type="number" value={price} onChange={e => setPrice(Number(e.target.value))} required />
      <button type="submit">Save</button>
      <button type="button" onClick={onCancel}>Cancel</button>
      {error && <span className="error">{error}</span>}
    </form>
  );
}
