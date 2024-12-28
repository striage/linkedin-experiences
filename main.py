import sys

from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = sys.argv[1]
password = sys.argv[2]
url = sys.argv[3]
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person(url, driver=driver)

experiences = person.experiences

print(person.name)
for experience in experiences:
    output_str = "- "
    output_str += experience.duration
    output_str += " as "
    output_str += experience.position_title
    output_str += " @ "
    output_str += experience.institution_name
    print(output_str)