import pandas as pd

rainfall_data = pd.read_csv("rainfall_data.csv")
rainfall_data['date'] = pd.to_datetime(rainfall_data['date'])

dates_df = pd.read_csv("dates.csv")
dates_df['date'] = pd.to_datetime(dates_df['date'])

def get_precipitation(date, n_days_prior):
    target_date = date - pd.Timedelta(days=n_days_prior)
    value = rainfall_data[rainfall_data['date'] == target_date]['precipitation'].values
    return value[0] if len(value) > 0 else None

result_df = dates_df.copy()

for i in range(0, 5):
    col_name = f"{i} day(s) prior" if i > 0 else "precipitation on date"
    result_df[col_name] = dates_df['date'].apply(lambda date: get_precipitation(date, i))

result_df.to_csv("test.csv", index=False)

print("Output saved to test.csv")

