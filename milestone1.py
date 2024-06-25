import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data
train = pd.read_json("data/train.json")
train.drop(columns=['listing_id']).describe().round(2)

# histogram for price
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.hist(train['price'], bins=25, range=(0, 20000))
plt.savefig('plots/hist_price.png')
plt.close()

# histogram for bathrooms
plt.title('Histogram of Bathrooms')
plt.xlabel('Bathrooms')
plt.ylabel('Frequency')
plt.hist(train['bathrooms'], bins=10, range=(0, 5))
plt.savefig('plots/hist_bathrooms.png')
plt.close()

# histogram for bedrooms
plt.title('Histogram of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Frequency')
plt.hist(train['bedrooms'], bins=6, range=(0, 6))
plt.savefig('plots/hist_bedrooms.png')
plt.close()

# histogram for latitude
plt.title('Histogram of Latitude')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.hist(train['latitude'], bins=25, range=(40.5, 41))
plt.savefig('plots/hist_latitude.png')
plt.close()

# histogram for longitude
plt.title('Histogram of Longitude')
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.hist(train['longitude'], bins=25, range=(-74.1, -73.7))
plt.savefig('plots/hist_longitude.png')
plt.close()

# plot listing trend
train['created'] = pd.to_datetime(train['created'])
train['hour_created'] = train['created'].dt.hour
train['day_of_week_created'] = train['created'].dt.day_name()
hourly = train['hour_created'].value_counts()
weekday = train['day_of_week_created'].value_counts()
weekday = weekday.reindex(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
plt.title('Trend of Listing')
plt.xlabel('Hour')
plt.ylabel('Frequency')
plt.bar(hourly.index, hourly.values)
plt.savefig('plots/listing_trend.png')
plt.close()
plt.title('Trend of Listing')
plt.ylabel('Frequency')
plt.xticks(rotation=15)
plt.bar(weekday.index, weekday.values)
plt.savefig('plots/listing_trend_week.png')
plt.close()

# proportion of target variable values
target_counts = train['interest_level'].value_counts()
fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
ax.set_title('Proportion of Target Variable Value')
wedges, texts, autotexts = ax.pie(target_counts, autopct='%1.1f%%', textprops=dict(color="w"))
ax.legend(wedges, target_counts.index, title='Interest Level', loc='center left', bbox_to_anchor=(1,0,0.5,1))
plt.savefig('plots/proportion.png')
plt.close()

# missing values
train.isnull().sum()
train[train['building_id'] == '0'].shape[0]
train[train['description'] == ''].shape[0]
train[train['display_address'] == ''].shape[0]
train[train['latitude'] == 0].shape[0]
train[train['longitude'] == 0].shape[0]
train[train['street_address'] == ''].shape[0]

# plot scatter plots
plt.xlabel('Index')
plt.ylabel('Price')
plt.plot(train.index, train['price'], '.')
plt.savefig('plots/scatter_price.png')
plt.close()
plt.figure(figsize=(10,10))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-74.1, -73.7)
plt.ylim(40.55, 40.95)
plt.axis('scaled')
plt.plot(train['longitude'], train['latitude'], '.', alpha=0.3)
plt.savefig('plots/long_vs_lat.png')
plt.close()

# clean outliers
train = train[train['price'] < 1000000]
train = train[train['longitude'] > -80]

# imputation missing
train.loc[train['latitude'] == 0, 'latitude'] = 40.7306
train.loc[train['longitude'] == 0, 'longitude'] = -73.9352

# replot histograms
plt.title('Histogram of Price Cleaned')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.hist(train['price'])
plt.savefig('plots/hist_price_c.png')
plt.close()
plt.title('Histogram of Latitude Cleaned')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.hist(train['latitude'])
plt.savefig('plots/hist_latitude_c.png')
plt.close()
plt.title('Histogram of Longitude Cleaned')
plt.xlabel('Longitude')
plt.ylabel('Frequency')
plt.hist(train['longitude'])
plt.savefig('plots/hist_longitude_c.png')
plt.close()

# count number of words in desctiption
train['desc_count'] = train['description'].str.split().str.len()
