import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

nav = webdriver.Chrome()

nav.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
nav.find_element('id', 'RESULT_TextField-1').send_keys('Pedro')
nav.find_element('id', 'RESULT_TextField-2').send_keys('Pedro')
nav.find_element('id', 'RESULT_TextField-3').send_keys('999999999')
nav.find_element('id', 'RESULT_TextField-4').send_keys('Brazil')
nav.find_element('id', 'RESULT_TextField-5').send_keys('Fortress')
nav.find_element('id', 'RESULT_TextField-6').send_keys('pedro@hotmail.com.br')
nav.find_element('xpath', '//*[@id="q26"]/table/tbody/tr[1]/td').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[3]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[4]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[5]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[6]/td/label').click()
nav.find_element('xpath', '//*[@id="q15"]/table/tbody/tr[7]/td/label').click()
x = nav.find_element('id', 'RESULT_RadioButton-9')
drop = Select(x)
drop.select_by_visible_text('Afternoon')
nav.find_element('id', 'FSsubmit').click()









