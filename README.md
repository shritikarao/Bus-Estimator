# Multi-Line ETA Predictor

A simple command-line tool that uses historical Transloc bus data to predict delays and compute an estimated time of arrival (ETA) for any stop on the Gold, Orange, or Green line.

## Features

- Simulated historical data for three lines (Gold, Orange, Green) under different weather and load conditions  
- Encodes categorical features (line, stop name, weather, load) with `LabelEncoder`  
- Trains a separate `LinearRegression` model per line  
- Interactive prompt to select line, stop, scheduled time, weather, and bus load  
- Outputs an ETA in `h:mm AM/PM` format  

## Requirements

- Python 3.7+  
- See `requirements.txt` for full list of dependencies  

## Installation

1. Clone or download this repository  
2. (Optional) Create and activate a virtual environment:  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
