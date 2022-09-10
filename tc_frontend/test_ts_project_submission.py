from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Test_Project_Scenario:
    def test_scenario_1(self, base_driver):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        self.driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
        navigated_url = self.driver.current_url
        assert navigated_url.find("simple-form-demo") > 0
        txt_message = "Welcome to LambdaTest"
        self.driver.find_element(By.ID, "user-message").send_keys(txt_message)
        self.driver.find_element(By.ID, "showInput").click()
        txt_displayed = self.driver.find_element(By.ID, "message").text
        assert txt_displayed == txt_message

    def test_scenario_2(self, base_driver):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        self.driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
        slider = self.driver.find_element(
            By.XPATH, "//*[@class='sp__range' and @value='15']")
        ActionChains(self.driver).drag_and_drop_by_offset(
            slider, 120, 0).perform()
        value_slider = slider.get_attribute("value")
        assert value_slider == "95"

    def test_scenario_3(self, base_driver):
        self.driver.get("https://www.lambdatest.com/selenium-playground")
        self.driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        navigated_url = self.driver.current_url
        assert navigated_url.find("input-form-demo") > 0
        self.driver.find_element(
            By.XPATH, "//*[@type='submit' and contains(text(),'Submit')]").click()
        sleep(2)
        ele = self.driver.find_element(By.NAME, "name")
        validation_message = self.driver.execute_script(
            "return arguments[0].validationMessage;", ele)
        assert "Please fill out this field." == validation_message
        self.driver.find_element(By.NAME, "name").send_keys("Test")
        self.driver.find_element(
            By.ID, "inputEmail4").send_keys("Test@test.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "company").send_keys("Test company")
        self.driver.find_element(By.NAME, "website").send_keys("Test.com")
        select = Select(self.driver.find_element(By.NAME, "country"))
        select.select_by_value("US")
        self.driver.find_element(By.ID, "inputCity").send_keys("Test City")
        self.driver.find_element(
            By.NAME, "address_line1").send_keys("123 test")
        self.driver.find_element(By.NAME, "address_line2").send_keys("asd asd")
        self.driver.find_element(By.ID, "inputState").send_keys("Test State")
        self.driver.find_element(By.NAME, "zip").send_keys("121009")
        self.driver.find_element(
            By.XPATH, "//*[@type='submit' and contains(text(),'Submit')]").click()
        sleep(2)
        txt_submit = "Thanks for contacting us, we will get back to you shortly."
        txt_displayed = self.driver.find_element(
            By.XPATH, "//*[contains(@class,'success-msg')]").text
        assert txt_displayed == txt_submit
