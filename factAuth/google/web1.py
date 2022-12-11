from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
url = "https://toshithh.github.io"
driver.get(url)

el = driver.find_element('id', "about")
#in devtools you can see the elements x,y and compare to:
print("location:", el.location)
print("size", el.size)

#you can just now say el.click() but if you must move:
action = ActionChains(driver)
action.move_to_element(el) 
action.click()
action.perform()