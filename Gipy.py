import sys
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common import keys
#_____________________________________PREQUEST_________________________________#
PATH = "C:\Program Files (x86)\chromedriver.exe"
project_folder = "C:\\Users\Devesh\Documents\Projects"  
#______________________________________________________________________________#
username = sys.argv[1]
password = sys.argv[2]
reponame = sys.argv[3]
def webpy():
    subprocess.Popen(['init.bat',project_folder,reponame],shell=True)
    
    # browser things #
    # initials
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.github.com")
    # signed in button click
    driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()
    # entering  username & password
    driver.find_element_by_css_selector("#login_field").send_keys(username)
    driver.find_element_by_css_selector("#password").send_keys(password)
    #loging in
    driver.find_element_by_css_selector("#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block").click()
    #logged in
    #creating New repository
    driver.get("https://www.github.com/new")
    driver.find_element_by_css_selector("#repository_name").send_keys(reponame)
    time.sleep(2)
    driver.find_element_by_css_selector("#new_repository > div.js-with-permission-fields > button").click() 
    #repo created

    subprocess.Popen(['end.bat',project_folder,reponame,username],shell=True)

if __name__ == "__main__":
    webpy()




