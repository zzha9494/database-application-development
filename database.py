"""Database Connection"""
import psycopg2


def openConnection():
    """Connect to the database using the connection string"""
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "postgres"
    passwd = "123"
    myHost = "localhost"

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


def checkEmpCredentials(username, password):
    """Validate employee login based on username and password"""
    try:
        curs = openConnection().cursor()
        curs.execute("SELECT *\
                      FROM Employee")

        # nr = 0
        row = curs.fetchone()
        while row is not None:
            # nr += 1
            if row[1] == username and row[3]:
                return row
            row = curs.fetchone()
        return
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
        return


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
