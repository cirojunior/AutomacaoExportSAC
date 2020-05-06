'''
Utilizando o Python para automatizar um export de relatório do SAP Analytics Cloud.
'''
import login
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

usuario = login.usuarios()
senha = login.senha()
url = login.url()

#executando webdriver e abrindo o site
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#Passando usuário
element = driver.find_element_by_id("i0116")
element.send_keys(usuario)
driver.find_element_by_id("idSIButton9").click()

#Passando senha
time.sleep(2)
element = driver.find_element_by_id("i0118")
element.send_keys(senha)
driver.find_element_by_id("idSIButton9").submit()

#confirmando acesso
time.sleep(1)
driver.find_element_by_id("idSIButton9").submit()

#Opções do input control no SAC 
lista_inputControl = ['Jose','Joao','Julio']

#desmarcando todos os checkbox
time.sleep(5)
for x in lista_inputControl:
    driver.find_element_by_xpath(".//*[contains(text(),'"+x+"')]").click()


#marcando o primeiro checkbox
time.sleep(10)
for x in lista_inputControl:
    driver.find_element_by_xpath(".//*[contains(text(),'"+x+"')]").click()
    driver.find_element_by_xpath("//div[contains(@class, 'sapEpmToolbarElement sapEpmToolbarItem sapEpmUiPageTipEnabled')]").click()
    driver.find_element_by_xpath(".//*[contains(text(),'Export...')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(@class, 'sapEpmUiDialogButton sapEpmUiDialogOkButton sapMBarChild sapMBtn sapMBtnBase sapMBtnInverted')]").click()
    time.sleep(10)
    os.rename("/home/ti/Downloads/SAC+Python.pdf", "/home/ti/Downloads/SAC+Python "+x+".pdf")
    driver.find_element_by_xpath(".//*[contains(text(),'"+x+"')]").click()

driver.close()