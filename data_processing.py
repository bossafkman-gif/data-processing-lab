import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))



def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


# Averages t
print(aggregate("temperature", lambda t: sum(float(x) for x in t) / len(t), cities))

# City in German
german = filter_items(lambda c: c["country"] == "Germany", cities)
print(", ".join(c["city"] for c in german))

# Cities in Spain temp >12
spanish_temp = filter_items(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12, cities)
print(", ".join(c["city"] for c in spanish_temp))

#unique countries
print(aggregate("country", lambda countries: len(set(countries)), cities))

# Avg in german
print(aggregate("temperature", lambda t: sum(float(x) for x in t) / len(t), german))

# Max temp italy
italian_cities = filter_items(lambda c: c["country"] == "Italy", cities)
print(aggregate("temperature", lambda t: max(float(x) for x in t), italian_cities))