#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:36:51 2018

@author: brant
"""
import pandas as pd
import sys
import scipy.stats as stats

inputArg1 = sys.argv[-2]
inputArg2 = sys.argv[-1]
data = pd.read_csv("/home/brant/Downloads/VISIBLE TO STUDENTS/Week 2/Day 7/statistics/data/airbnb.csv")
dataDF = pd.DataFrame(data)
    
def information(inputArg2):
    if (inputArg2 == ""):
        print("Please add a city, check your spelling, or add quotation marks around the city if it is multiple words")
        
    sortedDF = dataDF[dataDF.neighborhood == inputArg2]
    print("Number of listings: " + str(len(sortedDF)))
    
    numHomes = sortedDF[sortedDF.room_type == "Entire home/apt"]
    print("Number of private homes/apts: " + str(len(numHomes)))
    
    numRooms = sortedDF[sortedDF.room_type == "Private room"]
    print("Number of private rooms: " + str(len(numRooms)))
    
    sharedRooms = sortedDF[sortedDF.room_type == "Shared room"]
    print("Number of shared rooms: " + str(len(sharedRooms)))

    print("Average price per room: " + str(sortedDF.price.mean()))
    
    print("Price quartiles: " + str(stats.mstats.mquantiles(sortedDF.price)))
    pass


def search():
    minPrice = 0
    maxPrice = 1000000
    minRooms = 0
    maxRooms = 1000000
    minPrice = input("Please enter minimum price (or leave blank): ")
    maxPrice = input("Please enter maximum price (or leave blank): ")
    minRooms = input("Please enter minimum amount of rooms (or leave blank): ")
    maxRooms = input("Please enter maximum amount of rooms (or leave blank): ")
    neighborhoodArray = []
    neighborhoodInput = ""
    while (neighborhoodInput != "n"):
        if (neighborhoodInput != ""):
            neighborhoodArray.append(neighborhoodInput)
        neighborhoodInput = input("Enter a desired neighborhood, be careful of spelling.  Enter 'n' to stop: ")
    sortCat = input("Sort by price, score, or reviews? ")
    if (minPrice == ""):
        minPrice = 0
    if (maxPrice == ""):
        maxPrice = 1000000
    if (minRooms == ""):
        minRooms = 0
    if (maxRooms == ""):
        maxRooms = 1000000

    minPrice = int(minPrice)
    maxPrice = int(maxPrice)
    minRooms = int(minRooms)
    maxRooms = int(maxRooms)

    sorted1 = dataDF[dataDF.price >= minPrice]
    sorted2 = sorted1[sorted1.price <= maxPrice]
    sorted3 = sorted2[sorted2.bedrooms >= minRooms]
    sorted4 = sorted3[sorted3.bedrooms <= maxRooms]
    
    print(neighborhoodArray[:])
    
    mask = sorted4[sorted4["neighborhood"].isin(neighborhoodArray)]
        
    print(sorted4[mask])
        
    """
    if((sortCat == "price") or (sortCat == "Price")):
        sorted4.sort(sorted4.price, ascending=True)
    elif ((sortCat == "score") or (sortCat == "Score")):
        sorted4.sort(sorted4.overall_satisfaction, ascending=False)
    elif ((sortCat == "reviews") or (sortCat == "Reviews")):
        sorted4.sort(sorted4.reviews, ascending=False)

    if (len(sorted4) > 0):
        print(sorted4)
    else:
        print("There were no searches that matched your criteria")
    """
    pass

def main(inputArg1):
    if (inputArg1 == "information"):
        information(inputArg2)
    elif(inputArg2 == "search"):
        search()
    else:
        print("Incorrect function.  Please use either 'information' or 'search'")

main(inputArg1)
