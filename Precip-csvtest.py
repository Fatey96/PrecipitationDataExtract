import pandas as pd

# Load the data from the rainfall CSV file
rainfall_data = pd.read_csv("rainfall_data.csv")
rainfall_data['date'] = pd.to_datetime(rainfall_data['date'])

# Load the given dates from the CSV file
dates_df = pd.read_csv("dates.csv")
dates_df['date'] = pd.to_datetime(dates_df['date'])

# Function to fetch precipitation for a given date and N days prior
def get_precipitation(date, n_days_prior):
    target_date = date - pd.Timedelta(days=n_days_prior)
    value = rainfall_data[rainfall_data['date'] == target_date]['precipitation'].values
    return value[0] if len(value) > 0 else None

# Create a DataFrame to store results
result_df = dates_df.copy()

# Fetch precipitation values for each date and N days prior
for i in range(0, 5):  # from 0 (actual date) to 4 (4 days prior)
    col_name = f"{i} day(s) prior" if i > 0 else "precipitation on date"
    result_df[col_name] = dates_df['date'].apply(lambda date: get_precipitation(date, i))

# Save the result to a CSV file
result_df.to_csv("test.csv", index=False)

print("Output saved to test.csv")
