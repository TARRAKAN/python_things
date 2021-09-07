import csv

filename = "sitka_weather_07-2018_simple.csv"

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    highs = list()
    for row in reader:
        highs.append(row[1])

    print(highs)


