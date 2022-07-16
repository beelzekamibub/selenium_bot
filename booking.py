from selenium import webdriver
import booking.constants as const
import time
import os
import booking.BookingFilterations as bf
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Program Files (x86)\chromedriver.exe",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown;
        #os.environ['PATH']+=self.driver_path
        self.path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(self.path)
        #super(Booking,self).__init__()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.teardown:
            self.driver.quit()

    def change_currency(self,currency=None):
        currency_menu=self.driver.find_element(
            By.CSS_SELECTOR, "button[data-tooltip-text='Choose your currency']"
        )
        currency_menu.click()
        #*= allows to look substring
        curr=f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        self.driver.find_element(By.CSS_SELECTOR,curr).click()

    def select_place_to_go(self,place):
        search_box=self.driver.find_element(By.ID,"ss")
        search_box.clear()
        search_box.send_keys(place)
        first_result=self.driver.find_element(By.CSS_SELECTOR,'li[data-i="0"]')
        first_result.click()

    def select_date(self,check_in,check_out):
        check_in_element=self.driver.find_element(By.CSS_SELECTOR,f'td[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element=self.driver.find_element(By.CSS_SELECTOR,f'td[data-date="{check_out}"]')
        check_out_element.click()

    def select_adults(self,count=1):
        selection_element=self.driver.find_element(By.CSS_SELECTOR,'label#xp__guests__toggle.xp__input')
        selection_element.click()
        while True:
            decrease=self.driver.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease.click()
            val_element=self.driver.find_element(By.ID,"group_adults")
            if int(val_element.get_attribute('value'))==1:
                break

        increase=self.driver.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(count-1):
            increase.click()

    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    def apply_filterations(self):
        filter=bf.BookingFilterations(self.driver)
        filter.apply_star_rating(3)
        time.sleep(2)
        filter.sort_low()
