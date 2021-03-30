from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get("https://qasvus.wordpress.com/")
        driver_chrome.maximize_window()
        driver_chrome.implicitly_wait(3)
        self.assertIn("California Real Estate", driver_chrome.title)
        print('Page has', driver_chrome.title + 'as Page title')
        driver_chrome.implicitly_wait(3)
        popup = driver_chrome.find_element_by_xpath('//*[@value="Close and accept"]')
        if popup:
            popup.click()

        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        print(driver_chrome.title)
        print(driver_chrome.current_url)
        driver_chrome.find_element(By.ID, "g2-name").clear()
        driver_chrome.find_element(By.ID, "g2-name").send_keys('OLGA')
        driver_chrome.find_element(By.NAME, "g2-email").clear()
        driver_chrome.find_element(By.NAME, "g2-email").send_keys('olgaroeva24@gmail.com')
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").clear()
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys('test')
        submit = driver_chrome.find_element_by_xpath("//button[contains(text(),'Submit')]")
        body = driver_chrome.find_element_by_xpath("//div[@id='page']")

        if submit:
            submit.click()
        elif driver_chrome.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        time.sleep(3)
        driver_chrome.execute_script("window.scrollTo(0, 2600)")
        time.sleep(15)
        try:
            driver_chrome.find_element_by_link_text("go back").click()
        except NoSuchElementException:
            driver_chrome.body.send_keys(Keys.PAGE_UP)
            driver_chrome.find_element_by_xpath(By.LINK_TEXT, "go back").click()

        wait = WebDriverWait(driver_chrome, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        time.sleep(3)

    def test_search_1120x850(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 850)
        driver_chrome.get("https://qasvus.wordpress.com/")
        driver_chrome.implicitly_wait(3)
        self.assertIn("California Real Estate", driver_chrome.title)
        print('Page has', driver_chrome.title + 'as Page title')
        driver_chrome.implicitly_wait(3)
        popup = driver_chrome.find_element_by_xpath('//*[@value="Close and accept"]')
        if popup:
            popup.click()

        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        print(driver_chrome.title)
        print(driver_chrome.current_url)
        driver_chrome.find_element(By.ID, "g2-name").clear()
        driver_chrome.find_element(By.ID, "g2-name").send_keys('OLGA')
        driver_chrome.find_element(By.NAME, "g2-email").clear()
        driver_chrome.find_element(By.NAME, "g2-email").send_keys('olgaroeva24@gmail.com')
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").clear()
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys('test')
        submit = driver_chrome.find_element_by_xpath("//button[contains(text(),'Submit')]")
        body = driver_chrome.find_element_by_xpath("//div[@id='page']")

        if submit:
            submit.click()
        elif driver_chrome.body.send_keys(Keys.PAGE_DOWN):
            submit.click()
        time.sleep(3)
        driver_chrome.execute_script("window.scrollTo(0, 2600)")
        time.sleep(15)
        try:
            driver_chrome.find_element_by_link_text("go back").click()
        except NoSuchElementException:
            driver_chrome.body.send_keys(Keys.PAGE_UP)
            driver_chrome.find_element_by_xpath(By.LINK_TEXT, "go back").click()

        wait = WebDriverWait(driver_chrome, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        driver.maximize_window()

        driver.implicitly_wait(3)
        self.assertIn("California Real Estate", driver.title)
        print('Page has', driver.title + 'as Page title')
        driver.implicitly_wait(3)
        popup = driver.find_element_by_xpath('//*[@value="Close and accept"]')
        if popup:
            popup.click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        print(driver.title)
        print(driver.current_url)
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-name").send_keys('OLGA')
        driver.find_element(By.NAME, "g2-email").clear()
        driver.find_element(By.NAME, "g2-email").send_keys('olgaroeva24@gmail.com')
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").clear()
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys('test')
        submit = driver.find_element_by_xpath("//button[contains(text(),'Submit')]")
        body = driver.find_element_by_xpath("//div[@id='page']")

        if submit:
            submit.click()
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 2600)")
        time.sleep(15)
        try:
            driver.find_element_by_link_text("go back").click()
        except NoSuchElementException:
            driver.body.send_keys(Keys.PAGE_UP)
            driver.find_element_by_xpath(By.LINK_TEXT, "go back").click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

    def tearDown(self):
        self.driver.quit()