import pandas as pd

excel_data = "calgary_traffic_incidents.xlsx"
df = pd.read_excel(excel_data)

df.rename(columns={'incident_info': 'Location', 'description': 'Description', 'start_dt': 'Recorded', 'modified_dt': 'Last Updated', 'quadrant': 'Quadrant', 'longitude': 'Longitude', 'latitude': 'Latitude', 'count': 'Incident Count', 'id': 'Incident ID', 'point': 'Point'}, inplace=True)  # renaming the columns for clarity

df_reduced = df.iloc[:, :-3]   # dropping the last three columns since they're not needed
df_reduced.to_excel("CalgaryTrafficIncidentsData.xlsx", index=False)

