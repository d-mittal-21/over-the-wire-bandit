from selenium import webdriver
from selenium.webdriver.commom.keys import keys
driver = webdriver.chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://hello.iitk.ac.in/index.php/user/login")
assert "Hello" in driver.title
elem = driver.find_element_by_name("name")
elem.clear()
elem.send_keys("dmittal21")
elem.send.keys(Keys.Return)
elem= driver.find_element_by_name("pass")
elem.clear()
elem.send_keys("Visoshdi@123")
elem.send.keys(Keys.Return)
