// src/App.js

import React from 'react';
import logo from './logo.svg';
import './App.scss'; // Updated import for CSS

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to Our Church</h1>
        <p>
          Join us in worship and fellowship.
        </p>
      </header>

      <section className="Welcome-section">
        <h2>Welcome</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper urna ac nulla bibendum, at tristique odio lacinia.
        </p>
      </section>

      <section className="Events-section">
        <h2>Upcoming Events</h2>
        <ul>
          <li>Sunday Service - 10:00 AM</li>
          <li>Bible Study - Wednesday, 7:00 PM</li>
          {/* Add more events as needed */}
        </ul>
      </section>

      <section className="Contact-section">
        <h2>Contact Us</h2>
        <p>
          Feel free to reach out to us for any inquiries or information.
        </p>
        <address>
          <p>123 Church Street</p>
          <p>Cityville, State 12345</p>
          <p>Email: info@ourchurch.org</p>
          <p>Phone: (123) 456-7890</p>
        </address>
      </section>

      <footer className="App-footer">
        <p>
          © {new Date().getFullYear()} Our Church
        </p>
      </footer>
    </div>
  );
}

export default App;
