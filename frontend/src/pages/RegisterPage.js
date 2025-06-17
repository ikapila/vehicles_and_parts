import React, { useState } from 'react';
import { apiRequest } from '../services/api';

export default function RegisterPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [success, setSuccess] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      await apiRequest('/register', 'POST', { username, password });
      setSuccess('Registration successful! You can now log in.');
    } catch (err) {
      setError('Registration failed.');
    }
  };

  return (
    <div className="auth-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required />
        <button type="submit">Register</button>
      </form>
      {success && <div className="success">{success}</div>}
      {error && <div className="error">{error}</div>}
    </div>
  );
}
