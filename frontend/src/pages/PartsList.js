import React, { useEffect, useState } from 'react';
import { apiRequest } from '../services/api';
import AddPartForm from '../components/AddPartForm';
import EditPartForm from '../components/EditPartForm';

export default function PartsList({ token }) {
  const [parts, setParts] = useState([]);
  const [error, setError] = useState('');
  const [editingId, setEditingId] = useState(null);

  const fetchParts = async () => {
    try {
      const data = await apiRequest('/parts/', 'GET', null, token);
      setParts(data);
    } catch (err) {
      setError('Failed to load parts');
    }
  };

  useEffect(() => {
    fetchParts();
    // eslint-disable-next-line
  }, [token]);

  const handleDelete = async (id) => {
    try {
      await apiRequest(`/parts/${id}`, 'DELETE', null, token);
      fetchParts();
    } catch (err) {
      setError('Failed to delete part');
    }
  };

  return (
    <div>
      <h2>Parts</h2>
      <AddPartForm token={token} onAdded={fetchParts} />
      {error && <div className="error">{error}</div>}
      <ul>
        {parts.map(part => (
          <li key={part.id}>
            {editingId === part.id ? (
              <EditPartForm
                token={token}
                part={part}
                onUpdated={() => { setEditingId(null); fetchParts(); }}
                onCancel={() => setEditingId(null)}
              />
            ) : (
              <>
                {part.name} - Stock: {part.stock} - Price: ${part.price}
                <button onClick={() => setEditingId(part.id)}>Edit</button>
                <button onClick={() => handleDelete(part.id)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
