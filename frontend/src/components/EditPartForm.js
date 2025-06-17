import React, { useState } from 'react';
import { apiRequest } from '../services/api';

export default function EditPartForm({ token, part, onUpdated, onCancel }) {
  const [name, setName] = useState(part.name);
  const [stock, setStock] = useState(part.stock);
  const [price, setPrice] = useState(part.price);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await apiRequest(`/parts/${part.id}`, 'PUT', { name, stock, price }, token);
      if (onUpdated) onUpdated();
    } catch (err) {
      setError('Failed to update part');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 10 }}>
      <input type="text" value={name} onChange={e => setName(e.target.value)} required />
      <input type="number" value={stock} onChange={e => setStock(Number(e.target.value))} required />
      <input type="number" value={price} onChange={e => setPrice(Number(e.target.value))} required />
      <button type="submit">Save</button>
      <button type="button" onClick={onCancel}>Cancel</button>
      {error && <span className="error">{error}</span>}
    </form>
  );
}
