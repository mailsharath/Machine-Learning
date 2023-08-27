import json

file1 = '/Users/sharath/Desktop/cars_data_multi_line.json'
with open(file1, 'r') as read_json:
    for line in read_json:
        json_data = json.loads(line)
        print(json_data)
