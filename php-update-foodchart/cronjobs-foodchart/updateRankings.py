#!/usr/bin/python3
# import pymongo
import sys
import requests
import json
from datetime import datetime

def createLogFile(period, operation):
    global log
    # datetime object containing current date and time
    now = datetime.now()
    # # dd/mm/YY H:M:S
    dateString = now.strftime("%d_%m_%Y_%H:%M:%S")
    log = open("/var/log/" + operation + "_updateRankings_" + dateString + ".txt", "w+")
    log.write("###### \t Log file for " + operation + " request \t ###### \n")
    log.write("###### \t Log file created on " + dateString + " \t ###### \n")

def wipeStatistics(period):
    methodData = { 'period' : period }

    data = {
        'foodchart_token' : 'Felix@nul942Comdsa)(*&H((J*DSXT#@0932~2PaMMMdX*3@',
        'wipeStatistics' : json.dumps(methodData)
    }

    sendRequest(data, "Wipe")

def updateRankings():
    data = {
        'foodchart_token' : 'Felix@nul942Comdsa)(*&H((J*DSXT#@0932~2PaMMMdX*3@',
        'updateRankings' : True
    }
    sendRequest(data, "Update")

def sendRequest(data, operation):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.post('http://127.0.0.1:80/api/update_rankings.php', data=data, headers=headers)

    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        
        log.write("\n")
        log.write("###### \t Server Response : " + json.dumps(jsonResponse) + " \t ###### \n")
        log.write("\n")

        if jsonResponse["success"] == True :
            log.write("*\t Status : Rankings Succesfully " + operation + "d\t*\n")
            log.write("*\t Response Data : " + json.dumps(jsonResponse["data"]) + "\t*\n")
        else :
            log.write("*\t Status : Error occured while trying to " + operation + " rankings.\t*\n")
            log.write("*\t Response Error : " + json.dumps(jsonResponse["error"]) + " \n")
    else:
        log.write("\n")
        log.write("###### \t Server Response : " + response.status_code + " \t ######\n")
        log.write("\n")
    
if __name__== "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 2 :
        print(" Invalid arguments provided. Usage : python3 updateRankings.py $period ($period = daily or weekly or monthly)")
        sys.exit()
    else :
        if sys.argv[1] == "update":
            createLogFile(sys.argv[1], "update")
            updateRankings()
            log.close()
        elif sys.argv[1] == "wipe":
            if sys.argv[2] == "daily" or sys.argv[2] == "weekly" or sys.argv[2] == "monthly" :
                createLogFile(sys.argv[1], "wipe")
                wipeStatistics(sys.argv[2])
                log.close()
            else :
                print("Invalid arguments provided. Usage : python3 updateRankings.py $update/$wipe $period ($period = daily or weekly or monthly)")
