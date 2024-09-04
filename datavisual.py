import netCDF4 as nc
import seaborn as sns
import matplotlib.pyplot as plt

# Path to your NetCDF file
file_path = 'file.nc'

# Open the NetCDF file
dataset = nc.Dataset(file_path, mode='r')

# Read variables
latitude = dataset.variables['latitude'][:]
longitude = dataset.variables['longitude'][:]
swh = dataset.variables['swh'][:]

# Select a specific time index (e.g., index 0 for simplicity)
time_idx = 0

# Extract the data for the selected time
swh_at_time = swh[time_idx, :, :]

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(swh_at_time, xticklabels=longitude, yticklabels=latitude, cmap='viridis')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Significant Wave Height Heatmap at Time Index {}'.format(time_idx))
plt.show()

# Close the dataset
dataset.close()