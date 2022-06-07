
#importing libraries
from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class LinkedIn:
    
    def __init__(self,link):
        self.link=link
        

    #This function will login using my credentials into my linkedIn account
    
    def login(self):
        service=Service()
        driver = webdriver.Edge(service=service)   #connecting to me Edge browse
        driver.get(self.link)     #connecting to the LinkedIn login page
        print(self.link)
        print(driver.title)
        username="mohit.snegi97@gmail.com"
        password="Hollyhalston97)"
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_class_name("login__form_action_container ").click()
        driver.find_element_by_id('global-nav-search').click()
        driver.find_element_by_class_name("search-global-typeahead__input always-show-placeholder").send_keys("Ameya Ranade")

    def find_people(self):
        pass



link=LinkedIn("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
link.login()
