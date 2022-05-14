#!/usr/bin/env python3
import psycopg2

"""Database Connection"""

'''
Connect to the database using the connection string
'''

def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y22s1c9120_unikey"
    passwd = "password"
    myHost = "soit-db-pro-2.ucc.usyd.edu.au"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                user=userid,
                                password=passwd,
                                host=myHost)
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)

    # return the connection to use
    return conn


'''
Validate employee login based on username and password
'''


def checkEmpCredentials(username, password):
    return ['2', 'jaddison', 'Jo Addison', '111', 'jaddison@wsa.com.au', 'Technician']


'''
List all the associated tests in the database for an employee
'''


def findTestsByEmployee(username):
    return


'''
Find a list of test events based on the searchString provided as parameter
See assignment description for search specification
'''


def findTestsByCriteria(searchString):
    return


'''
Add a new test event
'''


def addTest(test_date, regno, status, technician, testengineer):
    return


'''
Update an existing test event
'''


def updateTest(test_id, test_date, regno, status, technician, testengineer):
    return
