
###### Mohmoud Mohamed - WGU Student ID: 002439508
######
######
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
# Load address data from CSV
# Time complexity: O(A), where A is the number of addresses in the CSV
# Space complexity: O(A), where A is the number of addresses in the CSV

with open("address.csv") as addressFile:
    addressReader = csv.reader(addressFile)
    addressReader = list(addressReader)

# Reading Distance CSV
# Load distance data from CSV
# Time complexity: O(D^2), where D is the number of distances (DxD matrix)
# Space complexity: O(D^2), where D is the number of distances (DxD matrix)

with open("distance.csv") as distanceFile:
    distanceReader = csv.reader(distanceFile)
    distanceReader = list(distanceReader)   

### Hash Table Class for efficient retrieval of package data

# Referencing C950 zyBooks: Figure 6.2.1: Hash table using chaining

# Hash Table implementation
# Time complexity: O(1) for add, retrieve, remove operations
# Space complexity: O(N + M), where N is the initial capacity and M is the number of packages

class HashTable:

    # Initialize hashtable with specified initial capacity
    #
    def __init__(self, initial_capacity = 40):
        self.hashtable = []
        for number in range(initial_capacity):
            self.hashtable.append([])
    #
    # Adds a new item into the hash table and updates an existing item in the array.
    # Calculate hash bucket
    #
    def add(self, hash_key, hash_item):
        #
        # Add key-value pair to the hashtable
        #
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]
        #
        # If the key is already present in the hash table bucket, proceed to update it.
        # Check for existing key and update value if found
        # Check for existing key and update value if found
        #
        for keyvaluepair in hashbucket_array:
            #
            if keyvaluepair[0] == hash_key:
                keyvaluepair[1] = hash_item
                return True
                #
        # If the item is not present in the bucket, append it to the end of the array.
        # Add new key-value pair
        #
        key_value = [hash_key, hash_item]
        hashbucket_array.append(key_value)
        return True
        #
    # Gets the hash table corresponding to an item with a matching key.
    # If found, it will return the item; otherwise, it will return None.
    #
    def retrieve(self, hash_key):
        #
        # Calculate hash bucket
        # Retrieve value based on key from the hashtable
        #
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]
        #
        # Fetch the key from the bucket
        # Retrieve value based on key
        #
        for keyvaluepair in hashbucket_array:
        #
            if keyvaluepair[0] == hash_key:
                return keyvaluepair[1]  # Value of keyvaluepair
        return None 
        #
    # Deletes an entry with a key that matches from the hash table.
    #
    def remove(self, hash_key):
        #
        # Remove key-value pair based on key from the hashtable
        #
        hashbucket = hash(hash_key) % len(self.hashtable)
        hashbucket_array = self.hashtable[hashbucket]
        #
        # If the item is present, it will be removed.
        # Remove key-value pair if key is found
        #
        if hash_key in hashbucket_array:
            hashbucket_array.remove(hash_key)
            #
### Package Class to represent package data
#
# Where the information regarding the criteria for the package is stored.
# Time complexity: O(1) for initialization and changeStatus
# Space complexity: O(1) for each package instance
#
class Packages:
    def __init__(self, ID, packageStreet, packageCity, packageState, packageZip, packageDeadline, packageWeight, packageNotes, packageStatus, packageDepartureTime, packageDeliveryTime):
        #
        # Initialize package instance with specified attributes
        #
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
        #
    def __str__(self):
        #
        # String representation of the package instance
        #
        return "ID: %s, %-20s, %s, %s,%s, Package Deadline: %s,%s,%s,Package Departure Time: %s,Package Delivery Time: %s" % (self.ID, self.packageStreet, self.packageCity, self.packageState, self.packageZip, self.packageDeadline, self.packageWeight, self.packageStatus, self.packageDepartureTime, self.packageDeliveryTime)
    #
    # The status of a package will be updated based on the entered time using this method.
    #
    def changeStatus(self, timeDiff):
        #
        # Change package status based on time difference
        #
        if self.packageDeliveryTime == None:
            self.packageStatus = "Package Location: The Hub"
        elif timeDiff < self.packageDepartureTime:
            self.packageStatus = "Package Location: The Hub"   
        elif timeDiff < self.packageDeliveryTime:
            self.packageStatus = "Package Location: En Route"     
        else:
            self.packageStatus = "Package Location: Delivered" 
        #
        # Special case for package with ID 9
        #
        if self.ID == 9:          # Once the package for item 9 is received, the address will be updated to the correct one.
            if timeDiff > datetime.timedelta (hours = 10, minutes = 20):
                self.packageStreet = "410 S State St"  
                self.packageZip = "84111"  
            else:
                self.packageStreet = "300 State St"
                self.packageZip = "84103"     
                #
# Generating packages containing information from the CSV to be inserted into the Hash Table.
# Function to load package data from CSV and populate the HashTable
# Time complexity: O(N), where N is the number of packages
# Space complexity: O(N), where N is the number of packages
#
def loadingPackageData(filename):
    with open(filename) as packageFile:
        packageReader = csv.reader(packageFile, delimiter = ',')
        next (packageReader)
        for package in packageReader:
            packageInstanceID = int(package[0])
            #
            packageInstanceStreet = package[1]
            #
            packageInstanceCity = package[2]
            #
            packageInstanceState = package[3]
            #
            packageInstanceZip = package[4]
            #
            packageInstanceDeadline = package[5]
            #
            packageInstanceWeight = package[6]
            #
            packageInstanceNotes = package[7]
            #
            packageInstanceStatus = "Package Location: The Hub"
            packageInstanceDepartureTime = None
            packageInstanceDeliveryTime = None
            #
            # Incorporating package information into the hash table.
            #
            packageInstance = Packages(packageInstanceID, packageInstanceStreet, packageInstanceCity, packageInstanceState, packageInstanceZip, packageInstanceDeadline, packageInstanceWeight, packageInstanceNotes, packageInstanceStatus, packageInstanceDepartureTime, packageInstanceDeliveryTime)
            #
            packageHashTable.add(packageInstanceID, packageInstance)
            #
# Package Hash Table
# Initialize Hash Table
# Time complexity: O(1)
# Space complexity: O(N), where N is the number of packages
#
packageHashTable = HashTable() 
#
# Creating a Truck: Necessary Requirements
# Truck class to represent truck data
#
### Truck Class
# Time complexity: O(1) for initialization
# Space complexity: O(1) for each truck instance
#
class Truck:
    def __init__(self, truckSpeed, truckMiles, truckLocation, truckLeavingTime, packages):
        #
        # Initialize truck instance with specified attributes
        #
        self.truckSpeed = truckSpeed
        self.truckMiles = truckMiles
        self.truckLocation = truckLocation
        self.truckTime = truckLeavingTime
        self.truckLeavingTime = truckLeavingTime
        self.packages = packages
        #
    def __str__(self):
        #
        # String representation of the truck instance
        #
        return "%s,%s,%s,%s,%s,%s" % (self.truckSpeed, self.truckMiles, self.truckLocation, self.truckTime, self.truckLeavingTime, self.packages)
        #
# Determines the minimum distance to the upcoming address.
# Function to find minimum address ID
# Time complexity: O(A), where A is the number of addresses
# Space complexity: O(1)
#
def minimumAddress(address):
    for row in addressReader:
        if address in row[2]:
           return int(row[0])
            #
# Calculates the distance separating two addresses.
# Function to calculate distance between two addresses
# Time complexity: O(1)
# Space complexity: O(1)
#
def betweenAddresses(address1, address2):
    distance = distanceReader[address1][address2]
    if distance == '':
        distance = distanceReader[address2][address1]
    return float(distance)
    #
# The function retrieves data from a CSV file.
# Load package data into Hash Table
# Time complexity: O(N), where N is the number of packages
# Space complexity: O(N), where N is the number of packages
#
loadingPackageData('package.csv')
#
# Loading the trucks manually and assigning them a departure time.
# Initialize three trucks with specified parameters
# Initialize three trucks with specified parameters
# Time complexity: O(1) for each truck initialization
# Space complexity: O(1) for each truck instance
#
truckFirst = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 8),[1,13,14,15,16,19,20,27,29,30,31,34,37,40])
truckSecond = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 11),[2,3,4,5,9,18,26,28,32,35,36,38])
truckThird = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5),[6,7,8,10,11,12,17,21,22,23,24,25,33,39])
#
### Nearest Neighbor
#
# Package Delivery Algorithm for the Truck
# Function to simulate truck delivering packages
# Time complexity: O(N*M), where N is the number of packages and M is the number of addresses
# Space complexity: O(N), where N is the number of packages
#
def truckDeliverThePackages(truck):
    print("Truck Object Instance Initialized")
    #
    # Generates an array containing all the packages slated for delivery.
    #
    deliveryArray = []
    #
    # Stores packages from the hash table into the deliveryArray array.
    #
    for packageID in truck.packages:
        package = packageHashTable.retrieve(packageID)
        deliveryArray.append(package)
        #
    truck.packages.clear()
    #
    # The algorithm will continue running as long as there are packages yet to be delivered.
    # Loop until all packages are delivered
    #
    while len(deliveryArray) > 0:
        upcomingAddress = 2000
        upcomingPackage = None
        #
        # Find the next package to be delivered based on distance
        #
        for package in deliveryArray:
            if package.ID in [25, 6]:
                upcomingPackage = package
                upcomingAddress = betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet))
                break
            if betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet)) <= upcomingAddress:
                upcomingAddress = betweenAddresses(minimumAddress(truck.truckLocation), minimumAddress(package.packageStreet))
                upcomingPackage = package
                #
        # Add the upcoming package to the truck
        #
        truck.packages.append(upcomingPackage.ID)    
        deliveryArray.remove(upcomingPackage)
        truck.truckMiles += upcomingAddress
        truck.truckLocation = upcomingPackage.packageStreet
        truck.truckTime += datetime.timedelta(hours = upcomingAddress / 18)
        upcomingPackage.packageDeliveryTime = truck.truckTime
        upcomingPackage.packageDepartureTime = truck.truckLeavingTime
        #   
# Initiates the departure of trucks for package delivery.
# Simulate package delivery for each truck
#
truckDeliverThePackages(truckFirst)
truckDeliverThePackages(truckThird)
#
# Truck 2 will remain until either Truck 1 or Truck 2 returns.
# Synchronize leaving time of the second truck with the earliest arrival time of the first and third trucks
#
truckSecond.truckLeavingTime = min(truckFirst.truckTime, truckThird.truckTime)
truckDeliverThePackages(truckSecond)
#
# WGUPS
#
print("WGUPS")
#
# The combined mileage of all the trucks.
# Output total miles driven by all trucks
#
print ("The total miles driven by all the trucks is:", (truckFirst.truckMiles + truckSecond.truckMiles + truckThird.truckMiles))
#
### User Interface
#
# Continuous loop to input time and view package status
#
# 1. Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
# 2. Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
# 3. Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.
# Time complexity: Depends on how long the user prolongs the loop for.
# Space complexity: O(1)
#
while True:
    #
    # Input desired time to view package status
    #
    inputTime = input("Kindly input the desired time to view the status of each package. Use the format HH:MM.")
    (h, m) = inputTime.split(":")
    timeDiff = datetime.timedelta(hours = int(h), minutes = int(m))
    try:
        packageEntry = [int(input("Input the desired Package ID or input nothing to see all package statuses."))]
    except ValueError:
        packageEntry =  range(1, 41)
        #
    # Loop through selected package IDs and update status based on time difference
    #
    for packageID in packageEntry:
        package = packageHashTable.retrieve(packageID)
        package.changeStatus(timeDiff)
        print(str(package))                    
#
