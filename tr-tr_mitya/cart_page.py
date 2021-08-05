from selenium import webdriver
from conf.settings import ENTRY_POINT, GECKO_PATH

driver = webdriver.Firefox(GECKO_PATH)
driver.get(ENTRY_POINT)

driver.find_elements_by_css_selector('.header-top .w-choose-city-widget-label').click()
