
#importing libraries
from lib2to3.pgen2 import driver
import time
from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

class LinkedIn:
    profiles=[]
    def __init__(self,link):
        self.link=link
        service=Service()
        driver = webdriver.Edge(service=service)   #connecting to me Edge browse
        driver.get(self.link)     #connecting to the LinkedIn login page

    #This function will login using my credentials into my linkedIn account
    
    def login(self):
        service=Service()
        self.driver = webdriver.Edge(service=service)   #connecting to me Edge browse
        self.driver.get(self.link)     #connecting to the LinkedIn login page
        print(self.link)
        print(self.driver.title)
        username="mohit.snegi97@gmail.com"
        password="Hollyhalston97)"
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("login__form_action_container ").click()
        self.driver.get("https://www.linkedin.com/company/cengage-learning/people/?keywords=Talent%20Acquisition%20Partner%2Cboston")
        time.sleep(15)
        get_title=self.driver.title
        
        profile= self.find_people(BeautifulSoup(self.driver.page_source),self.profiles)
        profile_names=list(set(profile))
        self.send_message(profile_names)
        
    def find_people(self,soup,profiles):
        id=[]
        souper=soup.find('div',class_='scaffold-finite-scroll__content')
        links=souper.findAll('a',class_='ember-view') 
        for link in links:
            profiles.append(link.get('href'))

        return profiles


    def send_message(self,profile_names):
        visited=[]
        while profile_names:
            visited_ID=profile_names.pop()
            visited.append(visited_ID)
            fullLink='http://www.linkedin.com'+visited_ID
            print(fullLink)
            self.driver.get(fullLink)
            time.sleep(15)
            self.driver.find_element_by_class_name("entry-point").click()
            custom_msg="""Hi,
                          If you are reading this that means my bot worked.
                          Anyways, I am a Northeastern university Student who applied for the data science intern
                          role at your comapny but no reply was there.
                          Recently I saw the same opening and was wondering if I can interview for the role.
                          If you are curious, the link for this bot is: https://github.com/Negi97Mohit/LinkedIn.git
                          and my email is: negi.m@northeastern.edu """



link=LinkedIn("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
link.login()
