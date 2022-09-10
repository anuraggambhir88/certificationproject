
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from msedge.selenium_tools import EdgeOptions

import urllib3


user_name = "anuraggambhir88"
app_key = "lUE20LWVFdV2mTd07Y6GMRVM58mr8vxLaBm5C9RFTOArK4gEDX"


# @pytest.fixture(name='global_config_all')
# def project_config(request):
#     driver = webdriver.Chrome(service=ChromeService(
#         ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.set_page_load_timeout(30)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

# @pytest.fixture(name='global_config_all')
# def project_config(request):
#     driver = webdriver.Firefox(
#         executable_path="C:\AutomationCode\geckodriver.exe")
#     driver.maximize_window()
#     driver.set_page_load_timeout(30)
#     request.cls.driver = driver
#     request.cls.browser = "firefox"
#     yield driver
#     driver.quit()


@pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"])
def base_driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.browser_version = "88.0"
        options.platform_name = "Windows 10"

    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.browser_version = "82.0"
        options.platform_name = "Windows 7"

    elif request.param == "MicrosoftEdge":
        options = EdgeOptions()
        options.browser_version = "87.0"
        options.platform_name = "Windows 10"

    lt_options = {}
    lt_options["username"] = "anuraggambhir88"
    lt_options["accessKey"] = "lUE20LWVFdV2mTd07Y6GMRVM58mr8vxLaBm5C9RFTOArK4gEDX"
    lt_options["visual"] = True
    lt_options["video"] = True
    lt_options["network"] = True
    lt_options["build"] = "NewTest"
    lt_options["project"] = "Project"
    lt_options["tunnel"] = False
    lt_options["console"] = "info"
    lt_options["selenium_version"] = "4.0.0"
    lt_options["w3c"] = True
    options.set_capability('LT:Options', lt_options)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + \
        app_key + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    request.cls.driver = driver
    request.cls.browser = request.param

    yield driver
    driver.quit()
