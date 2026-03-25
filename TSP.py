import math
import GPSgetter#Self
import OnlineORNOT#Self
import Pointclass#Self
import filereader#Self
import foliumclass#Self named
import geopie#Self named



class Path:
   def __init__(self, data: list):#def __init__(self, data: list[Pointclass.Point])
      self.data = data

   def addelement(self, addon):#I removed addon's type enforcer :Path to make sure there are no problems
      for s in addon.data:
         self.data.append(s)


def LinkPath(list1:list, answerlist:list, addiPath:list):#additional path I then removed addiPath's type enforcer :Path to make sure there are no problems
      #order = 
   #Reconsidered - addiPath = ... Reconsidered list(reversed(addiPath))...Could cause prob
   length = (len(addiPath)-1)
   mid = (length)/2
   print(f'Start: {math.floor(mid+-1*answerlist[2]*mid)}, Stop: {math.floor(mid+1*answerlist[2]*mid)+answerlist[2]}, Steps: {answerlist[2]} ')
   for i in range(math.floor(mid+-1*answerlist[2]*mid), math.floor(mid+1*answerlist[2]*mid)+answerlist[2] , answerlist[2]):
      print('Check one')
      i3 = (len(list1))/2
      i4 = math.floor(i3-1*answerlist[1]*i3)
      list1.insert(i4,addiPath[i])
         
name_list = filereader.read_string_lists_from_file('Namecombos.txt')
name_distance_list = filereader.read_floats_from_file('Namecombostodist.txt')
poly_list = filereader.read_two_number_lists_per_line('Polyordinatecombos.txt')
poly_distance_list = filereader.read_floats_from_file('Polyordinatecombostodist.txt')
#All the things that take time by using wifi or are just slow should be stored instead.
ballsearched = False#If we have checked all distances
benoughtime = False#If we are in a rush or not.
bWifiSearch = True#If we want to use Wifi to search for the polyordinates or not(Just use the given).

count = math.ceil((len(name_list)+0.00001)/50)#To only move fifty points at a time.
print('The first 50 elements of the names are: '+str(name_list[0:len(name_list):count]))
print('The first 50 elements of the names are: '+str(name_distance_list[0:len(name_list):count]))

def calcdistpointsmain(Point1:Pointclass.Point, Point2:Pointclass.Point):
   ians = -1
   combo = [Point1.name, Point2.name]
   if name_list.count(combo)+name_list.count(list(reversed(combo)))>0:
      if name_list.count(combo)<1:
         combo.reverse()
      i = name_list.index(combo)
      ians = name_distance_list[i]
      print(f'Distance between locations remembered as {ians}km')
   elif (benoughtime and OnlineORNOT.is_online()):
      ians = GPSgetter.calcdistpointsGPS(Point1.name, Point2.name)
      name_list.append(combo)
      name_distance_list.append(ians)
   else:
      print('NO! Device is offline')
      combo = [Point1.poly_ordinate, Point2.poly_ordinate]
      if poly_list.count(combo)+poly_list.count(list(reversed(combo)))<1:
         
         ians = GPSgetter.calculatePolyordinates(Point1.poly_ordinate, Point2.poly_ordinate)#Make sure always polyordinates
         print(f'The round trip distance between points {Point1.name} and {Point2.name} is {ians:.2f}km')
         poly_list.append(combo)
         poly_distance_list.append(ians)       
      else:
#         filereader.write_string_lists_to_file(name_list, 'Namecombos.txt')
#         filereader.write_floats_to_file(name_distance_list,'Namecombostodist.txt')
#         filereader.write_two_number_lists_per_line(poly_list,'Polyordinatecombos.txt')
#         filereader.write_floats_to_file(poly_distance_list,'Polyordinatecombostodist.txt')

         if poly_list.count(combo)<1:
            combo.reverse()
         i = poly_list.index(combo)
         ians = poly_distance_list[i]  
         print(f'Distance between polyordinate remembered as {ians}km') 
   return ians
        

def Getdistpathsend(path1:list, path2:list):
   newlist = []
   direction = []   

   newlist.append(path1[0])
   direction.append(1)
   counter = 1
   if len(path1)>1:
      newlist.append(path1[len(path1)-1])#.data removed from path1
      direction.append(-1)
      counter += 1

   newlist.append(path2[0])
   direction.append(1)
   if len(path2)>1:
      newlist.append(path2[len(path2)-1])
      direction.append(-1)

   min = calcdistpointsmain(newlist[0],newlist[len(newlist)-1])#main added to calcdistpoints to prevent confusion
   i3 = 0
   i4 = len(newlist)-1
   dist = 0
   for i in range(0, counter):
      for i2 in range(counter,len(newlist)):
         dist = calcdistpointsmain(newlist[i],newlist[i2])
         if (dist<min):
            min = dist
            i3 = i
            i4 = i2


   anslist = []
#   anslist.append(newlist[i3])
#   anslist.append(newlist[i4])
   anslist.append(min)#0 -Replaced dist with min
   anslist.append(direction[i3])#Order on first list
   anslist.append(direction[i4])#Order on second list
   print('Last checked '+newlist[i3].name+' '+newlist[i4].name)
   return anslist

# I need to add a main "clause" verifier to the following.
theoverlist = []
thefile = open("TSPut.txt", "r", encoding="utf-8")
theaverageanglelist = thefile.readlines()
thefile.close()
pathList = []

searcherlist = []
searcherlist = filereader.retrieve_locations_from_file('Locations.txt')
searcherpolylist = []
searcherpolylist = filereader.retrieve_locationslist_from_file('LocationsPolyordinates.txt')


for s in theaverageanglelist:
    #Name separator Please do not re-use the separator.
    separator = '#$%$#$$#'
    name = s.strip().split(separator)[0]#Please put the 0;0;0;0 polyordinate after the # if there is no actual polyordinate
    if (searcherlist.count(name)>0) or (geopie.place_exists(name)):
        polyordinate = s.strip().split(separator)[1]

        if searcherlist.count(name)>0:
            indexer = searcherlist.index(name)
            polyordinate = searcherpolylist[indexer] 
        elif (bWifiSearch==False):  
            polyordinate = polyordinate.split(';')
            print(f'Polyordinate for {name} obtained from file not geopy as {str(polyordinate)}')          
        else:

            polyordinate = geopie.get_xyz_coordinates(name)
            filereader.store_location_to_file(name, 'Locations.txt')
            filereader.store_locationlist_to_file(polyordinate, 'LocationsPolyordinates.txt')
            print(f'Polyordinate for {name} obtained from geopy as {str(polyordinate)}')
        tempPoint = Pointclass.Point(polyordinate,name) #data = [tempPoint] - No need..i guess
        path = [tempPoint]
        pathList.append(path)
        print(f'Location {name} added to the list')
    

iIndex = 0 #The number that will increase every time we move on.
iFound = 0
while len(pathList)>1:
    
    lBegin = []
    lend = []
    if ballsearched == False:
        print('\n|||||||||||||||||||Baseliner checked to start new search loop||||||||||||||||||||||||||||')
        #mindistlist = Getdistpathsend(pathList[0],pathList[len(pathList)-1])#Thats why when it gets to the end it seems to skip it does this first okay.
        #imin1 = 0
        #imin2 = len(pathList)-1

        #1.Search for distances and store them
        for i in range(0, len(pathList)-1):
            for i2 in range(i+1, len(pathList)):
                distlist = Getdistpathsend(pathList[i],pathList[i2])#Returns the distance, the direction of one list and the other. consider removing the distlist
                #if (distlist[0]<mindistlist[0]):
                #   mindistlist = distlist#min = dist
                #   imin1 = i
                #   imin2 = i2

        #2.Save
        #Sort the list
        combined = list(zip(name_distance_list, name_list))
        combined.sort()
        name_distance_list, name_list = zip(*combined)
        name_distance_list, name_list = list(name_distance_list), list(name_list)

        #Save the list
        filereader.write_string_lists_to_file(name_list, 'Namecombos.txt')
        filereader.write_floats_to_file(name_distance_list,'Namecombostodist.txt')

        #Sort the list
        combined = list(zip(poly_distance_list, poly_list))
        combined.sort()
        poly_distance_list, poly_list = zip(*combined)
        poly_distance_list, poly_list = list(poly_distance_list), list(poly_list)

        #Save the list
        filereader.write_two_number_lists_per_line(poly_list,'Polyordinatecombos.txt')
        filereader.write_floats_to_file(poly_distance_list,'Polyordinatecombostodist.txt')
        print('\nFull distance analysis checked. Storage Updated. Remembering this will be faster next time!\n|||||||||||||||||||||||||_________________|||||||||||||||||||||||||||\n')

        #3.Exit
        ballsearched = True
        print('The list has been sorted.')

 
    bFoundcount = 0
    while (bFoundcount<2):
        bFoundcount = 0
        if benoughtime:#Search by name or else by polyordinates
            #Search through the list for the name.
            dist = name_distance_list[iIndex]
            name1 = name_list[iIndex][0]
            name2 = name_list[iIndex][1]
            print(f'The names are {name1} and {name2} distance is {str(dist)}km')

            iFound1, iFound2 = -1, -1
            dir1, dir2 = 0, 0

            for i in range(0, len(pathList)):
                if (i!=iFound2) and ((pathList[i][0].name==name1) or (pathList[i][len(pathList[i])-1].name==name1)):
                    iFound1 = i
                    if (pathList[i][0].name==name1):
                        dir1=1 
                    else:
                        dir1=-1
                    bFoundcount += 1
                    print(f'One found at {str(pathList[i][0].name)} at index {str(i)}')
                    
                if (i!=iFound1) and ((pathList[i][0].name==name2) or (pathList[i][len(pathList[i])-1].name==name2)):
                    iFound2 = i
                    if (pathList[i][0].name==name2):
                        dir2=1 
                    else:
                        dir2=-1
                    bFoundcount += 1
                    print(f'One found at {str(pathList[i][0].name)} at index {str(i)}')
        elif benoughtime==False:#Search by poly or else by polyordinates
            #Search through the list for the polys.
            dist = poly_distance_list[iIndex]
            poly1 = poly_list[iIndex][0]
            poly2 = poly_list[iIndex][1]
            print(f'The polyordinates are {str(poly1)} and {str(poly2)} distance is {str(dist)}km')

            iFound1, iFound2 = -1, -1
            dir1, dir2 = 0, 0

            for i in range(0, len(pathList)):
                if (i!=iFound2) and ((pathList[i][0].poly_ordinate==poly1) or (pathList[i][len(pathList[i])-1].poly_ordinate==poly1)):
                    iFound1 = i
                    if (pathList[i][0].poly_ordinate==poly1):
                        dir1=1 
                    else:
                        dir1=-1
                    bFoundcount += 1
                    print(f'One found at {str(pathList[i][0].poly_ordinate)} at index {str(i)}')
                    
                if (i!=iFound1) and ((pathList[i][0].poly_ordinate==poly2) or (pathList[i][len(pathList[i])-1].poly_ordinate==poly2)):
                    iFound2 = i
                    if (pathList[i][0].poly_ordinate==poly2):
                        dir2=1 
                    else:
                        dir2=-1
                    bFoundcount += 1
                    print(f'One found at {str(pathList[i][0].poly_ordinate)} at index {str(i)}')

        if (bFoundcount==2):
            iFound +=1 
        print(f'The results are: There are {str(bFoundcount)} identified. And {str(iFound)} pairs found in total.')
        iIndex +=1 #Moving is needed all the time If not found, move on
        print(f'Locations are not found. Length is {len(pathList)}')

    mindistlist = [dist,dir1,dir2]
    imin1, imin2 = iFound1, iFound2


    print('New round of evaluation')
    
    mid2 = (len(pathList[imin1])-1)/2
    index2 = math.floor(mid2+-1*mindistlist[1]*mid2)

    i3 = (len(pathList[imin2])-1)/2
    index4 = math.floor(i3-1*mindistlist[2]*i3)

    print('The smallest distance so far is: '+str(mindistlist[0])+'. This is from '+str(pathList[imin1][index2].name)+' to '+str(pathList[imin2][index4].name))
    
    LinkPath(pathList[imin1],mindistlist,pathList[imin2]) #pathList[imin1].
    del pathList[imin2]

    for s in pathList:
        for s2 in s:
            print(s2.name, end="; ")
        print('')
    
lResults = []
print('\nResults are:__')
for s in pathList[0]:
    print(s.name)
    lResults.append(geopie.coordinates(s.name))
foliumclass.gpshtml(lResults)




#File format
#Cape Town#$%$#$$#0;0;0;0         
#            