from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_DemoClass:
    
    #her testten önce çaırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        #klasör oluşturma işlemini yapıyoruz. Exist -> bu klasör varsa oluşturma demek.
        Path(self.folderPath).mkdir(exist_ok=True)
        #günün tarihini al bu tarih ile klasör var mı kontrol et yoksa oluştur
        
    
    #her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()

    # setup -> testdemofunc -> teardown
    def test_demoFunc(self):
        #3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"
    #setup -> testdemo2 -> teardown
    def test_demo2(self):
        assert True
    
    def test_truth_login(self):
        self.waitForElementVisible((By.ID,"user-name"))
        username = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password = self.driver.find_element(By.ID,"password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

    @pytest.mark.skip()  #bunu es geç demek bu anotaition
    #@pytest.mark.parametrize("username,passworD",[("1","1"),("dnm","dnm")])
    #yukarıda ki anatasyon sık kullanılır 2 kullanıcı verisi gönderdik
    def test_invalid_login(self,username,passworD):
        self.waitForElementVisible((By.ID,"user-name"))
        userName = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        password = self.driver.find_element(By.ID,"password")
        userName.send_keys(username)
        password.send_keys(passworD)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
                                    #hangi dosya        #dosyaya verilecek isim
        self.driver.save_screenshot(f"{self.folderPath}/test-ivalid-login-{username}-{passworD}.png")#ekran resmi alır
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    def waitForElementVisible(self,locater,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locater)))
    # GİRİŞ YAPILDIKTAN SONRA LİNK TESTİ
    def test_click_link(self):
        self.test_truth_login()
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"//*[@id='item_4_img_link']/img"),10)
        imgLink = self.driver.find_element(By.XPATH,"//*[@id='item_4_img_link']/img")
        imgLink.click()
        self.waitForElementVisible((By.ID,"back-to-products"),10)
        backLink = self.driver.find_element(By.ID,"back-to-products")
        backLink.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-click-link.png")
    # slider açılır menuden çıkış yapma işlemi
    def test_click_sliderMenu(self):
        self.test_truth_login()
        self.waitForElementVisible((By.ID,"react-burger-menu-btn"))
        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
        self.waitForElementVisible((By.ID,"logout_sidebar_link"))
        logOutBtn = self.driver.find_element(By.ID,"logout_sidebar_link")
        logOutBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-click-sliderMenu.png")
        sleep(2)
        #alışveriş sepetine tıklama ve alışverişe devam etme butonu text kontrolü
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("deneme","123"),("user","password")])
    def test_shoppingCart(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userName = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"user-name"))
        passworD = self.driver.find_element(By.ID,"password")
        userName.send_keys(username)
        passworD.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test.shoppingCart{username}-{password}.png")
        self.waitForElementVisible((By.ID,"shopping_cart_container"))
        shoppingBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        shoppingBtn.click()
        self.waitForElementVisible((By.ID,"continue-shopping"))
        textBtn = self.driver.find_element(By.ID,"continue-shopping")
        assert textBtn.text == "Continue Shopping"
        self.driver.save_screenshot(f"{self.folderPath}/test.shoppingCart{username}-{password}.png")
        sleep(2)
        
        

    