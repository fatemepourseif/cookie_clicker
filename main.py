from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

timeout = time.time() + 5
five_min = time.time() + 60 * 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

wait = WebDriverWait(driver, 15)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > timeout:
        timeout = time.time() + 5

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = ids[n]

        current_money = driver.find_element(By.ID, "money").text
        if "," in current_money:
            current_money = current_money.replace(",", "")
        count_cookie = int(current_money)

        affordable_elements = {}
        for key, value in cookie_upgrades.items():
            if count_cookie >= key:
                affordable_elements[key] = value

        if affordable_elements:
            highest_price_affordable_upgrade = max(affordable_elements)
            to_purchase_id = affordable_elements[highest_price_affordable_upgrade]
            driver.find_element(by=By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_sec = driver.find_element(By.ID, value="cps").text
        print(cookie_sec)
        break
