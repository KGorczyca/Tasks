from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://profil.wp.pl/login.html?zaloguj=poczta')

browser.maximize_window() 
browser.implicitly_wait(20)

emailElem =browser.find_element_by_id('login')
emailElem.send_keys('fikcyjnekontodozadan@wp.pl')

passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('12345678')

passwordElem.submit()
                                      
