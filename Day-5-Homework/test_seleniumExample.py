from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install()) #eğer driver yolu bulamazsa böyle kullanabiliyoruz
# driver = webdriver.Chrome()
driver.maximize_window()#tam ekran yapar
driver.get("https://www.google.com.tr/?hl=tr")
sleep(5)#sitenin yüklenmesini bekleme için bunu yazdık, eğer yüklenmezse elementi bulamayabilir.
input = driver.find_element(By.ID,"APjFqb")#chrome da ıd si input olanı bul
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)#sitenin yüklenmesini bekleme için bunu yazdık
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()

listOfClasses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde {len(listOfClasses)} adet kurs var.")
# input() hiç kapatmaz
# sleep(10) 10 saniyeaçık kalır
while True:# while döngüsüne parantez koyulmaz
    continue #sonsuz döngü

#HTML LOCATORS


#full XPath
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a

#Xpath
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a

#web scraping
#data scraping