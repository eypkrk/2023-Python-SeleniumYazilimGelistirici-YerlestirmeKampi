from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
#5
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #hangi şarta kadar bekleyeceğini belirtir.

from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        
        #en fazla 5 saniye kadar olacak şekilde user-name id'li elementin görünmesini bekle
        #located tek parametre istediğinden dolayı parantez içinde parantez yapıp topple tek parametre yaptık
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.ID,"password")
    
        userNameInput.send_keys("1")
        password.send_keys("1")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResult}")
        
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        #action-chains aksiyon zinciri sıra ile çalıştırır
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()#çalıştır
        # userNameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        #js
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(5)
#Action-Chains

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()


#XPATH
#//*[@id="navbar"]/div/div/div/ul/li[3]/a