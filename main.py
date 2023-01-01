import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/IT School Lenovo/Desktop/Chrome108/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://christiantour.ro/")

driver.maximize_window()

time.sleep(4)

optiuni_meniu = driver.find_elements(By.XPATH,'//*[@id="app"]/div/header/div[4]/div[1]/div/div/div/div/div')
print(len(optiuni_meniu))

#Selectez "Circuite" din meniul principal
for circuite in optiuni_meniu:
    if circuite.text == 'Circuite':
        circuite.click()
        break


#Selectez un circuit;
driver.find_element(By.XPATH, '//*[@id="ctMainMenuCircuits"]/div/div/div/div[2]/div[2]/div[3]/div/div/ul[3]/li[2]/a').click()

time.sleep(4)
#Apas butonul Afiseaza
driver.find_element(By.XPATH,'//*[@id="app"]/div/div/main/div[2]/div/div[1]/div[1]/div/div/div[3]/button/span[2]/span').click()

time.sleep(4)
# Rezerv oferta
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div[3]/a/span[2]/span/span').click()


#Completez datele pentru rezervare:
# Email:
time.sleep(10)
optiuni_formular = driver.find_elements(By.CSS_SELECTOR, 'input[tabindex= "0"]')
print('optiuni_formular', len(optiuni_formular))

for optiune in optiuni_formular:

    # Completez Pasul1 din rezervare: Titularul contractului
    if optiune.get_attribute('aria-label') == 'Email':
        optiune.click()
        optiune.send_keys('tomiirina@yahoo.com')
    if optiune.get_attribute('aria-label') == 'Telefon':
        print('telefon')
        optiune.click()
        optiune.clear()
        optiune.send_keys('0775277377')
    if optiune.get_attribute('aria-label') == 'Prenume':
        print('Prenume')
        optiune.click()
        if optiune.text == '':
           optiune.send_keys('Oana')
    if optiune.get_attribute('aria-label') == 'Nume':
        print('Nume')
        optiune.click()
        optiune.clear()
        optiune.send_keys('Ciolpan')

#Completez Pasul 2 din rezervare: Servicii suplimentare;
driver.find_element(By.XPATH,'//*[@id="app"]/div/div/main/div/div/div[2]/div[5]/div[2]/div/div[1]/div/div[4]/div[1]/div[1]/div/div/div').click()

dropdown= driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div/div[2]/div[6]/div/div[2]/div/div/div[2]/div/div/label[1]/div/div[1]/div/label/div/div/div[1]/div[1]/span')
print('dropdown', dropdown)

#dropdown = Select(driver.find_element(By.CLASS_NAME, 'q-select__focus-target'))
#print('dropdown', dropdown)
#driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/main/div/div/div[2]/div[6]/div/div[2]/div/div/div[2]/div/div/label[1]/div/div[1]/div/label/div/div/div[2]/i').click()

#Selecteaza judet
driver.find_element(By.XPATH,'//*[@id="app"]/div/div/main/div/div/div[2]/div[7]/div/div[2]/div/div/div/label[3]/div/div[1]/div/label/div/div/div[2]/i').click()















#Selectez numarul maxim de copilasi
# driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[3]/label/div/div/div[3]').click()
# numarul_copilasi = driver.find_elements(By.XPATH, '//*[@id="f_f28aa394-71f2-4d79-b98e-aed8f3263043_3"]/div[2]/div')
# print(len(numarul_copilasi))








# First flow
#optiuni = driver.find_elements(By.CLASS_NAME,'q-item__label')

# optiuni = driver.find_elements(By.CSS_SELECTOR,'div[class="q-item__section column q-item__section--main justify-center"] div')
#
# for optiune in optiuni:
#     if optiune.text == 'Circuite':
#         optiune.click()
#         break
#
# print (len(optiuni))
#
# time.sleep(4)
#
# driver.find_element(By.CSS_SELECTOR, 'div[class="q-field__append q-field__marginal row no-wrap items-center q-anchor--skip"] i').click()
# time.sleep(2)
#
# driver.find_element(By.CSS_SELECTOR, 'div[class="q-field__native row items-center"] input').send_keys('Maldive')
# time.sleep(3)
# #destinatii = driver.find_elements(By.CSS_SELECTOR, 'div[class="q-field__native row items-center"] input')
# destinatii = driver.find_elements(By.XPATH, '//*[contains(text(), "Iasi")]')
# print (len(destinatii))
#
# for destinatie in destinatii:
#     if destinatie.text == 'Iasi':
#        print('before destinatie text')
#        destinatie.click()
#     break
#
#
# filtre = driver.find_elements(By.CSS_SELECTOR, 'div[class="q-field__label no-pointer-events absolute ellipsis"]')
# time.sleep(4)
#
# for filtru in filtre:
#     if filtru.text == 'Modalitate de transport':
#         print('este modalitatea de transport')
# #        driver.find_element(By.CSS_SELECTOR, 'div[class="q-field q-validation-component row no-wrap items-start ct-search-field bg-white text-black q-select q-field--auto-height q-select--without-input q-select--without-chips q-select--single q-field--borderless q-field--labeled"] div')
#         driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/label/div/div/div[3]/i').click()
#         time.sleep(3)
        #filtru.click()
        #driver.find_element(By.XPATH, '//*[@id="f_cb8d773a-c492-4a8e-9670-cdb0b17f7d62"]').click()
        #miloace_transport = driver.find_elements(By.XPATH,'//*[@id="f_cb8d773a-c492-4a8e-9670-cdb0b17f7d62"]')
        #miloace_transport = driver.find_elements(By.XPATH, '//*[@id="f_72dd99a6-9a3a-4660-a8de-08a36d87aff5_0"]')
        # print('mijloace de transport:',len(miloace_transport))
        # for mijloc in miloace_transport:
        #     if mijloc.text == 'Avion':
        #         mijloc.click()
        #         break;
        #filtru.click()
        #driver.find_element(By.CSS_SELECTOR,'div[class="q-field__append q-field__marginal row no-wrap items-center q-anchor--skip"] i').click()
        #break
    # if filtru.text == 'Plecare din...':
    #     print ('este plecare din')
    #     driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/label/div/div/div[3]').click()





    # #driver.find_element(By.CSS_SELECTOR, 'div[class="q-item__section column q-item__section--main justify-center"] div').click()
    #
    # print(destinatie.text)
    # print('after destinatie text')
    # if destinatie.text == 'Iasi':
    #     print('destinatie')
    #     destinatie.click()
    #     break
