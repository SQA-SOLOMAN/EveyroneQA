import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

required_text = "Gold"
link = 'http://suninjuly.github.io/xpath_examples'

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# assignment 1

def go_to_xpath_website():
    browser.get(link)


def first_xpath():
    first = browser.find_element(By.XPATH, '//*[text() = "Gold"]')
    print(first.text)
    assert required_text == first.text, f"The text is {first.text}"


def second_xpath():
    second = browser.find_element(By.XPATH, '//*[contains(text(), "Gold")]')
    print(second.text)
    assert required_text == second.text, f"The text is {second.text}"


def third_xpath():
    third = browser.find_element(By.XPATH, "//div[@style='padding-top: 90px;'] // button[text()='Gold']")
    print(third.text)
    assert required_text == third.text, f"The text is {third.text}"


def fourth_xpath():
    fourth = browser.find_element(By.XPATH, "//div[contains(@style, 'padd')][2] /button[3]")
    print(fourth.text)
    assert required_text == fourth.text, f"The text is {fourth.text}"


def first_css():
    css_s = browser.find_element(By.CSS_SELECTOR, "body.bg-light div:nth-child(2) button:nth-child(3)")
    print(css_s.text)
    assert required_text == css_s.text, f"The text is {css_s.text}"
    browser.close()


go_to_xpath_website()
first_xpath()
second_xpath()
third_xpath()
fourth_xpath()
first_css()

# ------------------
# Assignment 2

new_link = 'http://suninjuly.github.io/cats.html'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def go_to_cats_website():
    driver.get(new_link)




go_to_cats_website()