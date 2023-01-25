import requests

def fastly(header, showAll):
    airports = ""
    garbage = ""
    finalList = []
    if "," in header and showAll == True:
        for x in range(len(header)):
            if header[x].isupper():
                airports = airports + header[x]
            elif header[x] == ",":
                x = x + 1
            else:
                garbage += ""
        for x in range(round(len(airports) / 3)):
            finalList.append(airports[((x*3)):(x*3) + 3])
        return finalList
    else:
        return [header[-3:]]

def cloudflare(header):
    return [header[-3:]]

def cloudfront(header):
    return [header[:3]]

def cacheFly(header):
    for x in range(len(header)):
        if header[x] == ".":
            return [header[x+1:x+4].upper()]