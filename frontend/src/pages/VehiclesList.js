import React, { useEffect, useState } from 'react';
import { apiRequest } from '../services/api';
import AddVehicleForm from '../components/AddVehicleForm';
import EditVehicleForm from '../components/EditVehicleForm';

export default function VehiclesList({ token }) {
  const [vehicles, setVehicles] = useState([]);
  const [error, setError] = useState('');
  const [editingId, setEditingId] = useState(null);

  const fetchVehicles = async () => {
    try {
      const data = await apiRequest('/vehicles/', 'GET', null, token);
      setVehicles(data);
    } catch (err) {
      setError('Failed to load vehicles');
    }
  };

  useEffect(() => {
    fetchVehicles();
    // eslint-disable-next-line
  }, [token]);

  const handleDelete = async (id) => {
    try {
      await apiRequest(`/vehicles/${id}`, 'DELETE', null, token);
      fetchVehicles();
    } catch (err) {
      setError('Failed to delete vehicle');
    }
  };

  return (
    <div>
      <h2>Vehicles</h2>
      <AddVehicleForm token={token} onAdded={fetchVehicles} />
      {error && <div className="error">{error}</div>}
      <ul>
        {vehicles.map(vehicle => (
          <li key={vehicle.id}>
            {editingId === vehicle.id ? (
              <EditVehicleForm
                token={token}
                vehicle={vehicle}
                onUpdated={() => { setEditingId(null); fetchVehicles(); }}
                onCancel={() => setEditingId(null)}
              />
            ) : (
              <>
                {vehicle.name} ({vehicle.model}) - Stock: {vehicle.stock} - Price: ${vehicle.price}
                <button onClick={() => setEditingId(vehicle.id)}>Edit</button>
                <button onClick={() => handleDelete(vehicle.id)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
