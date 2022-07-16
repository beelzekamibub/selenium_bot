from selenium import webdriver
import time
from booking.booking import Booking
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #bot.change_currency('INR')
    bot.select_place_to_go('new york')
    bot.select_date('2022-08-10','2022-08-15')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filterations()

