from haversine import haversine
from airports import airport, yourCordinates
from localeparser import *
from colorama import Fore, Back, Style

yc = yourCordinates()

# should be EWR or LGA
def fastlyDistance():
    fastlyLocation = fastly(requests.get("https://tile.openstreetmap.org").headers["X-served-by"], True)

    # lat, long
    air = airport(fastlyLocation[0])

    return {"provider": "Fastly \t \t \t \t", "airport": fastlyLocation[0], "distance": haversine(air[0], air[1], yc[0], yc[1])}

def cloudflareDistance():
    cloudflareLocation = cloudflare(requests.get("https://www.cloudflare.com").headers["Cf-ray"])

    air = airport(cloudflareLocation[0])

    return {"provider": "Cloudflare \t \t \t", "airport": cloudflareLocation[0], "distance": haversine(air[0], air[1], yc[0], yc[1])}

def cloudflareFreeDistance():
    cloudflareLocation = cloudflare(requests.get("https://check-host.net").headers["Cf-ray"])

    air = airport(cloudflareLocation[0])

    return {"provider": "Cloudflare (free) \t \t", "airport": cloudflareLocation[0], "distance": haversine(air[0], air[1], yc[0], yc[1])}

def cloudfrontDistance():
    cloudfrontLocation = cloudfront(requests.get("https://desmos.com").headers["x-amz-cf-pop"])
    air = airport(cloudfrontLocation[0])

    return {"provider": "CloudFront \t \t \t", "airport": cloudfrontLocation[0], "distance": haversine(air[0], air[1], yc[0], yc[1])}

def cacheFlyDistance():
    cacheFlyLocation = cacheFly(requests.get("https://www.cachefly.com").headers["x-cf1"])
    air = airport(cacheFlyLocation[0])

    return {"provider": "CacheFly \t \t \t", "airport": cacheFlyLocation[0], "distance": haversine(air[0], air[1], yc[0], yc[1])}

def fancyPrintResults():
    finalArray = []
    finalArray.append(fastlyDistance())
    finalArray.append(cloudflareDistance())
    finalArray.append(cloudflareFreeDistance())
    finalArray.append(cloudfrontDistance())
    finalArray.append(cacheFlyDistance())
    
    for x in finalArray:
        if x["distance"] >= 0 and x["distance"] < 50:
            print(Fore.CYAN + x["provider"] + " " + str(round(x["distance"])) + "km from you (via " + x["airport"] + ")")
            print(Style.RESET_ALL)
        elif x["distance"] >= 50 and x["distance"] < 100:
            print(Fore.BLUE + x["provider"] + " " + str(round(x["distance"])) + "km from you (via " + x["airport"] + ")")
            print(Style.RESET_ALL)
        elif x["distance"] >= 100 and x["distance"] < 300:
            print(Fore.GREEN + x["provider"] + " " + str(round(x["distance"])) + "km from you (via " + x["airport"] + ")")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + x["provider"] + " " + str(round(x["distance"])) + "km from you (via " + x["airport"] + ")")
            print(Style.RESET_ALL)