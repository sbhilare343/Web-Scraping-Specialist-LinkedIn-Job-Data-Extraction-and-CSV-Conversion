import time
import re
from selenium import webdriver
# from selenium.common import *
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


class BackendWork:
    def __init__(self):
        self.PATH = "chromedriver path"
        self.LINK = "https://www.linkedin.com/login"
        self.USERID = "userid"
        self.PASSWORD = "password"
        self.t1 = None
        self.t2 = None
        self.t3 = None

    def login(self):
        # Request to the website.
        s = Service(self.PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(self.LINK)
        driver.implicitly_wait(10)

        # Sign in process.
        driver.find_element(By.ID, "username").send_keys(self.USERID)
        driver.find_element(By.ID, "password").send_keys(self.PASSWORD)
        driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
        driver.implicitly_wait(10)
        # time.sleep(90)
        self.perform_search(driver)

    def perform_search(self, driver_new):
        # Dataframe.
        df = pd.DataFrame(columns=["Job Title", "Company", "Link"])
        # Creating soup object.
        page = 25
        counter = 0
        n = 2
        driver_new.get(
            f"https://www.linkedin.com/jobs/search/?currentJobId=3807488043&keywords={self.t1}%20{self.t2}%20{self.t3}"
            f"&origin=SWITCH_SEARCH_VERTICAL")
        while counter < n:
            job_title = []
            job_links = []
            company = []
            driver_new.implicitly_wait(10)
            soup = BeautifulSoup(driver_new.page_source, "html.parser")

            # Job titles.
            tags = soup.find_all("a", class_="disabled ember-view job-card-container__link job-card-list__title")
            time.sleep(5)
            for tag in tags:
                job_title.append(tag["aria-label"])
            # print(job_title)

            # Company name.
            span_tag = soup.find_all("span", class_="job-card-container__primary-description")
            for span in span_tag:
                company.append(span.text.strip())
            # print(company)

            # Job links.
            a_tags_links = soup.find_all(href=re.compile("jobs/view"))
            for a_tag_link in a_tags_links:
                job_links.append("https://www.linkedin.com" + a_tag_link['href'])
            # print(job_links)

            for i in range(len(job_title)):
                row = [job_title[i], company[i], job_links[i]]
                df.loc[len(df)] = row

            # New link.
            new_link = driver_new.current_url + "&start=" + str(page)
            driver_new.get(new_link)
            page += 25
            print(counter)
            counter += 1
            time.sleep(5)
        df.to_csv("Jobs.csv")
        print(df)
