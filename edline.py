from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_calender_data():

    username = "andynsmith"
    password = "jazz3"

    driver = webdriver.Chrome('chromedriver')
    driver.get('https://www.edline.net')

    username_input = driver.find_element_by_xpath("/html/body/form[4]/div[1]/div[1]/div/input")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("/html/body/form[4]/div[1]/div[2]/div/input")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    my_edline_button = driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/div[2]/div[1]")
    hover_over = ActionChains(driver).move_to_element(my_edline_button).perform()
    time.sleep(1)

    combined_calender_button = driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/div[2]/div[2]/div/div[2]/ul[1]/li[3]/a")
    combined_calender_button.click()

    time.sleep(100)
    driver.quit()

get_calender_data()
