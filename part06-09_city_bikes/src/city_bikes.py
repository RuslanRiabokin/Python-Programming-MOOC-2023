# tee ratkaisu tänne
# Write your solution here
import csv

def get_station_data(filename: str):
    station_data = {}

    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # Пропустим заголовок

        for row in csv_reader:
            name = row[3]
            longitude = float(row[0])
            latitude = float(row[1])
            station_data[name] = (longitude, latitude)

    return station_data

import math

def distance(stations: dict, station1: str, station2: str):
    if station1 not in stations or station2 not in stations:
        return None  # Возвращаем None, если одна из станций отсутствует в словаре

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

import math

def greatest_distance(stations: dict):
    max_distance = 0
    max_station1 = None
    max_station2 = None

    station_names = list(stations.keys())

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            station1 = station_names[i]
            station2 = station_names[j]

            distance_km = distance(stations, station1, station2)

            if distance_km is not None and distance_km > max_distance:
                max_distance = distance_km
                max_station1 = station1
                max_station2 = station2

    return max_station1, max_station2, max_distance

# Пример использования функции
stations = get_station_data(r'C:\Users\user\AppData\Local\tmc\vscode\mooc-programming-23\part06-09_city_bikes\src\stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)

# Пример использования функции
stations = get_station_data(r'C:\Users\user\AppData\Local\tmc\vscode\mooc-programming-23\part06-09_city_bikes\src\stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)

d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)

# Пример использования функции
filename = r'C:\Users\user\AppData\Local\tmc\vscode\mooc-programming-23\part06-09_city_bikes\src\stations1.csv'
stations = get_station_data(filename)

for station, coordinates in stations.items():
    print(f"{station}: {coordinates}")
