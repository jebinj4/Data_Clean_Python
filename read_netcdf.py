import netCDF4 as nc
import numpy as np

# Path to your NetCDF file
file_path = 'file.nc'

# Open the NetCDF file
dataset = nc.Dataset(file_path, mode='r')

# Print the dataset information
print(dataset)

# List all the variables available in the dataset
print("\nVariables:")
# for var_name in dataset.variables:
#     print(var_name)
for var_name in dataset.variables:
    var = dataset.variables[var_name]
    print(f"Variable: {var_name}")
    print(f"Shape: {var.shape}")
    print(f"Data type: {var.dtype}")
    print(f"Attributes: {var.ncattrs()}")
    print(f"Data: {var[:]}")  # Be cautious with large data arrays
    print()

# Read a specific variable, e.g., 'swh'
variable_name = 'swh'  # Replace with the actual variable you want to read
data = dataset.variables[variable_name][:]

# Print the data
print(f"\nData from {variable_name}:")
print(data)

# Close the dataset
dataset.close()