import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import io
import re
from datetime import datetime

#change to your install dir
driver = webdriver.Chrome('D:/001/chromedriver_win32/chromedriver.exe')
driver.get('https://www.bloomberg.com/')
# CL
time.sleep(5)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

root = tk.Tk()
root.withdraw()
text = root.clipboard_get()
#print(text)

dt = datetime.now().strftime('%Y%m%d_%H%M%S')
print(dt)

#save to a file with datetime name
filename = "D:\\001\\" + dt +".txt"
with io.open(filename,'w',encoding='utf8') as f:
    f.write(text)

#with io.open(filename,'r',encoding='utf8') as f:
#    myline = f.read()

#read line by line into list
with io.open(filename,'r',encoding='utf8') as f:
    content = f.readlines()

content = [x.strip() for x in content]

#print(myline)

i=0;
for x in content:
    print(x)
    #handle content line using your logic
    i = i+1

time.sleep(3)

driver.quit()

# THE END
