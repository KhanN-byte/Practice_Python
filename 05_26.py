'''
Asynchronous Programming 

'''

import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World')


async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())


'''

Browser Automation and DOM Manipulation

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup the Chrome driver using webdriver-manager
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Open Google
    driver.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Enter search text
    search_box.send_keys("Selenium Python")

    # Simulate hitting the Enter key
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(2)

    # Get the titles of the search results
    titles = driver.find_elements(By.CSS_SELECTOR, 'h3')

    # Print each title
    for title in titles:
        print(title.text)

finally:
    # Close the browser
    driver.quit()


'''

Understanding Classes, Methods, Inheritance __init__() vs super().__init__(), MRO (Method Resolutoon Order)

'''

class Animal():
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def action(self):
        print(f'What animal is it: {self.name}, and whats the type: {self.types}')
class SomeAnimal(Animal):
    def __init__(self, name, types):
        super().__init__(name, types)

    def action(self):
        print(f'This animal is: {self.name}, and whats the type: {self.types}')

Cat = Animal('Fighting Fish', 'Beta Fish')
Cat.action()
Lion = SomeAnimal('African Lion', 'Cat')
Lion.action()


