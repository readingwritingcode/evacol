#! /usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Automatización del navegador web fireox para recolectar datos desde el
# la plataforma worldcat
# datos de entrada: titulo material bibliografico
# Author: dave
# End Of Info
# # # # # # # # # #  # # # # # # # # # # # # #  # # # #  # # # # # # # # #
import sys
import time
import Levenshtein as lv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options



#ops=Options()
#ops.set_headless()

title='Física : campos y ondas. v.2. Marcelo Alonso'

driver=webdriver.Firefox(executable_path='geckodriver')
driver.get('https://www.worldcat.org/')

cook=driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
cook.click()
time.sleep(1)
search=driver.find_element(By.XPATH, '//*[@id="q1"]')
search.clear()
search.send_keys(title)
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/div/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input').click()
time.sleep(2)
tr=driver.find_elements(By.XPATH,'//form/table/tbody/tr/td[4]/div[3]/a')
lt=[]
for i in tr:
    lt.append(i.text.replace('́',''))
    print(i.text.replace('́',''))
    print("calculating match")

time.sleep(1)
lvtr=[]
lti=[]
for j in lt:
    jt=j.replace('.','').replace(' ','').replace(':','').lower()
    print(jt,'----',tw,'---',lv.ratio(jt,tw))
    if lv.ratio(tw,jt) >= 0.75:
        lti.append(j)
        
    lvtr.append(lv.ratio(tw,jt))
lvm=max(lvtr)
print(lt[lvtr.index(lvm)],lvtr.index(lvm))

edr=driver.find_element('path to element')

time.sleep(1)
print("select best match")
lvm=max(lvtr)
print('\n')


    
# click button search
# select format
# select idioms
# iterate over results
#   '//form/table/tbody/tr[i(1-10)]/td[4]/div[3]/a/strong/text()').map(x => x.wholeText)
# deside which of result is
#   compare term by term
#
#     algorith v1.
#     tw=title.split
##    lt=list_title_results
##
##    idx=[]
##    for j in lt:
##        s=0
##        for i in range(len(tw)):
##            if tw[i] in j:
##                s+=1
##        if s == len(tw):
##            idx.append(lt.index(j))
# click in editions
#    $x('//table/tbody/tr/td[i(1-10)]/div[2]/form/table/tbody/tr[4]/td[4]/ul/li/a')
# get data editions:
#   ed=driver.find_elements(scrapbooks.By.XPATH,'//table[@class="table-results"]/tbody//td[7]')
#   '''
#   for i in ed:
#       store(i.text)
#   '''
##
##tw=title.split
##lt=list_title_results
##
##idx=[]
##for j in lt:
##    s=0
##    for i in range(len(tw)):
##        if tw[i] in j:
##            s+=1
##    if s == len(tw):
##        idx.append(lt.index(j))
##
