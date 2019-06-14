from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools as it
import time as t

symbs = '`1234567890-=\][\';/.,?><":}{+_)(*&^%$#@!'
alpha = 'abcdefghijklmnopqrstuvwxyz'

charSet = alpha + alpha.upper() + symbs

##charSet = '0123456789'

x = int(input('Reps: '))


##Must use chrome as of now, sorry!
def selSetup(driverType='chrome', driverPath='chromedriver.exe', \
             url=None):
    if driver == 'chrome':
    driver = webdriver.Chrome(driverPath)
    driver.get(url)
    return driver

def idFeilds(userID='Username', passID='Password', subID='Submit' \
             userClass=None, passClass=None, subClass=None, driver):
    if userID is not None and passID is not None:
        uFeild = driver.find_element_by_id(userID)
        pFeild = driver.find_element_by_id(userID)
    elif userClass is None and passClass is None:
        print('you need to enter some values...')
    else:
        uFeild = driver.find_element_by_class(userClass)
        pFeild = driver.find_element_by_class(passClass)
    
    return uFeild, pFeild

def sendData(username, password, uFeild, pFeild):
    uFeild.send_keys(username)
    pFeild.send_keys(password)
    


def iterate(charSet, x):
    spam = it.product(charSet, repeat=x)

    comboTotal = str(len(charSet) ** x)
    counter = 0

    global startTime
    startTime = t.time()
    for i in spam:
        i = ''.join(map(str,i))
        print('Testing Combo ' + str(counter) + \
              ' of ' + comboTotal + ' | [' + i + ']')
        counter += 1
    global endTime
    endTime = t.time()

##iterate(charSet, x)
print('Done!')
eTS = round((endTime - startTime), 6)
eTM = round(((endTime - startTime)/60), 6)
eTH = round((((endTime - startTime)/60)/60), 6)

print('Elapsed Time: \nSec: ' + str(eTS) + '\nMin: ' + str(eTM) + \
      '\nHrs: ' + str(eTH))
