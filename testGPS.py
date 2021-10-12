#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from firebase import firebase
from datetime import datetime
import time
import random
import csv
import logging
import threading

urlDB = 'https://maps-f1ef8.firebaseio.com/'

routeFiles = ["RouteLine1.csv", "RouteLine2.csv", "RouteLine3.csv"]
fieldName = ['Latitude', 'Longitude']
users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']


def sendData(user, ID, lat, lng, speed, time):
    data = {'id': ID,
            'lat': lat,
            'lng': lng,
            'speed': speed,
            'time': time
            }

    fb = firebase.FirebaseApplication(urlDB, None)
    # result = fb.post('/user/',data)
    result = fb.patch('/' + user + '/', data)
    return result


def currentTime():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # print("timestamp =", timestamp)
    return timestamp


##########

def readRoute(fileName):
    with open(fileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        if reader.fieldnames == fieldName:
            Rlatitude = []
            Rlongitude = []
            # Rtime=[]
            print('Field names found: ', reader.fieldnames)
            line_count = 0
            for row in reader:
                # print(row['Latitude'], row['Longitude'])
                if line_count != 0:
                    # Rtime.append(row['TimeStamp']);
                    Rlatitude.append(float(row['Latitude']))
                    Rlongitude.append(float(row['Longitude']))
                line_count += 1

            print(line_count - 1, 'lines have been processed')

            return Rlatitude, Rlongitude

        else:
            print('Field names found: ', reader.fieldnames)
            print('It seems that the fields are not what the csv file should have')

            return None, None


def bus1():
    [LatVector, LngVector] = readRoute(routeFiles[0])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[0], 1, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus2():
    [LatVector, LngVector] = readRoute(routeFiles[1])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[1], 2, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus3():
    [LatVector, LngVector] = readRoute(routeFiles[2])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[2], 3, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus4():
    [LatVector, LngVector] = readRoute(routeFiles[2])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[3], 4, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus5():
    [LatVector, LngVector] = readRoute(routeFiles[1])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[4], 5, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus6():
    [LatVector, LngVector] = readRoute(routeFiles[0])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[5], 6, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)

def bus7():
    [LatVector, LngVector] = readRoute(routeFiles[2])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[6], 7, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus8():
    [LatVector, LngVector] = readRoute(routeFiles[2])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[7], 8, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus9():
    [LatVector, LngVector] = readRoute(routeFiles[1])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[8], 9, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)


def bus10():
    [LatVector, LngVector] = readRoute(routeFiles[0])

    for r in range(0, len(LatVector)):
        lat = LatVector[r] + ((random.random() - 0.5) / 10000)
        lng = LngVector[r] + ((random.random() - 0.5) / 10000)
        speed = 20 + random.random() * 5
        result = sendData(users[9], 10, lat, lng, speed, currentTime())

        print(result)
        time.sleep(5)




if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    
    readRoute(routeFiles[0])
    

    x1 = threading.Thread(target=bus1, args=())
    threads.append(x1)
    x1.start()

    x2 = threading.Thread(target=bus2, args=())
    threads.append(x2)
    x2.start()

    x3 = threading.Thread(target=bus3, args=())
    threads.append(x3)
    x3.start()

    x4 = threading.Thread(target=bus4, args=())
    threads.append(x4)
    x4.start()

    x5 = threading.Thread(target=bus5, args=())
    threads.append(x5)
    x5.start()

    x6 = threading.Thread(target=bus6, args=())
    threads.append(x6)
    x6.start()

    x7 = threading.Thread(target=bus7, args=())
    threads.append(x7)
    x7.start()

    x8 = threading.Thread(target=bus8, args=())
    threads.append(x8)
    x8.start()

    x9 = threading.Thread(target=bus9, args=())
    threads.append(x9)
    x9.start()

    x10 = threading.Thread(target=bus10, args=())
    threads.append(x10)
    x10.start()

















