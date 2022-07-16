from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import booking.constants as const
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFilterations:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def apply_star_rating(self,rating):
        star_box=self.driver.find_element(
            By.CSS_SELECTOR,"div[data-filters-group='class']"
        )
        star_children=star_box.find_elements(By.CSS_SELECTOR,'*')
        time.sleep(2)
        for star in star_children:
            if str(star.get_attribute('innerHTML')).strip()==f'{rating} stars':
                star.click()

    def sort_low(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,"button[data-testid='sorters-dropdown-trigger']").click()
            self.driver.find_element(By.CSS_SELECTOR,"button[data-id='class_asc']").click()
        except:
            self.driver.find_element(By.CSS_SELECTOR, "li[data-id='price']").click()