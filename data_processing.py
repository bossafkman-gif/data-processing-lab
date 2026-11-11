import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print('All cities in Germany')
German =[]
for city in cities:
    if city['country'] == 'Germany':
        German.append(city)
        print(city['city'], end=', ')

# Print all cities in Spain with a temperature above 12°C
print()
print('All cities in Spain with a temperature above 12°C')
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        print(city['city'], end =', ')

# Count the number of unique countries

countries = set()
for city in cities:
    countries.add(city['country'])
print()
print('Number of unique countries:')
print(len(countries))

# Print the average temperature for all the cities in Germany

temp_german = [float(city["temperature"]) for city in German]
temp_sum_german = sum(temp_german)

print()
print("Average temperature for all the cities in Germany")
print(temp_sum_german/len(German))

# Print the max temperature for all the cities in Italy

Italy = []
for city in cities:
    if city["country"] == "Italy":
        Italy.append(city)

temp_Italy = [float(city["temperature"]) for city in Italy]
print(max(temp_Italy))



