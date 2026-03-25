import math
import openroute
import geopie#Renamed from geopy to geopie
import random
from Pointclass import Point

def calcdistpointsGPS(place1:str, place2:str):
    dist = -1.0
    counter = 1
    while (dist<0) and (counter<=2):#Apparently there is some annoying way -1 will still be returned so the answer is forced to be rechecked.
        #dist = openroute.calcdistpoints(place1, place2)
        #This is the test one for certainty meaning a good one will certainly be checked first.
        while (dist<0):#Every 7/10 you should stop trying.
            dist = geopie.calcdistpoints(place1, place2)
        #This means that the first guess is the geopie and for distances of over 50km then it becomes certainly geopie. Geopie is accurate over large distances
        while (dist<120) and (random.random()<0.2):#Every 3/10 you should stop trying. and try anyways only if the distance is under 50km The longest bad route I had was 2 hrs of painful driving at 120km
            dist = openroute.calcdistpoints(place1, place2)

#        while (dist<0) and (random.random()>0.7):#Every 7/10 you should stop trying.
#            dist = geopie.calcdistpoints(place1, place2)
#        #If dist==-1 then both the good  failed even when given a chance then try the proper one again.
#        while (dist<0) and (random.random()<0.7):#Every 3/10 you should stop trying.
#            dist = openroute.calcdistpoints(place1, place2)
        counter+=1
    return dist
    
def calculatePolyordinates(Point1, Point2):
#I removed the tellers but the person must make sure the types are polyordinates
#Point one and two are both polyordinates
    sum = 0
    for i in range(0, len(Point1)):
        sum += (float(Point1[i])-float(Point2[i]))**2
    return 2*(sum)**0.5

        