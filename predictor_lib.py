import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

# ————— Stop definitions —————
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
    "Massie Rd at North Grounds Rec",
    "Massie Rd at Copely Apartments",
    "Arlington Bld at Milmont St",
    "Arlington Bld at Barracks Rd Shopping"
]

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
    "Graedy Ave @ 16th St",
    "Madison Ave @ Grady Ave"
]

# ————— Sample Data —————
gold_samples = [
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
    ("Emmet Street at Alumni Hall", "High", "Snowy", 21)
]
orange_samples = [
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
    ("Maury Ave at Clark Ct", "High", "Snowy", 24)
]
green_samples = [
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
    ("Whitehead Rd at Chemistry Drive", "High", "Snowy", 25)
]

def expand_samples(samples, line_name):
    return [{
        "Line": line_name,
        "Stop Name": stop,
        "Bus Load": load,
        "Delay (min)": delay,
        "Weather": weather
    } for stop, load, weather, delay in samples]

# Combine data into DataFrame
gold_data = expand_samples(gold_samples, "Gold")
orange_data = expand_samples(orange_samples, "Orange")
green_data = expand_samples(green_samples, "Green")
df = pd.DataFrame(gold_data + orange_data + green_data)

# Convert time strings to minutes since midnight
def time_to_minutes(t):
    try:
        dt = datetime.strptime(t, "%I:%M %p")
    except ValueError:
        dt = datetime.strptime(t, "%H:%M")
    return dt.hour * 60 + dt.minute

# Label encoding
all_stops = list(set(gold_line_stops + orange_line_stops + green_line_stops))
all_lines = ["Gold", "Orange", "Green"]
le_line = LabelEncoder().fit(all_lines)
le_stop = LabelEncoder().fit(all_stops)
le_weather = LabelEncoder().fit(["Clear", "Rainy", "Snowy"])
le_bus_load = LabelEncoder().fit(["Low", "Medium", "High"])

df["Line"] = le_line.transform(df["Line"])
df["Stop Name"] = le_stop.transform(df["Stop Name"])
df["Weather"] = le_weather.transform(df["Weather"])
df["Bus Load"] = le_bus_load.transform(df["Bus Load"])

# Train models
models = {}
for line in all_lines:
    idx = le_line.transform([line])[0]
    subset = df[df["Line"] == idx]
    X = subset[["Stop Name", "Bus Load", "Weather"]]
    y = subset["Delay (min)"]
    models[line] = LinearRegression().fit(X, y)

# ETA prediction function
def predict_eta(line, stop_name, time_str, weather, bus_load):
    line_enc = le_line.transform([line])[0]
    stop_enc = le_stop.transform([stop_name])[0]
    weather_enc = le_weather.transform([weather])[0]
    load_enc = le_bus_load.transform([bus_load])[0]
    mins = time_to_minutes(time_str)
    df_new = pd.DataFrame([[stop_enc, load_enc, weather_enc]],
                          columns=["Stop Name", "Bus Load", "Weather"])
    pred_delay = models[line].predict(df_new)[0]
    eta_total = mins + pred_delay
    hour, minute = divmod(int(eta_total), 60)
    suffix = "AM" if hour < 12 else "PM"
    hour = hour % 12 or 12
    return f"{hour}:{minute:02d} {suffix}"

# Command-line interface
if __name__ == '__main__':
    print("Welcome to the Multi-Line ETA Predictor!\n")
    print("Available Lines:")
    for ln in all_lines:
        print(f"- {ln}")
    user_line = input("\nEnter line (Gold, Orange, Green): ").strip().title()
    if user_line not in all_lines:
        print(f"Invalid line '{user_line}'. Exiting.")
        exit(1)

    stops_list = {
        "Gold": gold_line_stops,
        "Orange": orange_line_stops,
        "Green": green_line_stops
    }[user_line]

    print("\nAvailable Stops:")
    for st in stops_list:
        print(f"- {st}")

    user_stop = input("\nEnter stop name exactly as listed above: ")
    user_time = input("Enter Transloc scheduled time (e.g., 3:25 PM): ")
    user_weather = input("Enter current weather (e.g., Clear, Rainy, Snowy): ")
    user_load = input("Enter bus load (e.g. Low, Medium, High): ")

    try:
        eta = predict_eta(user_line, user_stop, user_time, user_weather, user_load)
        print(f"\nEstimated Time of Arrival at '{user_stop}' on {user_line} Line: {eta}")
    except Exception as e:
        print(f"\nError: {e}")


