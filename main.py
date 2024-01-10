
######
######
###### Mohmoud Mohamed - WGU Student ID: 002439508
######
######

### 3 trucks
### 2 drivers
### Drivers leave the hub no earlier than 8:00 a.m
### The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

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

### Nearest Neighbor



### User Interface



