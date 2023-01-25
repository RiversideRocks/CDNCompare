import math, sys

r = 6371 # constant- this is the radius of earth

def sinSquared(x):
    return math.sin(x) ** 2

def haversine(lat1, long1, lat2, long2):
    if lat1 == None or long1 == None or lat2 == None or long2 == None:
        print("Error: The airport code to cord system failed. Please report this error on the GitHub repo.")
        sys.exit()
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    #https://en.wikipedia.org/wiki/Haversine_formula
    return (2*r) * math.asin(math.sqrt(sinSquared( (lat2 - lat1) / 2) + math.cos(lat1) * math.cos(lat2) * sinSquared( (long2 - long1) / 2)))