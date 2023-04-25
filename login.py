from behave import *
from selenium import webdriver

@given('I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome(executable_path="/Users/akbar/Downloads/chromedriver_mac_arm64_akbar/chromedriver")


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")
    context.driver.implicitly_wait(10)


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element("name", "username").send_keys(user)
    context.driver.find_element("name", "password").send_keys(pwd)



@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element("xpath", "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()



@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    text = context.driver.find_element("xpath",
                                "//header/div[1]/div[1]/span[1]/h6[1]").text
    assert text=="Dashboard"
    context.driver.close()