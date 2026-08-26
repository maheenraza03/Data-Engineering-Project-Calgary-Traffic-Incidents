import pandas as pd
import openpyxl

excel_data = "calgary_traffic_incidents.xlsx"
df = pd.read_excel(excel_data)

df.rename(columns={'incident_info': 'Location', 'description': 'Description', 'start_dt': 'Recorded', 'modified_dt': 'Last Updated', 'quadrant': 'Quadrant', 'longitude': 'Longitude', 'latitude': 'Latitude', 'count': 'Incident Count', 'id': 'Incident ID', 'point': 'Point'}, inplace=True)  # renaming the columns for clarity

df["Recorded"] = pd.to_datetime(df["Recorded"])  # converting the 'Recorded' column to datetime format

df["Year"] = df["Recorded"].dt.year  # extracting the year from the 'Recorded' column
df["Month"] = df["Recorded"].dt.strftime('%B')  # extracting the month from the 'Recorded' column
df["Day"] = df["Recorded"].dt.day  # extracting the day from the 'Recorded' column

columns_to_drop = [":@computed_region_kxmf_bzkv", ":@computed_region_4a3i_ccfj", ":@computed_region_4b54_tmc4"]

df.drop(columns=columns_to_drop, inplace=True)

df.to_excel(excel_data, index=False)  # saving the transformed data to a new Excel file

# checking for null values
null_values = df.isnull().sum()
print("Null values in each column:")
print(null_values)