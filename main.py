
######
######
###### Mohmoud Mohamed - WGU Student ID: 002439508
######
######

### 3 trucks
### 2 drivers
### Drivers leave the hub no earlier than 8:00 a.m
### The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

### 40 packages for two of the trucks
### Under 140 miles

### Importing From Python Standard Library

# Import the datetime module for working with dates and times

import datetime

# Import the csv module for reading and writing CSV files

import csv

### CSV File Reading

# Reading Address CSV

with open("address.csv") as addressFile:
    addressReader = csv.reader(addressFile)
    addressReader = list(addressReader)

# Reading Distance CSV

with open("distance.csv") as distanceFile:
    distanceReader = csv.reader(distanceFile)
    distanceReader = list(distanceReader)   

### Hash Table Class

# Referencing C950 zyBooks: Figure 7.8.2: Hash table using chaining

# Hash Table implementation

class HashTable:
    def __init__(self, initial_capacity = 40):
        self.hashtable = []
        for number in range(initial_capacity):
            self.hashtable.append([])

    # Adds a new item into the hash table and updates an existing item in the array.

    def add(self, hash_key, hash_item):
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]

        # If the key is already present in the hash table bucket, proceed to update it.

        for keyvaluepair in hashbucket_array:

            if keyvaluepair[0] == hash_key:
                keyvaluepair[1] = hash_item
                return True

        # If the item is not present in the bucket, append it to the end of the array.
 
        key_value = [hash_key, hash_item]
        hashbucket_array.append(key_value)
        return True

    # Gets the hash table corresponding to an item with a matching key.
    # If found, it will return the item; otherwise, it will return None.

    def retrieve(self, hash_key):
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]

        # Fetch the key from the bucket

        for keyvaluepair in hashbucket_array:

            if keyvaluepair[0] == hash_key:
                return keyvaluepair[1]  # Value of keyvaluepair
        return None 
        
    # Deletes an entry with a key that matches from the hash table.

    def remove(self, hash_key):
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]

        # If the item is present, it will be removed.

        if hash_key in hashbucket_array:
            hashbucket_array.remove(hash_key)

### Package Class

# Where the information regarding the criteria for the package is stored.
 
class Packages:
    def __init__(self, ID, packageStreet, packageCity, packageState, packageZip, packageDeadline, packageWeight, packageNotes, packageStatus, packageDepartureTime, packageDeliveryTime):
        self.ID = ID
        self.packageStreet = packageStreet
        self.packageCity = packageCity
        self.packageState = packageState
        self.packageZip = packageZip
        self.packageDeadline = packageDeadline
        self.packageWeight = packageWeight
        self.packageNotes = packageNotes
        self.packageStatus = packageStatus
        self.packageDepartureTime = None # packageDepartureTime
        self.packageDeliveryTime = None # packageDeliveryTime

    def __str__(self):
        return "ID: %s, %-20s, %s, %s,%s, Package Deadline: %s,%s,%s,Package Departure Time: %s,Package Delivery Time: %s" % (self.ID, self.packageStreet, self.packageCity, self.packageState, self.packageZip, self.packageDeadline, self.packageWeight, self.packageStatus, self.packageDepartureTime, self.packageDeliveryTime)

    # The status of a package will be updated based on the entered time using this method.

    def changeStatus(self, timeDiff):
        if self.packageDeliveryTime == None:
            self.packageStatus = "Package Location: The Hub"
        elif timeDiff < self.packageDepartureTime:
            self.packageStatus = "Package Location: The Hub"   
        elif timeDiff < self.packageDeliveryTime:
            self.packageStatus = "Package Location: En Route"     
        else:
            self.packageStatus = "Package Location: Delivered" 
        if self.ID == 9:          # Once the package for item 9 is received, the address will be updated to the correct one.
            if timeDiff > datetime.timedelta (hours = 10, minutes = 20):
                self.packageStreet = "410 S State St"  
                self.packageZip = "84111"  
            else:
                self.packageStreet = "300 State St"
                self.packageZip = "84103"     

    # Generating packages containing information from the CSV to be inserted into the Hash Table.

def loadingPackageData(filename):
    with open(filename) as packageFile:
        packageReader = csv.reader(packageFile, delimiter = ',')
        next (packageReader)
        for package in packageReader:
            packageInstanceID = int(package[0])

            packageInstanceStreet = package[1]

            packageInstanceCity = package[2]

            packageInstanceState = package[3]

            packageInstanceZip = package[4]

            packageInstanceDeadline = package[5]

            packageInstanceWeight = package[6]

            packageInstanceNotes = package[7]

            packageInstanceStatus = "Package Location: The Hub"
            packageInstanceDepartureTime = None
            packageInstanceDeliveryTime = None

            # Incorporating package information into the hash table.

            packageInstance = Packages(packageInstanceID, packageInstanceStreet, packageInstanceCity, packageInstanceState, packageInstanceZip, packageInstanceDeadline, packageInstanceWeight, packageInstanceNotes, packageInstanceStatus, packageInstanceDepartureTime, packageInstanceDeliveryTime)

            packageHashTable.add(packageInstanceID, packageInstance)

# Package Hash Table

packageHashTable = HashTable() 

# Creating a Truck: Necessary Requirements

### Truck Class

class Truck:
    def __init__(self, truckSpeed, truckMiles, truckLocation, truckLeavingTime, packages):
        self.truckSpeed = truckSpeed
        self.truckMiles = truckMiles
        self.truckLocation = truckLocation
        self.truckTime = truckLeavingTime
        self.truckLeavingTime = truckLeavingTime
        self.packages = packages

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.truckSpeed, self.truckMiles, self.truckLocation, self.truckTime, self.truckLeavingTime, self.packages)

# Determines the minimum distance to the upcoming address.

def minimumAddress(address):
    for row in addressReader:
        if address in row[2]:
           return int(row[0])

# Calculates the distance separating two addresses.

def betweenAddresses(address1, address2):
    distance = distanceReader[address1][address2]
    if distance == '':
        distance = distanceReader[address2][address1]
    return float(distance)

# The function retrieves data from a CSV file.

loadingPackageData('package.csv')

# Loading the trucks manually and assigning them a departure time.

truckFirst = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 8),[1,13,14,15,16,19,20,27,29,30,31,34,37,40])
truckSecond = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 11),[2,3,4,5,9,18,26,28,32,35,36,38])
truckThird = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5),[6,7,8,10,11,12,17,21,22,23,24,25,33,39])

### Nearest Neighbor

# Package Delivery Algorithm for the Truck

def truckDeliverThePackages(truck):
    print("Truck Object Instance Initialized")

    # Generates an array containing all the packages slated for delivery.

    deliveryArray = []

    # Stores packages from the hash table into the deliveryArray array.

    for packageID in truck.packages:
        package = packageHashTable.retrieve(packageID)
        deliveryArray.append(package)

    truck.packages.clear()

    # The algorithm will continue running as long as there are packages yet to be delivered.

    while len(deliveryArray) > 0:
        upcomingAddress = 2000
        upcomingPackage = None
        for package in deliveryArray:
            if package.ID in [25, 6]:
                upcomingPackage = package
                upcomingAddress = betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet))
                break
            if betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet)) <= upcomingAddress:
                upcomingAddress = betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet))
                upcomingPackage = package
        truck.packages.append(upcomingPackage.ID)    
        deliveryArray.remove(upcomingPackage)
        truck.truckMiles += upcomingAddress
        truck.truckLocation = upcomingPackage.packageStreet
        truck.truckTime += datetime.timedelta(hours = upcomingAddress / 18)
        upcomingPackage.packageDeliveryTime = truck.truckTime
        upcomingPackage.packageDepartureTime = truck.truckLeavingTime
            
# Initiates the departure of trucks for package delivery.

truckDeliverThePackages(truckFirst)
truckDeliverThePackages(truckThird)

# Truck 2 will remain until either Truck 1 or Truck 2 returns.

truckSecond.truckLeavingTime = min(truckFirst.truckTime, truckThird.truckTime)
truckDeliverThePackages(truckSecond)

# WGUPS

print("WGUPS")

# The combined mileage of all the trucks.

print ("The total miles driven by all the trucks is:", (truckFirst.truckMiles + truckSecond.truckMiles + truckThird.truckMiles))

### User Interface

# 1. Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
# 2. Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
# 3. Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.

while True:

    inputTime = input("Kindly input the desired time to view the status of each package. Use the format HH:MM.")
    (h, m) = inputTime.split(":")
    timeDiff = datetime.timedelta(hours = int(h), minutes = int(m))
    try:
        packageEntry = [int(input("Input the desired Package ID or input nothing to see all package statuses."))]
    except ValueError:
        packageEntry =  range(1, 41)
    for packageID in packageEntry:
        package = packageHashTable.retrieve(packageID)
        package.changeStatus(timeDiff)
        print(str(package))                    

