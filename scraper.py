from selenium import webdriver

def getTasks():
    driver = webdriver.Chrome('C:/Users/michj/Desktop/chromedriver.exe')
    driver.get('https://hopeful-wing-4f2937.netlify.app/')
    driver.implicitly_wait(3)
    taskList = driver.find_elements_by_tag_name('ul')
    return taskList[0].text
