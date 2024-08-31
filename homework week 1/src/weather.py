# import libs
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os, time

file_driver = os.path.join("src", "chromedriver.exe")
driver = webdriver.Chrome()

url = ['https://meteostat.net/en/place/vn/thu-uc?s=48900&t=2024-05-01/2024-05-12', 
       'https://meteostat.net/en/place/vn/thu-uc?s=48900&t=2024-05-13/2024-05-24',
       'https://meteostat.net/en/place/vn/thu-uc?s=48900&t=2024-05-25/2024-05-31',
       'https://meteostat.net/en/place/vn/thu-uc?s=48900&t=2024-06-01/2024-06-12']

# Open the website
def open_web(url):
    driver.get(url)
    time.sleep(3)

# Click "accept" button of privacy notice
def click_accept():
    driver.find_element(By.XPATH, '//*[@id="cookieModal"]/div/div/div[3]/button[2]').click()
    time.sleep(1)

    # Click the button with table icon to show details
def show_details():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div[1]/div[1]/button[2]').click()
    time.sleep(2)  # Give it time to load the details table

# Click "show more" button
def show_more():
    for i in range(28):
        try:
            driver.find_element(By.XPATH, '//*[@id="details-modal"]/div/div/div[2]/div[2]/button').click()
            time.sleep(1)
        except Exception:  # if the table is still loading, delay more 2s before clicking the button
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="details-modal"]/div/div/div[2]/div[2]/button').click()
            time.sleep(1)

# Get data
def get_data():
    table = driver.find_element(By.TAG_NAME, 'tbody')
    tr = table.find_elements(By.TAG_NAME, 'tr')
    date = []
    hour = []
    condition = []
    tempt = []
    dew = []
    sunshine = []
    precipitation = []
    snow = []
    wdirect = []
    wspeed = []
    gust = []
    pressure = []
    humidity = []

    for row in tr:
        th = row.find_elements(By.CSS_SELECTOR, 'th')
        td = row.find_elements(By.CSS_SELECTOR, 'td')
        date.append(th[0].text)
        hour.append(th[1].text)
        condition.append(td[0].text)
        tempt.append(td[1].text)
        dew.append(td[2].text)
        sunshine.append(td[3].text)
        precipitation.append(td[4].text)
        snow.append(td[5].text)
        wdirect.append(td[6].text)
        wspeed.append(td[7].text)
        gust.append(td[8].text)
        pressure.append(td[9].text)
        humidity.append(td[10].text)

    data = {
        "Date": date,
        "Hour": hour,
        "Condi": condition,
        "Temp": tempt,
        "Sunsine": sunshine,
        "Dew": dew,
        "preci": precipitation,
        "Snow": snow,
        "wdirect": wdirect,
        "wspeed": wspeed,
        "Gust": gust,
        "Pressure": pressure,
        "Humidity": humidity
    }
    save_to_csv(data)

# create first row of the table
def create_first_row():
    header = {
        "Date": [], "Hour": [], "Condi": [], "Temp": [], "Sunsine": [], "Dew": [], "preci": [], "Snow": [],
        "wdirect": [], "wspeed": [], "Gust": [], "Pressure": [], "Humidity": []
    }
    df1 = pd.DataFrame(header)
    df1.to_csv("homework week 1\Data\weather.csv", index=False)

# save data to file csv
def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("homework week 1\Data\weather.csv", header=False, index=False, mode='a')

# use for 25/5 - 31/5
def show_more2():
    for i in range(16):
        try:
            driver.find_element(By.XPATH, '//*[@id="details-modal"]/div/div/div[2]/div[2]/button').click()
            time.sleep(1)
        except Exception:  # if the table is still loading, delay more 2s before clicking the button
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="details-modal"]/div/div/div[2]/div[2]/button').click()
            time.sleep(1)

if __name__ == "__main__":
    open_web(url[0])
    click_accept()
    show_details()
    show_more()
    create_first_row()
    get_data()

    open_web(url[1])
    click_accept()
    show_details()
    show_more()
    get_data()

    open_web(url[2])
    click_accept()
    show_details()
    show_more2()
    get_data()

    open_web(url[3])
    click_accept()
    show_details()
    show_more()
    get_data()

    driver.close()
