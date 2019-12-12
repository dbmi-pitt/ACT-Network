import sys
import urllib.request
import json
import datetime
import calendar
import time
import argparse
import getpass 

import cx_Oracle
from string import Template 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#
# Example selenium script to query ACT (i2b2/SHRINE) databases and
# fill in a Redcap survey
#

# Constants
millisecondsInDay = 24 * 60 * 60 * 1000

# Configure
site = 'Pitt'

#TODO PARAMETERIZE and DE-ORACLE

# SHRINE Schema
dataStewardSchema='NCATSPROD_STEWARDDB'
dataStewardUserName = 'XXX'
dataStewardPassword = 'XXX'

# PM (i2b2) Schema
pmHost='not used'
pmSchema='NCATSPROD_PM'
pmUserName = 'XXX'
pmPassword = 'XXX'


#conn_str_prod01 = Template('$USERNAME/$PASSWORD@HOST:PORT/SID')
conn_str_prod01 = 'USERNAME/PASSWORD@HOST:PORT/SID'



# Data Steward Metric queries (Templates)
# Total queries
totalQueriesSQL = Template('select count(*) from $DB_SCHEMA."queries" '
'where "date"  between' 
'(to_date(\'$FIRST_MONTH_DAY 00:00:00\', \'MM/DD/YYYY HH24:MI:SS\') - '
'to_date(\'19700101\', \'YYYYMMDD\')) * $MILLISEC_IN_DAY and '
'(to_date(\'$LAST_MONTH_DAY 00:00:00\', \'MM/DD/YYYY HH24:MI:SS\') - '
'to_date(\'19700101\', \'YYYYMMDD\')) * $MILLISEC_IN_DAY')


#Total SHRINE Users
registeredUsersSQL = Template('select count(*) from $DB_SCHEMA.PM_PROJECT_USER_ROLES'
' WHERE PROJECT_ID = \'SHRINE\' AND USER_ROLE_CD = \'USER\' ')

#New Users
newRegisteredUsersSQL  = Template('select count(*) from' 
' $DB_SCHEMA.PM_PROJECT_USER_ROLES '
' WHERE PROJECT_ID = \'SHRINE\' AND USER_ROLE_CD = \'USER\''
' AND ENTRY_DATE  > \'01-$METRIC_MONTH-$METRIC_YEAR\'')

#New Query-er
newQueriersSQL = Template('select ' 
' count(distinct "researcher") from NCATSPROD_STEWARDDB."queries"' 
' where "date" between '
' (to_date(\'$FIRST_MONTH_DAY 00:00:00\', \'MM/DD/YYYY HH24:MI:SS\') - '
' to_date(\'19700101\', \'YYYYMMDD\')) * $MILLISEC_IN_DAY'
' and (to_date(\'$LAST_MONTH_DAY 00:00:00\', \'MM/DD/YYYY HH24:MI:SS\') - '
' to_date(\'19700101\', \'YYYYMMDD\')) * $MILLISEC_IN_DAY'
' and "researcher" not in '
' ( select "researcher" from  NCATSPROD_STEWARDDB.\"queries\"'
' where "date" < (to_date(\'$FIRST_MONTH_DAY 00:00:00\', \'MM/DD/YYYY HH24:MI:SS\')'
' - to_date(\'19700101\', \'YYYYMMDD\')) * $MILLISEC_IN_DAY)')

#Monthly topics
queryTopicsSQL = Template('select distinct a."name" from ' 
 '$DB_SCHEMA."queries" b, $DB_SCHEMA."topics" a '
 'where a."id" = b."topic" and b."date" '
 'between (to_date(\'$FIRST_MONTH_DAY\', \'MM/DD/YYYY HH24:MI:SS\') - '
 'to_date(\'01/01/1970\', \'MM/DD/YYYY\')) * $MILLISEC_IN_DAY '
 'and (to_date(\'$LAST_MONTH_DAY\', \'MM/DD/YYYY HH24:MI:SS\') - '
 'to_date(\'01/01/1970\', \'MM/DD/YYYY\')) * $MILLISEC_IN_DAY')


'''
DB Utility functions
'''
def dbOracleConnect(connString):
    connection = cx_Oracle.connect(connString)
    print('Connected to DB')
    return connection

def dbExecuteQuery(conn, queryString):
    c = conn.cursor()

    try:
        c.execute(queryString)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 955:
            print('Object already exists' + queryString)
        elif error.code == 1031:
            print("Insufficient privileges - are you sure you're using the owner account?")
        elif error.code == 942:
            print('Table does not exists' + queryString)
        else:
            print(error.code)
            print(error.message)
            print(error.context)
        c.close()
    return c

def dbExecuteQuery(conn, queryString):
    c = conn.cursor()
    c.execute(queryString)
    return c
    rowcount=0
    for row in c:
        print (row)
        #print (row[0], "-", row[1])
        rowcount = rowcount + 1
        if rowcount == 5:
            break

def dbExecuteQuerySingle(conn, queryString):
    c = conn.cursor()
    print('queryString', queryString)
    try:
        c.execute(queryString)
        row = c.fetchone()
        return row[0]
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 955:
            print('Object already exists' + queryString)
        elif error.code == 1031:
            print("Insufficient privileges - are you sure you're using the owner account?")
        elif error.code == 942:
            print('Table does not exists' + queryString)
        else:
            print(error.code)
            print(error.message)
            print(error.context)
        c.close()
    return c

def dbExecuteQueryList(conn, queryString):
    print('queryString', queryString)
    c = conn.cursor()
    try:
        c.execute(queryString)
        responseList = ([])
        for row in c:
            responseList.append(row[0])
        return responseList
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 955:
            print('Object already exists' + queryString)
        elif error.code == 1031:
            print("Insufficient privileges - are you sure you're using the owner account?")
        elif error.code == 942:
            print('Table does not exists' + queryString)
        else:
            print(error.code)
            print(error.message)
            print(error.context)
            c.close()
        return 

def dbClose(conn):    
    conn.close()

def fillField(browser, fieldId, inputText):
    browser.find_element_by_id(fieldId).send_keys(inputText)
    
def fillField(browser, fieldName, inputText):
    browser.find_element_by_name("totalregisteredusers").send_keys('137')


############# MAIN

if __name__ == "__main__":
    print( 'Usage: ACTDataStewardMetric.py yyyy mm')
    print( 'Start Time')
    print(time.strftime("%c"))
    print( 'Number of arguments:', len(sys.argv), 'arguments.')
    print( 'Argument List:', str(sys.argv))
    metricYear = int(sys.argv[1])
    metricMonth = int(sys.argv[2])
    browser = webdriver.Chrome()
    #user = getpass.getuser() 
    #pwd = getpass.getpass(prompt='Password:') 
    lastDayOfMonth = calendar.monthrange(metricYear,metricMonth)[1]
    monthName = calendar.month_name[metricMonth]
    firstMonthDay = str(metricMonth) + '/01/' + str(metricYear)
    lastMonthDay = str(metricMonth) + '/' + str(calendar.monthrange(metricYear,metricMonth)[1]) + '/' + str(metricYear)

    # Connect to database - This assumes the login has read access to
    # both the i2b2 PM and SHRINE DATASTWARD schema
    # conn_prod = dbOracleConnect(conn_str_prod01.safe_substitute(USERNAME=pmUserName, PASSWORD=pmPassword))
    conn_prod = dbOracleConnect(conn_str_prod01)
    registeredUsers = dbExecuteQuerySingle(conn_prod,
                                           registeredUsersSQL.safe_substitute(
                                               DB_SCHEMA=pmSchema,
                                               FIRST_MONTH_DAY=firstMonthDay,
                                               LAST_MONTH_DAY=lastMonthDay,
                                               MILLISEC_IN_DAY=millisecondsInDay))
    print('registeredUsers',registeredUsers)
    newRegisteredUsers = dbExecuteQuerySingle(conn_prod,
                                           newRegisteredUsersSQL.safe_substitute(
                                               DB_SCHEMA=pmSchema,
                                               FIRST_MONTH_DAY=firstMonthDay,
                                               METRIC_YEAR=metricYear,
                                               METRIC_MONTH=monthName,
                                               LAST_MONTH_DAY=lastMonthDay,
                                               MILLISEC_IN_DAY=millisecondsInDay))
    print('newRegisteredUsers',newRegisteredUsers)
    
    totalQueriesResponse = dbExecuteQuerySingle(conn_prod,
                                           totalQueriesSQL.safe_substitute(
                                               DB_SCHEMA=dataStewardSchema,
                                               FIRST_MONTH_DAY=firstMonthDay,
                                               LAST_MONTH_DAY=lastMonthDay,
                                               MILLISEC_IN_DAY=millisecondsInDay))
    print('totalQueriesResponse',totalQueriesResponse)
    
    queryTopicsResponse = dbExecuteQueryList(conn_prod,
                                           queryTopicsSQL.safe_substitute(
                                               DB_SCHEMA=dataStewardSchema,
                                               FIRST_MONTH_DAY=firstMonthDay,
                                               LAST_MONTH_DAY=lastMonthDay,
                                               MILLISEC_IN_DAY=millisecondsInDay))
    print('queryTopicsResponse',queryTopicsResponse);
    newQueriers = dbExecuteQuerySingle(conn_prod,
                                           newQueriersSQL.safe_substitute(
                                               DB_SCHEMA=dataStewardSchema,
                                               FIRST_MONTH_DAY=firstMonthDay,
                                               LAST_MONTH_DAY=lastMonthDay,
                                               MILLISEC_IN_DAY=millisecondsInDay))
    print('newQueriers',newQueriers);

    browser.implicitly_wait(10) # seconds
    browser.get('https://www.ctsiredcap.pitt.edu/redcap/surveys/?s=JPTYEE8AEP')
    browser.find_element_by_id("rc-ac-input_institution").send_keys(site)
    browser.find_element_by_id("rc-ac-input_month").send_keys(monthName)
    browser.find_element_by_name("totalregisteredusers").send_keys(registeredUsers)
    browser.find_element_by_name("newregisteredusers").send_keys(newRegisteredUsers)
    browser.find_element_by_name("totalqueries").send_keys(totalQueriesResponse)
    browser.find_element_by_name("querytopics").send_keys(', '.join(queryTopicsResponse))
    browser.find_element_by_name("firsttimeusers").send_keys(newQueriers)

#browser.quit()

