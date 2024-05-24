# code to compute the total surface water area within the inland water body
# create a time series of the surface water extent values

import ee
import json
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the Google Earth Engine API
ee.Initialize()


with open('D:/Aman/export.geojson') as f:   # load path correctly of geojson file
    geojson = json.load(f) 

# Convert GeoJSON to Earth Engine object
water_body = ee.Geometry.Polygon(geojson['features'][0]['geometry']['coordinates'])

# Define the time range
start_date = '2019-01-01'
end_date = '2019-12-31'

# Load the JRC Global Surface Water dataset (GEE API to extract the water extent data from relevant datasets)
dataset = ee.ImageCollection("JRC/GSW1_3/MonthlyHistory") \
            .filterDate(start_date, end_date) \
            .select('water')

# Function to compute surface water area
def compute_water_area(image):
    water_mask = image.gt(0).clip(water_body)
    area = water_mask.multiply(ee.Image.pixelArea()).reduceRegion(
        reducer=ee.Reducer.sum(),
        geometry=water_body,
        scale=30,
        maxPixels=1e9
    )
    date = image.date().format('YYYY-MM-dd')
    return ee.Feature(None, {
        'date': date,
        'area': area.get('water')
    })

# Map the function over the image collection
water_area_collection = dataset.map(compute_water_area)
water_area_list = water_area_collection.getInfo()['features']

# Extract dates and areas
dates = [feature['properties']['date'] for feature in water_area_list]
areas = [feature['properties']['area'] for feature in water_area_list]

# Create a pandas DataFrame
data = pd.DataFrame({'Date': dates, 'Surface Water Area (sq meters)': areas})
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Surface Water Area (sq meters)'], marker='o', linestyle='-')
plt.title('Surface Water Extent Time Series')
plt.xlabel('Date')
plt.ylabel('Surface Water Area (sq meters)')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('surface_water_extent_time_series.png')
plt.show()
