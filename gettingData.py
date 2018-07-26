# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:15:46 2018

@author: Hamza
"""

import os

def main():
    
    #CHANGE THIS!!
    os.chdir("C:\\Users\\ghost\\Desktop\\pytorch-yolo-v3-master\\")
    
    allObjects = []
    with open ("data.txt", "rt") as myFile:
        for line in myFile:
            if "car" or "truck" or "van" in line:
                allObjects.append(line)
    
    carCount = 0 
    truckCount = 0
    for i in range(len(allObjects)):
        carCount = carCount + allObjects[i].count("car")
        truckCount = truckCount + allObjects[i].count("truck")
            
    total = truckCount + carCount
    
    with open("carData.txt", "a") as myFile:
        myFile.write("\n\n\n")
        myFile.write("We found %d car(s)" % total)
                
main()
         
            