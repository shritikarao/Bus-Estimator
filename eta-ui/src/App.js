/*
1. Scaffold your React app:
   npx create-react-app eta-ui
   cd eta-ui

2. Replace src/App.js with the following:
*/
import React, { useState, useEffect } from 'react';
import './App.css';

// Copy your stops arrays from eta_predictor.py into this mapping:
const stopsByLine = {
  Gold: [
    "Arlington Bldf at Milmont Street",
    "Arlington Bld at Jeffersonian Apartments",
    "Massie Rd at Law School",
    "Massie Rd at Faulkner Apartments",
    "Massie Rd at JPJ South",
    "Emmet Street at Goodwin Bridge",
    "Emmet Street at Emmet/Ivy Garage",
    "Emmet Street at Alumni Hall",
    "Emmet Street at Ridley Hall",
    "White Rd at Chemistry Drive",
    "Alderman Road at Gooch/Dillard",
    "Stadium Road at Runk Dining Hall",
    "Hereford Dr at Runk Dining Hall",
    "Hereford Dr at Johnson House",
    "McCormick Rd at Kellogg House",
    "McCormick Rd at Lile-Maupin House",
    "Alderman Rd at O-Hill Dining Hall",
    "Whitehead Rd at Scott Stadium",
    "Emmet St at Central Grounds Garage",
    "Emmet Street at Snyder Tennis Courts",
    "Emmet St at Emmy/Ivy Garage",
    "Emmet St at Goodwin Bridge (Northbound)",
    "Massie Rd at JPJ West",
    "Massie Rd at Faulkner Apartments",
    "Massie Rd at North Grounds Rec",
    "Massie Rd at Copely Apartments",
    "Arlington Bld at Milmont St",
    "Arlington Bld at Barracks Rd Shopping"
  ],
  Orange: [
    "Madison Ave at Preston Ave",
    "Preston Ave at Washington Park",
    "Grady Ave at 10 ½ St",
    "Grady Ave at 14th St",
    "14th Street at Virginia Ave",
    "14th Street at Wertland St (Southbound)",
    "Jefferson Park Ave at UVA Medical Center",
    "Jefferson Park Ave at Cabell Hall",
    "Jefferson Park Ave at Montebello Circle",
    "Jefferson Park Ave at Shamrock Rd (Southbound)",
    "Jefferson Park Ave at Maury Ave",
    "Maury Ave at Clark Ct",
    "Alderman Rd at Gooch/Dillard (Northbound)",
    "Whitehead Rd at Scott Stadium",
    "Stadium Rd at Stadium Garage",
    "Stadium Rd at Alderman Rd",
    "Jefferson Park Ave at Observatory Ave",
    "Jefferson Park Ave at Shamrock Rd (Northbound)",
    "Jefferson Park Ave at Kent Terrace",
    "Jefferson Park Ave at Valley Rd",
    "Jefferson Park Ave at Brandon Ave",
    "Jefferson Park Ave at Pinn Hall",
    "14th Street at Wertland St (Northbound)",
    "14th Street at John St",
    "Madison Ave at Grady Ave"
  ],
  Green: [
    "Madison Ave at Preston Ave",
    "Preston Ave at Washington Park",
    "Grady Ave at 10 ½ St",
    "Grady Ave at 14th St",
    "Grady Ave at Preston Pl",
    "Rugy Rd at Lambeth Ln",
    "University Ave at Newcomb Rd (Westbound)",
    "Emmet St at Alumni Hall (026)",
    "McCormick Rd at McCormick Rd Dorms",
    "Alderman Rd at O-Hill Dining Hall",
    "Alderman Rd at Gooch/Dillard",
    "Whitehead Rd at Chemistry Drive",
    "Alderman Rd at AFC",
    "McCormick Rd at Chemistry Building",
    "McCormick Rd at Thonton Hall",
    "Emmet St at Central Grounds Garage",
    "Emmet St at Snyder Tennis Courts",
    "University Ave at Newcomb Rd (Eastbound)",
    "Rugby Rd at Lambeth Ln (Northbound)",
    "Rugby Rd at Lambeth Ln (Northbound)",
    "Graedy Ave at 16th St",
    "Madison Ave at Grady Ave"
  ]
};

function App() {
  const lines = Object.keys(stopsByLine);
  const [form, setForm] = useState({
    line: lines[0],
    stop: stopsByLine[lines[0]][0],
    time: '',
    weather: 'Clear',
    bus_load: 'Low'
  });
  const [stops, setStops] = useState(stopsByLine[lines[0]]);
  const [eta, setEta] = useState(null);

  // Update stops when line changes
  useEffect(() => {
    const list = stopsByLine[form.line] || [];
    setStops(list);
    setForm(f => ({ ...f, stop: list[0] }));
  }, [form.line]);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:8080/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
      const data = await res.json()
      setEta(data.eta)
    } catch (err) {
      console.error(err)
      alert('Could not fetch ETA')
    }
  }

  return (
    <div className="App">
      <h1>ETA Predictor</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Line:
          <select name="line" value={form.line} onChange={handleChange}>
            {lines.map(l => <option key={l} value={l}>{l}</option>)}
          </select>
        </label>

        <label>
          Stop:
          <select name="stop" value={form.stop} onChange={handleChange}>
            {stops.map(s => <option key={s} value={s}>{s}</option>)}
          </select>
        </label>

        <label>
          Time (e.g. 3:25 PM):
          <input type="text" name="time" value={form.time} onChange={handleChange} required />
        </label>

        <label>
          Weather:
          <select name="weather" value={form.weather} onChange={handleChange}>
            {['Clear','Rainy','Snowy'].map(w => <option key={w} value={w}>{w}</option>)}
          </select>
        </label>

        <label>
          Bus Load:
          <select name="bus_load" value={form.bus_load} onChange={handleChange}>
            {['Low','Medium','High'].map(b => <option key={b} value={b}>{b}</option>)}
          </select>
        </label>

        <button type="submit">Predict ETA</button>
      </form>

      {eta && (
        <div className="result">
          <h2>Estimated Arrival:</h2>
          <p>{eta}</p>
        </div>
      )}
    </div>
  );
}

export default App;

/*
3. Enable CORS on your Python backend (Flask/FastAPI) and run it on port 5000.
4. Start React UI:
   npm start
*/

