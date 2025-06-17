import React, { useState } from 'react';
import { apiRequest } from '../services/api';

export default function AddPartForm({ token, onAdded }) {
  const [name, setName] = useState('');
  const [stock, setStock] = useState(0);
  const [price, setPrice] = useState(0);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      await apiRequest('/parts/', 'POST', { name, stock, price }, token);
      setName(''); setStock(0); setPrice(0);
      if (onAdded) onAdded();
    } catch (err) {
      setError('Failed to add part');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add Part</h3>
      <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
      <input type="number" placeholder="Stock" value={stock} onChange={e => setStock(Number(e.target.value))} required />
      <input type="number" placeholder="Price" value={price} onChange={e => setPrice(Number(e.target.value))} required />
      <button type="submit">Add Part</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}
