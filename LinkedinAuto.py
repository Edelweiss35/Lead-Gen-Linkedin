from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException


linkedin_url = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"
email = "edelweiss832@outlook.com"
password = "qwe123QWE!@#"
str_search = "graduate"
country = "United States"

nCnt = 0


EXE_PATH = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')    
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-fullscreen')
driver = webdriver.Chrome(executable_path=EXE_PATH, chrome_options=chrome_options)
driver.get(linkedin_url)
random_delay = random.random()
time.sleep(2 + random_delay)
input = driver.find_element_by_name("session_key")
input.send_keys(email)
random_delay = random.random()
time.sleep(3 + random_delay)
input = driver.find_element_by_name("session_password")
input.send_keys(password)
random_delay = random.random()
time.sleep(random.randint(2,5) + random_delay)
driver.find_element_by_xpath("//button[@type='submit']").click()
random_delay = random.random()
time.sleep(random.randint(3,7) + random_delay)

try:
    driver.find_element_by_xpath("//button[@class='secondary-action']").click()
    random_delay = random.random()
    time.sleep(1 + random_delay)
except NoSuchElementException:
    pass

search = driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']")
search.send_keys(str_search)
random_delay = random.random()
time.sleep(random.randint(2,5) + random_delay)

search_button = driver.find_element_by_xpath("//button[@data-control-name='nav.search_button']").click()
random_delay = random.random()
time.sleep(random.randint(3,7) + random_delay)

search_button = driver.find_element_by_xpath("//button[@aria-label='View only People results']").click()
random_delay = random.random()
time.sleep(random.randint(3,7) + random_delay)

location_button = driver.find_element_by_xpath("//button[@aria-controls='locations-facet-values']").click()
random_delay = random.random()
time.sleep(random.randint(1,3) + random_delay)

location_input = driver.find_element_by_xpath("//input[@placeholder='Add a location']")
location_input.send_keys(country)
random_delay = random.random()
time.sleep(random.randint(1,3) + random_delay)

div_content = driver.find_element_by_xpath("//div[@class='basic-typeahead__triggered-content search-s-add-facet__typeahead-tray']")

location_list = driver.find_elements_by_xpath("//div[@class='basic-typeahead__selectable ember-view']")
location_list[0].click()
random_delay = random.random()
time.sleep(random.randint(1,3) + random_delay)

apply_button_list = driver.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
apply_button_list[1].click()
random_delay = random.random()
time.sleep(random.randint(2,5) + random_delay)

driver.find_element_by_xpath("//div[@class='search-results-container']").click()
random_delay = random.random()
time.sleep(random.randint(2,5) + random_delay)

for i in range(100):
    print(i)
    
    try:
        connect_button_list = driver.find_elements_by_xpath("//button[@data-control-name='srp_profile_actions']")
        random_delay = random.random()
        time.sleep(2 + random_delay)
        if connect_button_list != None:
            for connect_button in connect_button_list:
                if connect_button.text == "Connect":
                    connect_button.click()
                    random_delay = random.random()
                    time.sleep(random.randint(2,10) + random_delay)
                    
                    driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--3 ml1']").click()

                    random_delay = random.random()
                    time.sleep(random.randint(2,10) + random_delay)
                    nCnt = nCnt + 1
                    print('connected people')
                    print(nCnt)
                    if nCnt == 100:
                        break

            str_tmp = "&page=" + str(i + 30)
            print(str_tmp)
            
            if i == 0:
                current_url = driver.current_url + str_tmp
                driver.get(current_url)
                #driver.find_element_by_xpath('//button[@aria-label="'+str_tmp+'"]').click()
                continue

        random_delay = random.random()
        time.sleep(random.randint(2,10) + random_delay)
    except NoSuchElementException:
        if i == 0:
            driver.find_element_by_xpath('//button[@aria-label="'+str_tmp+'"]').click()
            continue
        pass
    except StaleElementReferenceException:
        if i == 0:
            driver.find_element_by_xpath('//button[@aria-label="'+str_tmp+'"]').click()
            continue
        pass
    except ElementClickInterceptedException:
        if i == 0:
            driver.find_element_by_xpath('//button[@aria-label="'+str_tmp+'"]').click()
            continue
        pass
        
    

    current_url = driver.current_url
    page_pos = current_url.find('page=')
    current_page = current_url[page_pos + 5:len(current_url)]
    print('current page------')
    print(current_page)
    old_replace_str = current_url[page_pos:len(current_url)]
    
    new_page = int(current_page, 10) + 1
    if new_page == 100:
        break
    new_replace_str = old_replace_str.replace(current_page, str(new_page))
    new_url = current_url.replace(old_replace_str, new_replace_str)
    print(new_url)
    random_delay = random.random()
    time.sleep(3 + random_delay)
    driver.get(new_url)
    random_delay = random.random()
    time.sleep(3 + random_delay)