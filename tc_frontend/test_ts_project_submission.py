from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def test_scenario_1():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
    navigated_url = driver.current_url
    assert navigated_url.find("simple-form-demo") > 0
    txt_message = "Welcome to LambdaTest"
    driver.find_element(By.ID, "user-message").send_keys(txt_message)
    driver.find_element(By.ID, "showInput").click()
    txt_displayed = driver.find_element(By.ID, "message").text
    assert txt_displayed == txt_message


def test_scenario_3():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
    navigated_url = driver.current_url
    assert navigated_url.find("input-form-demo") > 0
    driver.find_element(By.NAME, "name").send_keys("Test")
    driver.find_element(By.NAME, "email").send_keys("Test")
    driver.find_element(By.NAME, "password").send_keys("Test")
    driver.find_element(By.NAME, "company").send_keys("Test")
    driver.find_element(By.NAME, "website").send_keys("Test")
    select = Select(driver.find_element(By.NAME, "country"))
    select.select_by_visible_text
    driver.find_element(By.ID, "city").send_keys("Test")
    driver.find_element(By.NAME, "address_line1").send_keys("Test")
    driver.find_element(By.NAME, "address_line2").send_keys("Test")
    driver.find_element(By.ID, "inputState").send_keys("Test")
    driver.find_element(By.NAME, "zip").send_keys("Test")
