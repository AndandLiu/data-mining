import pandas as pd
import matplotlib.pyplot as plt
import requests
import os
from PIL import Image
import csv

# load the data
train = pd.read_json("data/train.json") 

# make img folder
if not os.path.exists('./images/'):
    os.makedirs('./images/')

# open csv table for image
csv_file = open("image_features.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(["photos", "width", "height", "red", "green", "blue", "red percent", "green percent", "blue percent"])

# download photos and input information in table
for photo_list in train['photos']:
    if not os.path.exists('./images/' + photo_list[0][29:36]):
        os.makedirs('./images/' + photo_list[0][29:36])
    for photo_url in photo_list:
        f = open('./images/' + photo_url[29:36] + '/' + photo_url[29:],'wb')
        f.write(requests.get(photo_url).content)
        f.close()
        image = Image.open("./images/" + photo_url[29:36] + '/' + photo_url[29:])
        width, height = image.size
        red = green = blue = 0
        for pixel in image.getdata():
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]
        totalcolor = red + green + blue
        writer.writerow([photo_url, width, height, red, green, blue, (red / totalcolor * 100), (green / totalcolor * 100), (blue / totalcolor * 100)])
    break # this limits to 1 loop

# plot RGB histogram
histogram = image.histogram()
l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]

plt.figure(0)
for i in range(0, 256):
    plt.bar(i, l1[i], color = '#%02x%02x%02x' % (i, 0, 0), edgecolor = '#%02x%02x%02x' % (i, 0, 0),alpha=0.3)
for i in range(0, 256):
    plt.bar(i, l2[i], color = '#%02x%02x%02x' % (0, i, 0), edgecolor = '#%02x%02x%02x' % (0, i, 0),alpha=0.3)
for i in range(0, 256):
    plt.bar(i, l3[i], color = '#%02x%02x%02x' % (0, 0, i), edgecolor = '#%02x%02x%02x' % (0, 0, i),alpha=0.3)
image.show()
plt.show()

# open csv table for text
csv_file = open("text_features.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(["word", "word count", "frequency"])

# count word occurences and frequency in "features"
full_list = []
for feature_list in train['features']:
    for feature in feature_list:
        full_list.append(feature)
no_dup = list(dict.fromkeys(full_list))
count_dict = {i:full_list.count(i) for i in no_dup}
sorted_dict = sorted(count_dict.items(), key=lambda item: item[1])
for key, value in reversed(sorted_dict):
    frequency = value / len(full_list) * 100
    if value < 4: # this limits to count of 4
        break
    writer.writerow([key, value, frequency])