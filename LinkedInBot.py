#importing libraries
from lib2to3.pgen2 import driver
import time
from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException

#Main Bot class
class LinkedIn:
    profiles=[]     #Saving the profiles
    
    #constructor
    def __init__(self,link):
        self.link=link
        service=Service()
        options=Options()
        options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(service=service)   #connecting to me Edge browse
        driver.get(self.link)     #connecting to the LinkedIn login page

    #This function will login using my credentials into my linkedIn account
    def login(self):
        service=Service()
        self.driver = webdriver.Chrome(service=service)   #connecting to me Edge browse
        self.driver.get(self.link)     #connecting to the LinkedIn login page
        print(self.link)
        print(self.driver.title)

        #my login credentials
        username="mohit.snegi97@gmail.com"
        password="Hollyhalston97)"

        #logining In
        uname_xpath="//input[@id='username']"
        pass_xpath="//input[@id='password']"
        self.driver.find_element(By.XPATH, uname_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,pass_xpath).send_keys(password)
        # self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@class='btn__primary--large from__button--floating']").click()


        #redirecting to Cengage website
        self.driver.get("https://www.linkedin.com/company/state-street/people/?facetGeoRegion=90000007")
        time.sleep(15)
        get_title=self.driver.title
        
        #calling funtion to find the people profile line on the cengage website 
        profile= self.find_people(BeautifulSoup(self.driver.page_source),self.profiles)
        profile_names=list(set(profile))
        print(len(profile_names))
        print(profile_names)

        self.find_msgbox()

        #this function will send the message to individual profiles
        self.send_message(profile_names)
        

    #Function to find the people profile link on the current website    
    def find_people(self,soup,profiles):
        souper=soup.find('div',class_='scaffold-finite-scroll__content')
        links=souper.findAll('a',class_='ember-view') 
        for link in links:
            profiles.append(link.get('href'))  #appending the profile link to profiles array

        return profiles

    def find_msgbox(self):
        button1=self.driver.find_element_by_class_name("scaffold-finite-scroll__content")
        button=button1.find_elements_by_class_name("artdeco-button__text")
        for l in button:
            l.click()
            time.sleep(10)
            # self.driver.find_element_by_xpath('//div[@class="msg-overlay-bubble-header__controls"]/*[name()="svg"]').click()
            close=self.driver.find_element_by_class_name("msg-overlay-bubble-header__controls")
            closed1=close.find_element_by_css_selector(".msg-overlay-bubble-header__control.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view")
            print(closed1.text)
            closed1.click()
            time.sleep(10)






    def send_message(self,profile_names):
        visited=[]
        while profile_names:
            visited_ID=profile_names.pop()
            visited.append(visited_ID)
            fullLink='http://www.linkedin.com'+visited_ID
            print(fullLink)
            self.driver.get(fullLink)
            time.sleep(10)
            button=self.driver.find_element(by=By.CLASS_NAME,value='pvs-profile-actions ')
            self.driver.implicitly_wait(10)
            ActionChains(self.driver).move_to_element(button).click(button).perform()
            time.sleep(15)
            try:
                self.driver.find_element_by_class_name("artdeco-text-input--input").send_keys("Hello")
            except:
                print("No Message")
            custom_msg="""Hello,

I am sending this message from an automated bot written in Python.

I am currently a Northeastern University student,

I had applied for the Data Analyst intern role from my university portal back in May, Recently I saw the same opening and was wondering if I can interview for the position.

The link for this bot is "https://github.com/Negi97Mohit/LinkedIn.git".

If you wish to connect, my email id is : negi.m@northeastern.edu 

With regards,
Mohit Negi"""



link=LinkedIn("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
link.login()
