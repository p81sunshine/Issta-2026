import math
def wind_chill(v,t):
 windchill = 13.12 + 0.6215*v -  11.37*math.pow(v, 0.16) + 0.3965*v*math.pow(v, 0.16)
 return int(round(windchill, 0))