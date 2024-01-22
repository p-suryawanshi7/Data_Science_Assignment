#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import csv
import logging


# In[ ]:


def get_linkedin_data(first_name, last_name, access_token):
    try:
        url = f"https://api.linkedin.com/v2/people/(first_name:{first_name},last_name:{last_name})"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error("Error occurred in API call", exc_info=True)
        return None

def save_to_csv(data, file_path):
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def main():
    access_token = "YOUR_ACCESS_TOKEN"
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    data = get_linkedin_data(first_name, last_name, access_token)
    if data:
        print(data)

if __name__ == "__main__":
    main()

save_to_csv(user_data, "linkedin_data.csv")


# In[ ]:


get_ipython().system('pip install Selenium')


# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


# In[ ]:


def get_linkedin_data_browser(first_name, last_name):
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/")
    time.sleep(2)


    search_box = driver.find_element("name", "search")
    search_box.send_keys(f"{first_name} {last_name}")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    users_data = []
    search_results = driver.find_elements_by_css_selector(".search-result__info")
    for result in search_results[:10]:
        user_data = get_user_details_browser(result)
        users_data.append(user_data)

    driver.quit()
    return users_data[:5]

def get_user_details_browser(result):
    full_name = result.find_element_by_css_selector(".actor-name").text
    headline = result.find_element_by_css_selector(".subline-level-1").text
    location = result.find_element_by_css_selector(".subline-level-2").text

    return {"Full Name": full_name, "Headline": headline, "Location": location}

def save_to_csv(data, file_path):
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    first_name = input("Enter user's first name: ")
    last_name = input("Enter user's last name: ")

    user_data = get_linkedin_data_browser(first_name, last_name)

    save_to_csv(user_data, "linkedin_data_browser.csv")


# In[ ]:




