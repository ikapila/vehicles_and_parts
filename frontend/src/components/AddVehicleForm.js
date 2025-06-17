import React, { useState } from 'react';
import { apiRequest } from '../services/api';

export default function AddVehicleForm({ token, onAdded }) {
  const [name, setName] = useState('');
  const [model, setModel] = useState('');
  const [stock, setStock] = useState(0);
  const [price, setPrice] = useState(0);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await apiRequest('/vehicles/', 'POST', { name, model, stock, price }, token);
      setName(''); setModel(''); setStock(0); setPrice(0);
      if (onAdded) onAdded();
    } catch (err) {
      setError('Failed to add vehicle');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add Vehicle</h3>
      <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
      <input type="text" placeholder="Model" value={model} onChange={e => setModel(e.target.value)} required />
      <input type="number" placeholder="Stock" value={stock} onChange={e => setStock(Number(e.target.value))} required />
      <input type="number" placeholder="Price" value={price} onChange={e => setPrice(Number(e.target.value))} required />
      <button type="submit">Add Vehicle</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}
