"""Database Connection"""
import psycopg2

global current_user


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
    global current_user

    try:
        curs = openConnection().cursor()
        curs.callproc("checkEmpCredentials", [username, password])

        current_user = username
        return curs.fetchone()
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
        return


def findTestsByEmployee(username):
    """List all the associated tests in the database for an employee"""
    result = []
    try:
        curs = openConnection().cursor()
        curs.callproc("findTestsByEmployee", [username])

        row = curs.fetchone()
        while row:
            result.append({
                "test_id": str(row[0]),
                "test_date": row[1],
                "regno": row[2],
                "status": row[3],
                "technician": row[4],
                "testengineer": row[5],
                "technicianuser": current_user,
            })
            row = curs.fetchone()
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    finally:
        return result


def findTestsByCriteria(searchString):
    """Find a list of test events based on the searchString provided as parameter
    See assignment description for search specification
    """
    keyword = str(searchString).strip().lower()
    result = []
    try:
        if keyword == "":
            return findTestsByEmployee(current_user)

        curs = openConnection().cursor()
        curs.callproc("findTestsByCriteria", [keyword])

        row = curs.fetchone()
        while row:
            result.append({
                "test_id": str(row[0]),
                "test_date": row[1],
                "regno": row[2],
                "status": row[3],
                "technician": row[4],
                "testengineer": row[5],
                "technicianuser": current_user,
            })
            row = curs.fetchone()
        return result
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)


def addTest(test_date, regno, status, technician, testengineer):
    """Add a new test event"""
    conn = openConnection()
    curs = conn.cursor()
    curs.callproc("test", [test_date, regno, status, technician, testengineer])
    result = curs.fetchone()
    if result[-1]:
        curs.execute(f"INSERT INTO TestEvent (TestDate,RegNo,Status,Technician,TestEngineer)"
                     f"VALUES ('{test_date}', '{regno}', '{result[0]}', {result[1]}, {result[2]});")
    conn.commit()
    return result[-1]


'''
Update an existing test event
'''


def updateTest(test_id, test_date, regno, status, technician, testengineer):
    return
