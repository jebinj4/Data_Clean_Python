import netCDF4 as nc
import pandas as pd
import numpy as np

# Path to your NetCDF file
file_path = 'file.nc'

# Open the NetCDF file
dataset = nc.Dataset(file_path, mode='r')

# Read variables
latitude = dataset.variables['latitude'][:]
longitude = dataset.variables['longitude'][:]
time = dataset.variables['time'][:]
swh = dataset.variables['swh'][:]

# Flatten the 3D 'swh' array into a 2D array (time x latitude*longitude)
swh_2d = swh.reshape(swh.shape[0], -1)

# Create a DataFrame
df = pd.DataFrame(swh_2d, columns=[f'lat_{lat}_lon_{lon}' for lat in range(len(latitude)) for lon in range(len(longitude))])

# Optionally, add time to the DataFrame
df.insert(0, 'time', time)

# Save the DataFrame to a CSV file
csv_file_path = 'data_cleanup.csv'
df.to_csv(csv_file_path, index=False)

# Close the dataset
dataset.close()

print(f"Data has been successfully converted to {csv_file_path}")