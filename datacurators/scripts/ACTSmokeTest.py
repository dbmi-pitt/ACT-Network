from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import re


ontologyElement = {}

def runQuery(browser):
#    runOk = browser.find_element(By.ID, "yui-gen5-button")
    runOk = browser.find_element(By.ID, "yui-gen9-button")
    runOk.click()

def pickQueryType(browser, queryTypeList):
    runQuery = browser.find_element(By.ID, "runBox")
    runQuery.click()

    if len(queryTypeList) > 0:
        for queryType in queryTypeList:
            print (queryType)
            currentDivElement = browser.find_element(By.ID, queryType)
            print (currentDivElement.get_attribute('value'))
            currentElement = currentDivElement.find_element(By.TAG_NAME, 'input')
            print (currentElement.get_attribute('value'))
            currentElement.click()


# Open each of the Ontology tree nodes until you get to the desired element
def traverseOntology(browser, nodeStrings):
    global currentElement
    nodeCnt = 0
    for currentNode in nodeStrings:
        print ('Current Node: ' , currentNode)
        #Find all the visible concepts
        '''
        try:
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sdxDefaultCONCPT")))
                #EC.presence_of_element_located((By.ID, "myDynamicElement")))
        finally:
            print('Still not visible')
        '''
            
        sdxConcepts = browser.find_elements(By.CLASS_NAME, "sdxDefaultCONCPT")

        #Add them to a dictionary
        print('Add more nodes...');
        for sdxConcept in sdxConcepts:
            print("sdxConcepts: %s" % sdxConcept.text)
            ontologyElement[sdxConcept.text] = sdxConcept
        #Find the concept that corresponds to your 1st click open it
        print('Open...', currentNode)
        currentElement = ontologyElement[currentNode]
        if ( nodeCnt < len(nodeStrings)):
            currentElement.click()
        nodeCnt = nodeCnt + 1
        time.sleep(5) #webdriver wait does not seem to be working
    #return the last element
    return currentElement


# Open each of the Ontology tree nodes until you get to the desired element
def findValueByExclusion(browser):
    global currentElement
    elementCnt = 0
    tagElements = browser.find_elements(By.TAG_NAME, "tr")
    
    #Add them to a dictionary
    print('Add more nodes...');
    for tagElement in tagElements:
        print("tagElement Text: %s" % tagElement.text)
'''
        ontologyElement[sdxConcept.text] = sdxConcept
        #Find the concept that corresponds to your 1st click open it
        print('Open...', currentNode)
        currentElement = ontologyElement[currentNode]
        if ( nodeCnt < len(nodeStrings)):
            currentElement.click()
        nodeCnt = nodeCnt + 1
        time.sleep(5) #webdriver wait does not seem to be working
    #return the last element
    return currentElement
'''


# Find the first numerical text
def findValueByNumberOnly(browser, tag_name):
    global currentElement
    elementCnt = 0
    tagElements = browser.find_elements(By.TAG_NAME, tag_name)
    
    #Add them to a dictionary
    print('Add more nodes...');
    for tagElement in tagElements:
        print("tagElement Text: %s" % tagElement.text)
        if tagElement.text.isnumeric() == True:
            return int(tagElement.text)
    return -1

# use regular expression on innerhtml to find what you are looking for
# This is used because the use of ids and tags is pretty inconsistent
# in the interface
def findValuesByRegularExpression(browser, regExpressions):
    #print ('Element: ' , browser.get_attribute('innerHTML'))
    theText = browser.get_attribute('innerHTML')
    for regExpression in regExpressions:
        print ('Reg Ex: ' ,regExpression)
        value = findValueByRegularExpression(theText, regExpression, 1)
        print ('Value: ' , value)


def findValueByRegularExpression(theText, regularExpression, matchGroup):
    #print ('Element: ' , browser.get_attribute('innerHTML'))
    #print ('Reg Ex: ' ,regularExpression) 
    match = re.search(regularExpression, theText )
    if match:
        print('Match: ', match.group(matchGroup))
        return match.group(matchGroup)
    return -1 #NO MATCH

'''
    #Add them to a dictionary
    print('Add more nodes...');
    for tagElement in tagElements:
        print("tagElement Text: %s" % tagElement.getElementName())
        match = re.search(regularExpression, tagElement.getText())
        if match:
            print('Match: ', tagElement.text)
    return -1
'''


browser = webdriver.Chrome()
browser.implicitly_wait(10) # seconds
#browser.get('https://i2b2.act.pitt.edu/webclient/')
browser.get('https://dbmi-ncats-test02.dbmi.pitt.edu/webclient/')
print("Done waiting")
browser.find_element_by_id("loginusr").send_keys(Keys.CONTROL, "a")
browser.find_element_by_id("loginusr").send_keys('username')
browser.find_element_by_id("loginpass").send_keys(Keys.CONTROL, "a")
browser.find_element_by_id("loginpass").send_keys('passwd'+ Keys.RETURN)
nodeStrings = ['ACT Demographics','Race','Asian']
time.sleep(5)

#Drag term to panel
currentNode = traverseOntology(browser, nodeStrings)
queryPanel1 = browser.find_element(By.ID, "QPD1")
ActionChains(browser).drag_and_drop(currentNode, queryPanel1).perform()


#infoQueryStatusText
#Number of patients for 'query name'
#patient_count:

# Select Query Topic
#queryTopicSelect = Select(browser.find_element(By.ID, "queryTopicSelect"))
#queryTopicSelect.select_by_visible_text("Test Pitt Query")

#Run query popup
'''value PATIENT_GENDER_COUNT_XML id crcDlgResultOutputPATIENT_GENDER_COUNT_XML 
PATIENT_VITALSTATUS_COUNT_XML
PATIENT_RACE_COUNT_XML
PATIENT_AGE_COUNT_XML
'''
queryTypeList = ['crcDlgResultOutputPATIENT_GENDER_COUNT_XML',
                 'crcDlgResultOutputPATIENT_VITALSTATUS_COUNT_XML',
                 'crcDlgResultOutputPATIENT_RACE_COUNT_XML',
                 'crcDlgResultOutputPATIENT_AGE_COUNT_XML']
pickQueryType(browser, queryTypeList)


#Name Query
runQuery(browser)


# try to find the answer
time.sleep(60)
answer = browser.find_element(By.ID, "chart0")
print(answer.find_element_by_tag_name("tr").text)
findValueByExclusion(answer)
answerNumber = findValueByNumberOnly(answer, 'tr')
print('Query Result',answerNumber)
showQueryStatus = browser.find_element(By.ID, "infoQueryStatusText")
#print('showQueryStatus: ', showQueryStatus.get_attribute('innerHTML'))
#endDateMillsecElem = browser.find_element(By.ID, "endDateMillsecElem")
#print('endDateMillsecElem: ', endDateMillsecElem.get_attribute('innerHTML'))

time.sleep(60)
#findValueByRegularExpression(showQueryStatus, 'div', 'Compute Time: (\w*)')
regExprs = ('Compute Time: (\w*)','patient_count: <font color=\"#0000dd\">(\d*)')
findValuesByRegularExpression(showQueryStatus, regExprs)


'''
#drop Asian on 1st query panel
asian = ontologyElement['Asian']
queryPanel1 = browser.find_element(By.ID, "QPD1")
ActionChains(browser).drag_and_drop(asian, queryPanel1).perform()

# Select Query Topic
queryTopicSelect = Select(browser.find_element(By.ID, "queryTopicSelect"))
queryTopicSelect.select_by_visible_text("Test Pitt Query")

#Run query
runQuery = browser.find_element(By.ID, "runBox")
runQuery.click()
#runOk = browser.find_element(By.ID, "yui-gen5-button")
runOk = browser.find_element(By.ID, "yui-gen9-button")
runOk.click()
'''
# Run Query


    
#    sdxConcept.click()
#demographics = browser.find_element(By.ID, "ONT_TID-1")
#demographics.click()
#race = browser.find_element(By.ID, "ONT_TID-99")
#race.click()
#asian = browser.find_element(By.ID, "ONT_TID-103")




#ActionChains(browser).drag_and_drop(asian, queryPanel1).perform()



#for sdxConcept in sdxConcepts:
#    print("Value is: %s" % sdxConcept.get_attribute("value"))
#    sdxConcept.click()
'''
WebElement element = browser.findElement(By.name("source"));
WebElement target = browser.findElement(By.name("target"));

(new Actions(browser)).dragAndDrop(element, target).perform();
'''

'''    
browser.find_element_by_name('loginForm').send_keys('test')

browser.switch_to.frame('_yuiResizeMonitor')
browser.find_element_by_id('loginusr').send_keys('test')

browser.find_element_by_class_name("input")
browser.find_element_by_id("loginusr").send_keys('username')
browser.find_element_by_id ('ID').send_keys('password')
browser.find_element_by_id('submit').click()


elem = browser.findElement(By.id("uname"));
#elem = browser.find_element_by_name('uname')  # Login
elem.send_keys('username' + Keys.RETURN)
elem = browser.find_element_by_name('input#loginpass')  # Login
elem.send_keys('password' + Keys.RETURN)
elem = browser.find_element_by_name('input')  # Login
elem.send_keys(Keys.RETURN)
'''
#browser.quit()
'''
male
250 icd9
e13 icd10
36 icd9p
03 icd10p
1012974 cpt
va med 161 acetam
loinc 2345-7
visit 2 days
inc e13 exc 250
01/01/2014 e08-e13 exclude 250 no date
male all breakdowns
retired 71010
'''

''' Make Methods
 Read in json that describes the test
--select
--breakdown
--set date
--set exclude
--add to more that one panel
--login
'''
