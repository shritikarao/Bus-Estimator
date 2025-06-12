import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

# Gold Line Stops
gold_line_stops = [
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
]

# Orange Line Stops
orange_line_stops = [
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
]

green_line_stops = [
    "Madison Ave at Preston Ave",
    "Preston Ave @ Washington Park",
    "Grady Ave at 10 ½ St",
    "Grady Ave at 14th St",
    "Grady Ave at Preston Pl",
    "Rugy Rd @ Lambeth Ln",
    "University Ave @ Newcomb Rd (Westbound)",
    "Emmet St @ Alumni Hall (026)",
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
    "Rugby Rd @ Lambeth Ln (Northbound)",
    "Rugby Rd @ Lambeth Ln (Northbound)",
    "Graedy Ave @ 16th St",
    "Madison Ave @ Grady Ave"
]

# Collected Gold Line data
# Each entry: (Stop Name, Bus Load, Weather, Delay)
gold_samples = [
    # Clear, Low/Medium Load, Short Delays
    ("Massie Rd at JPJ South", "Low", "Clear", 2),
    ("Massie Rd at JPJ South", "Medium", "Clear", 4),
    ("White Rd at Chemistry Drive", "Low", "Clear", 3),
    ("Alderman Road at Gooch/Dillard", "Medium", "Clear", 5),
    ("Stadium Road at Runk Dining Hall", "Low", "Clear", 2),
    ("Hereford Dr at Johnson House", "Medium", "Clear", 6),
    ("McCormick Rd at Kellogg House", "Low", "Clear", 3),
    ("McCormick Rd at Lile-Maupin House", "Medium", "Clear", 5),
    ("Alderman Rd at O-Hill Dining Hall", "Low", "Clear", 4),
    ("Whitehead Rd at Scott Stadium", "Medium", "Clear", 6),
    ("Emmet Street at Goodwin Bridge", "Low", "Clear", 2),
    ("Emmet Street at Alumni Hall", "Medium", "Clear", 4),
    # Rainy, Medium/High Load, Higher Delays
    ("Massie Rd at JPJ South", "High", "Rainy", 10),
    ("White Rd at Chemistry Drive", "Medium", "Rainy", 8),
    ("Alderman Road at Gooch/Dillard", "High", "Rainy", 12),
    ("Stadium Road at Runk Dining Hall", "Medium", "Rainy", 9),
    ("Hereford Dr at Johnson House", "High", "Rainy", 13),
    ("McCormick Rd at Kellogg House", "Medium", "Rainy", 8),
    ("McCormick Rd at Lile-Maupin House", "High", "Rainy", 11),
    ("Alderman Rd at O-Hill Dining Hall", "Medium", "Rainy", 9),
    ("Whitehead Rd at Scott Stadium", "High", "Rainy", 14),
    ("Emmet Street at Goodwin Bridge", "Medium", "Rainy", 7),
    ("Emmet Street at Alumni Hall", "High", "Rainy", 12),
    # Snowy, High Load, Long Delays
    ("Massie Rd at JPJ South", "High", "Snowy", 18),
    ("White Rd at Chemistry Drive", "High", "Snowy", 20),
    ("Alderman Road at Gooch/Dillard", "High", "Snowy", 22),
    ("Stadium Road at Runk Dining Hall", "High", "Snowy", 19),
    ("Hereford Dr at Johnson House", "High", "Snowy", 21),
    ("McCormick Rd at Kellogg House", "High", "Snowy", 20),
    ("McCormick Rd at Lile-Maupin House", "High", "Snowy", 23),
    ("Alderman Rd at O-Hill Dining Hall", "High", "Snowy", 22),
    ("Whitehead Rd at Scott Stadium", "High", "Snowy", 24),
    ("Emmet Street at Goodwin Bridge", "High", "Snowy", 19),
    ("Emmet Street at Alumni Hall", "High", "Snowy", 21),
    # Some mixed cases
    ("Emmet Street at Ridley Hall", "Medium", "Rainy", 10),
    ("Emmet Street at Ridley Hall", "Low", "Clear", 3),
    ("Emmet Street at Ridley Hall", "High", "Snowy", 20),
    ("Arlington Bld at Jeffersonian Apartments", "Low", "Clear", 2),
    ("Arlington Bld at Jeffersonian Apartments", "Medium", "Rainy", 8),
    ("Arlington Bld at Jeffersonian Apartments", "High", "Snowy", 18),
]

# Collected Orange Line data
# Each entry: (Stop Name, Bus Load, Weather, Delay)
orange_samples = [
    # Clear, Low/Medium Load, Short Delays
    ("Madison Ave at Preston Ave", "Low", "Clear", 1),
    ("Preston Ave at Washington Park", "Low", "Clear", 2),
    ("Grady Ave at 10 ½ St", "Medium", "Clear", 4),
    ("Grady Ave at 14th St", "Low", "Clear", 2),
    ("14th Street at Virginia Ave", "Medium", "Clear", 5),
    ("14th Street at Wertland St (Southbound)", "Low", "Clear", 3),
    ("Jefferson Park Ave at UVA Medical Center", "Medium", "Clear", 4),
    ("Jefferson Park Ave at Cabell Hall", "Low", "Clear", 2),
    ("Jefferson Park Ave at Montebello Circle", "Medium", "Clear", 5),
    ("Jefferson Park Ave at Shamrock Rd (Southbound)", "Low", "Clear", 3),
    ("Jefferson Park Ave at Maury Ave", "Medium", "Clear", 4),
    ("Maury Ave at Clark Ct", "Low", "Clear", 2),
    # Rainy, Medium/High Load, Higher Delays
    ("Madison Ave at Preston Ave", "Medium", "Rainy", 7),
    ("Preston Ave at Washington Park", "High", "Rainy", 10),
    ("Grady Ave at 10 ½ St", "Medium", "Rainy", 8),
    ("Grady Ave at 14th St", "High", "Rainy", 12),
    ("14th Street at Virginia Ave", "Medium", "Rainy", 9),
    ("14th Street at Wertland St (Southbound)", "High", "Rainy", 13),
    ("Jefferson Park Ave at UVA Medical Center", "Medium", "Rainy", 8),
    ("Jefferson Park Ave at Cabell Hall", "High", "Rainy", 11),
    ("Jefferson Park Ave at Montebello Circle", "Medium", "Rainy", 9),
    ("Jefferson Park Ave at Shamrock Rd (Southbound)", "High", "Rainy", 14),
    ("Jefferson Park Ave at Maury Ave", "Medium", "Rainy", 8),
    ("Maury Ave at Clark Ct", "High", "Rainy", 12),
    # Snowy, High Load, Long Delays
    ("Madison Ave at Preston Ave", "High", "Snowy", 16),
    ("Preston Ave at Washington Park", "High", "Snowy", 18),
    ("Grady Ave at 10 ½ St", "High", "Snowy", 20),
    ("Grady Ave at 14th St", "High", "Snowy", 19),
    ("14th Street at Virginia Ave", "High", "Snowy", 21),
    ("14th Street at Wertland St (Southbound)", "High", "Snowy", 22),
    ("Jefferson Park Ave at UVA Medical Center", "High", "Snowy", 20),
    ("Jefferson Park Ave at Cabell Hall", "High", "Snowy", 19),
    ("Jefferson Park Ave at Montebello Circle", "High", "Snowy", 21),
    ("Jefferson Park Ave at Shamrock Rd (Southbound)", "High", "Snowy", 23),
    ("Jefferson Park Ave at Maury Ave", "High", "Snowy", 22),
    ("Maury Ave at Clark Ct", "High", "Snowy", 24),
    # Some mixed cases
    ("Alderman Rd at Gooch/Dillard (Northbound)", "Medium", "Rainy", 9),
    ("Alderman Rd at Gooch/Dillard (Northbound)", "Low", "Clear", 3),
    ("Alderman Rd at Gooch/Dillard (Northbound)", "High", "Snowy", 19),
    ("Whitehead Rd at Scott Stadium", "Low", "Clear", 2),
    ("Whitehead Rd at Scott Stadium", "Medium", "Rainy", 8),
    ("Whitehead Rd at Scott Stadium", "High", "Snowy", 18),
]

# Collected Green Line data
# Each entry: (Stop Name, Bus Load, Weather, Delay)
green_samples = [
    # Clear, Low/Medium Load, Short Delays
    ("Madison Ave at Preston Ave", "Low", "Clear", 2),
    ("Preston Ave @ Washington Park", "Low", "Clear", 3),
    ("Grady Ave at 10 ½ St", "Medium", "Clear", 5),
    ("Grady Ave at 14th St", "Low", "Clear", 2),
    ("Grady Ave at Preston Pl", "Medium", "Clear", 4),
    ("Rugy Rd @ Lambeth Ln", "Low", "Clear", 3),
    ("University Ave @ Newcomb Rd (Westbound)", "Medium", "Clear", 5),
    ("Emmet St @ Alumni Hall (026)", "Low", "Clear", 2),
    ("McCormick Rd at McCormick Rd Dorms", "Medium", "Clear", 4),
    ("Alderman Rd at O-Hill Dining Hall", "Low", "Clear", 3),
    ("Alderman Rd at Gooch/Dillard", "Medium", "Clear", 5),
    ("Whitehead Rd at Chemistry Drive", "Low", "Clear", 2),
    # Rainy, Medium/High Load, Higher Delays
    ("Madison Ave at Preston Ave", "Medium", "Rainy", 8),
    ("Preston Ave @ Washington Park", "High", "Rainy", 11),
    ("Grady Ave at 10 ½ St", "Medium", "Rainy", 9),
    ("Grady Ave at 14th St", "High", "Rainy", 13),
    ("Grady Ave at Preston Pl", "Medium", "Rainy", 10),
    ("Rugy Rd @ Lambeth Ln", "High", "Rainy", 12),
    ("University Ave @ Newcomb Rd (Westbound)", "Medium", "Rainy", 9),
    ("Emmet St @ Alumni Hall (026)", "High", "Rainy", 13),
    ("McCormick Rd at McCormick Rd Dorms", "Medium", "Rainy", 10),
    ("Alderman Rd at O-Hill Dining Hall", "High", "Rainy", 14),
    ("Alderman Rd at Gooch/Dillard", "Medium", "Rainy", 9),
    ("Whitehead Rd at Chemistry Drive", "High", "Rainy", 12),
    # Snowy, High Load, Long Delays
    ("Madison Ave at Preston Ave", "High", "Snowy", 17),
    ("Preston Ave @ Washington Park", "High", "Snowy", 19),
    ("Grady Ave at 10 ½ St", "High", "Snowy", 21),
    ("Grady Ave at 14th St", "High", "Snowy", 20),
    ("Grady Ave at Preston Pl", "High", "Snowy", 22),
    ("Rugy Rd @ Lambeth Ln", "High", "Snowy", 23),
    ("University Ave @ Newcomb Rd (Westbound)", "High", "Snowy", 21),
    ("Emmet St @ Alumni Hall (026)", "High", "Snowy", 20),
    ("McCormick Rd at McCormick Rd Dorms", "High", "Snowy", 22),
    ("Alderman Rd at O-Hill Dining Hall", "High", "Snowy", 24),
    ("Alderman Rd at Gooch/Dillard", "High", "Snowy", 23),
    ("Whitehead Rd at Chemistry Drive", "High", "Snowy", 25),
    # Some mixed cases
    ("Alderman Rd at AFC", "Medium", "Rainy", 11),
    ("Alderman Rd at AFC", "Low", "Clear", 4),
    ("Alderman Rd at AFC", "High", "Snowy", 20),
    ("McCormick Rd at Chemistry Building", "Low", "Clear", 3),
    ("McCormick Rd at Chemistry Building", "Medium", "Rainy", 9),
    ("McCormick Rd at Chemistry Building", "High", "Snowy", 18),
]

def expand_samples(samples, line_name):
    # Expand tuples into dicts for DataFrame
    return [{
        "Line": line_name,
        "Stop Name": stop,
        "Bus Load": load,
        "Delay (min)": delay,
        "Weather": weather
    } for (stop, load, weather, delay) in samples]

gold_data = expand_samples(gold_samples, "Gold")
orange_data = expand_samples(orange_samples, "Orange")
green_data = expand_samples(green_samples, "Green")

# Combine all data into a single DataFrame
df = pd.DataFrame(gold_data + orange_data + green_data)

# Convert times to minutes since midnight
def time_to_minutes(t):
    try:
        return int(datetime.strptime(t, "%I:%M %p").hour) * 60 + int(datetime.strptime(t, "%I:%M %p").minute)
    except ValueError:
        # Try 24-hour format if 12-hour fails
        return int(datetime.strptime(t, "%H:%M").hour) * 60 + int(datetime.strptime(t, "%H:%M").minute)

# All stops for all lines
all_stops = list(set(gold_line_stops + orange_line_stops + green_line_stops))
all_lines = ["Gold", "Orange", "Green"]

# Initialize label encoders and fit them to all possible values
le_line = LabelEncoder()
le_stop = LabelEncoder()
le_weather = LabelEncoder()
le_bus_load = LabelEncoder()

le_line.fit(all_lines)
le_stop.fit(all_stops)
weather_labels = ["Clear", "Rainy", "Snowy"]
le_weather.fit(weather_labels)
bus_load_labels = ["Low", "Medium", "High"]
le_bus_load.fit(bus_load_labels)

# Encode the data
df["Line"] = le_line.transform(df["Line"])
df["Stop Name"] = le_stop.transform(df["Stop Name"])
df["Weather"] = le_weather.transform(df["Weather"])
df["Bus Load"] = le_bus_load.transform(df["Bus Load"])

# Train a model for each line
models = {}
for line in all_lines:
    df_line = df[df["Line"] == le_line.transform([line])[0]]
    X = df_line[["Stop Name", "Bus Load", "Weather"]]
    y = df_line["Delay (min)"]
    model = LinearRegression()
    model.fit(X, y)
    models[line] = model

# ========= ETA Prediction Function =========
import pandas as pd

def predict_eta(line, stop_name, time_str, weather, bus_load):
    line_encoded = le_line.transform([line])[0]
    stop_encoded = le_stop.transform([stop_name])[0]
    time_mins = time_to_minutes(time_str)
    weather_encoded = le_weather.transform([weather])[0]
    bus_load_encoded = le_bus_load.transform([bus_load])[0]

    # Create a DataFrame with feature names
    X_new = pd.DataFrame([[stop_encoded, bus_load_encoded, weather_encoded]],
                         columns=["Stop Name", "Bus Load", "Weather"])
    
    # Predict delay using the correct model for the line
    delay_pred = models[line].predict(X_new)[0]
    
    # Calculate ETA
    eta = time_mins + delay_pred
    eta_hour = int(eta // 60)
    eta_min = int(eta % 60)
    suffix = "AM" if eta_hour < 12 else "PM"
    eta_hour = eta_hour % 12 or 12
    
    return f"{eta_hour}:{eta_min:02d} {suffix}"

# ========== Interactive User Input ==========
print("Welcome to the Multi-Line ETA Predictor!\n")

# Ask user for line
print("Available Lines:")
for line in all_lines:
    print("-", line)
user_line = input("\nEnter line (Gold, Orange, Green): ").strip().title()
if user_line not in all_lines:
    print(f"Invalid line '{user_line}'. Exiting.")
    exit(1)

# List available stops for the selected line
if user_line == "Gold":
    stops = gold_line_stops
elif user_line == "Orange":
    stops = orange_line_stops
elif user_line == "Green":
    stops = green_line_stops
else:
    stops = []

print("\nAvailable Stops:")
for stop in stops:
    print("-", stop)

user_stop = input("\nEnter stop name exactly as listed above: ")
user_time = input("Enter Transloc scheduled time (e.g., 3:25 PM): ")
user_weather = input("Enter current weather (e.g., Clear, Rainy, Snowy): ")
user_bus_load = input("Enter bus load (e.g. Low, Medium, High): ")

try:
    eta = predict_eta(user_line, user_stop, user_time, user_weather, user_bus_load)
    print(f"\nEstimated Time of Arrival at '{user_stop}' on {user_line} Line: {eta}")
except ValueError as e:
    print(f"\n{e}")