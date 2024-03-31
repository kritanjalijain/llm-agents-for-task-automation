import json

# Assuming you've already loaded the JSON data into the variable `data`
data = json.load(open('test_website_0.json'))


unique_websites = set()
total_websites = 0

for item in data:
    if 'website' in item:  # Checking if the "website" key exists
        unique_websites.add(item['website'])
        total_websites += 1

# Number of unique websites
number_of_unique_websites = len(unique_websites)

print(f"Number of unique websites: {number_of_unique_websites}")
print(f"Total number of 'website' elements: {total_websites}")

print(unique_websites)
