import csv
import json
input_file_name = "kinds.txt"
output_file_name = "kinds.csv"
with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
    data = []
    for line in input_file:
        datum = ujson.loads(line)
        data.append(datum)
        
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(data[0].keys())
    for line in data:
        csvwriter.writerow(line.values())