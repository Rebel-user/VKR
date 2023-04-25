from lib2to3.pgen2 import driver

from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="/Users/akbar/Downloads/chromedriver_mac_arm64_akbar/chromedriver")


@when('open orange hrm homepage')
def openHomePage(context):
    #wait = WebDriverWait(driver, 10)
    context.driver.get("https://opensource-demo.orangehrmlive.com")

    context.driver.implicitly_wait(20)


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element("xpath",
                        "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
