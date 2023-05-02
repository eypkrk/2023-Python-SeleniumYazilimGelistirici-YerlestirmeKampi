from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestHomework:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #driver'ı yükledik
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(5)
        self.userName = self.driver.find_element(By.ID,"user-name")
        self.password = self.driver.find_element(By.ID,"password")
        print(self.userName)
        sleep(2)
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)

    def testLoginAllNull(self):
        self.userName.send_keys("")
        self.userName.send_keys("")
        sleep(2)
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Tüm Alan Boş Sonuç: {testResult}")
    def testLoginPasswordNull(self):
        self.userName.send_keys("eyüp")
        self.password.send_keys("")
        sleep(2)
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Şifre Alanı Boş Sonuç: {testResult}")
        self.userName.clear()
        
    def testLoginLocked(self):
        self.userName.send_keys("locked_out_user") 
        self.password.send_keys("secret_sauce") 
        sleep(2)
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Kilitli Kullanıcı Sonuç: {testResult}")
        self.userName.clear()
        self.password.clear()
     
    def testLoginIcon(self):
        self.userName.send_keys("")
        self.password.send_keys("")
        sleep(2)
        self.loginBtn.click()
        errorIcon = self.driver.find_elements(By.CLASS_NAME,"svg-inline--fa fa-times-circle fa-w-16 error_icon")
        for icon in errorIcon:
            print(f"Test X İcon Görünüyor: {icon.is_enabled()}")
        errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
        sleep(2)
        errorBtn.click()
        for icon in errorIcon:
            print(f"Test X İcon Görünmüyor: {icon.is_displayed()}")

    def testLoginDirect(self):
        self.userName.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        sleep(2)
        self.loginBtn.click()
        getUrl = self.driver.current_url
        print(getUrl)
        testResult = getUrl == "https://www.saucedemo.com/inventory.html"
        print(f"Test Yönlendirilen Site: {testResult}")
    def testLenProduct(self):
        lenProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün Sayısı: {len(lenProduct)}")

testCheck = TestHomework()
testCheck.testLoginAllNull()
testCheck.testLoginPasswordNull()
testCheck.testLoginLocked()
testCheck.testLoginIcon()
testCheck.testLoginDirect()
testCheck.testLenProduct()

while True:
    continue

