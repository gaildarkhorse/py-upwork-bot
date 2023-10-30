import os
import time
import pyautogui
#import pyscreeze
#from pyscreeze import center, grab, pixel, pixelMatchesColor, screenshot
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select as OriginalSelect


class Select(object):
    def __init__(self, element):
        self.element = element
        self.select = OriginalSelect(element)

    def select_by_visible_text(self, text):
        self._wait_for_element_to_be_clickable()
        self.select.select_by_visible_text(text)

    def select_by_value(self, value):
        self._wait_for_element_to_be_clickable()
        self.select.select_by_value(value)

    def select_by_index(self, index):
        self._wait_for_element_to_be_clickable()
        self.select.select_by_index(index)

    def _wait_for_element_to_be_clickable(driver, self):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(self.element))

# Install multiple extensions on a profile
def install_extensions_on_profile( profile_directory, extension_paths ) :
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=" + profile_directory)
    
    unpacked_extension_paths = []
    for extension_path in extension_paths:
        if extension_path.endswith(".crx"):
            crx_extension_path = os.path.abspath(extension_path)
            print(crx_extension_path)
            chrome_options.add_extension(extension_path)
        else:
            unpacked_extension_path = os.path.abspath(extension_path)
            print(unpacked_extension_path)
            unpacked_extension_paths.append(unpacked_extension_path)

    # Join the unpacked extension paths with commas
    unpacked_extensions_argument = ",".join(unpacked_extension_paths)
    chrome_options.add_argument("--load-extension=" + unpacked_extensions_argument)
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    
   
    #extn_btn_location1 = pyautogui.locateOnScreen('Screenshot_1.png')
    #print(extn_btn_location1)
    #btn1_x, btn1_y = pyautogui.center(extn_btn_location1)
    #pyautogui.click(btn1_x, btn1_y)

    #extn_btn_location2 = pyautogui.locateOnScreen('Screenshot_1.png')
    #print(extn_btn_location2)
    #btn2_x, btn2_y = pyautogui.center(extn_btn_location2)
    #pyautogui.click(btn2_x, btn2_y)

    screen_width, screen_height = pyautogui.size()
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

    extn_btn1_loc_width = 176
    extn_btn1_loc_height = 97
    extn_btn2_loc_width = 268
    extn_btn2_loc_height = 304
    extn_btn3_loc_width = 268
    extn_btn3_loc_height = 367
    extn_btn4_loc_width = 268
    extn_btn4_loc_height = 416
    
    # click extension button in menu bar
    click_position1_x = screen_width - extn_btn1_loc_width
    click_position1_y = extn_btn1_loc_height
    #pyautogui.moveTo(click_position1_x, click_position1_y, duration=3)
    pyautogui.click(click_position1_x, click_position1_y)
    print(">>>>>>", click_position1_x, click_position1_y)
    #time.sleep(1)

    # click extenstion inner button (eg: x-block) in popup menu
    click_position2_x = screen_width - extn_btn2_loc_width
    click_position2_y = extn_btn2_loc_height
    #pyautogui.moveTo(click_position2_x, click_position2_y, duration=1)
    pyautogui.click(click_position2_x, click_position2_y)
    print(">>>>>>", click_position2_x, click_position2_y)
    #time.sleep(1)

    # click extenstion inner button (eg: x-block) in popup menu
    click_position3_x = screen_width - extn_btn3_loc_width
    click_position3_y = extn_btn3_loc_height
    #pyautogui.moveTo(click_position3_x, click_position3_y, duration=1)
    pyautogui.click(click_position3_x, click_position3_y)
    print(">>>>>>", click_position3_x, click_position3_y)
    #time.sleep(1)

    # click extenstion inner button (eg: x-block) in popup menu
    click_position4_x = screen_width - extn_btn4_loc_width
    click_position4_y = extn_btn4_loc_height
    #pyautogui.moveTo(click_position4_x, click_position4_y, duration=1)
    pyautogui.click(click_position4_x, click_position4_y)
    print(">>>>>>", click_position4_x, click_position4_y)
    pyautogui.moveTo(screen_width / 2, screen_height  * 2 / 3 , duration=1)
    return driver

def find_element_available(driver, element_criteria):
    flag = 1
    print('>>>>>', 'Finding ', element_criteria )
    time.sleep(3)
    while(flag):
        try:
            element = driver.find_element(By.XPATH, element_criteria)
            print('>>>>>', 'Found ', element_criteria )
            driver.execute_script('arguments[0].click()', element)
            flag = 0
        except Exception as e:
            print('>>>>>', 'Cannot find ', element_criteria )            
            print( e.msg )
            flag = 1
            time.sleep(1)

def pass_cloud_fare(driver) :
    flag = 1
    element_criteria = 'iframe'
    print('>>>>>', 'Finding ', element_criteria )
    time.sleep(1)
    while(flag):
        try:
            # iframe_element = driver.find_element(By.XPATH, element_criteria)
            iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe")))
            print("iframe", iframe)

            print('>>>>>', 'Found ', element_criteria )
            flag = 0
        except Exception as e:
            print('>>>>>', 'Cannot find ', element_criteria )            
            print( e.msg )
            flag = 1
            time.sleep(1)
    
    # tmp = driver
    # tmp.switch_to.frame(iframe_element)
    # element_in_iframe = tmp.find_element( By.XPATH, '//*[@id="ctp-checkbox-container"]' )

def perform_Tab_on_element(driver, element, repeat):
    for _ in range(repeat):  # Perform repeat Tab key presses
        element.send_keys(Keys.TAB)
        element = driver.switch_to.active_element
    return element   


def step1_joinClientOrLancer(driver):
    flag = 1
    while (flag) :
        try:
            # Find Radio
            parent = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container div.row")))
            second_element = parent.find_element(By.CSS_SELECTOR, "div[data-qa='work']")
            second_element.click()
            print(">>>>>1","Found the freelancer radio")

            # Click Apply            
            apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container button.up-btn.up-btn-primary.width-md.up-btn-block")))            
            apply_button.click()
            print(">>>>>1","Clicked Apply")

            flag = 0

        except Exception as e:
            print(">>>>>", 'Step 1 *** Failed')
            time.sleep(1)

firstName = 'John'
lastName = 'Doe'
password = 'Password11'

def step2_createNewAccountPage( driver, email ):
    flag = 1
    while (flag) :
        try:
            element = driver.find_element(By.ID, 'first-name-input')
            element.clear()
            element.send_keys(firstName)
            
            element = driver.find_element(By.ID, 'last-name-input')
            
            element.clear()
            element.send_keys(lastName)
            
            element = driver.find_element(By.ID, 'redesigned-input-email')
            element.clear()
            element.send_keys(email)
            
            element = driver.find_element(By.ID, 'password-input')
            element.clear()
            element.send_keys(password)

            # TAB to checkbox
            element = perform_Tab_on_element(driver, element, 4)
            element.send_keys(Keys.SPACE)
            time.sleep(1)
            # TAB to Button
            element = perform_Tab_on_element(driver, element, 4)
            time.sleep(2)
            element.send_keys(Keys.ENTER)

            # checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkbox-terms")))
            # checkbox.click()
            
            # Click Create            
            # apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".up-btn.up-btn-primary.up-btn-block.mt-10.mt-md-20.mb-20")))            
            # apply_button.click()
            print(">>>>>2", "Clicked Create")

            flag = 0

        except Exception as e:
            print(">>>>>", 'Step 2 *** Failed')
            time.sleep(3)

def step2_switchTabAndVerify(driver):
    driver.switch_to.window(driver.window_handles[2])
    driver.close()

    # driver.switch_to.window(driver.window_handles[1])
    # driver.close()
    print('>>>>>2', 'Close Other Tabs')

    driver.switch_to.window(driver.window_handles[0])
    print('>>>>>2', 'Page switched')
    time.sleep(3)
    # driver.refresh()
    print('>>>>>2', 'refresh end')

    # driver.get('https://www.minuteinbox.com/window/id/2')
    flag = 1
    while (flag) :
        try :
            # iframe = WebDriverWait(driver, 3).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe")))
            print('>>>>>2', 'Finding new email')

            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-href="2"].hidden-xs.hidden-sm.klikaciRadek.newMail')))
            # element = element.find_element( By.CSS_SELECTOR, "tr[data-href='2']" )
            element.click()

            driver.switch_to.frame("iframeMail")
            parent = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-holder")))
            verifyBtn = parent.find_element(By.CSS_SELECTOR, 'a')
            verifyBtn.click()
            time.sleep(2)
            flag = 0
            print(">>>>>2","Clicked Verify")
        except Exception as e:
            print(">>>>>", 'Step Email Verify Failed')
            time.sleep(1)

def closeOtherTabs(driver):
    time.sleep(1)
    window_handles = driver.window_handles
    for handle in window_handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
            driver.close()
    print('>>>>>', 'Closed Other tabs' )

def switch_window(driver, index) :
    time.sleep(1)
    flag = 1
    while(flag):
        try:
            driver.switch_to.window(driver.window_handles[index])
            flag = 0
        except:
            time.sleep(1)
    time.sleep(1)

def step3_closeCookieModal(driver):
    flag = 1
    while (flag):
        try:
        # Accept close_button.click()   
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ot-sdk-container button.onetrust-close-btn-handler.banner-close-button.ot-close-icon"))).click()
            print("Close Cookie Modal Success")
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>3', 'Close Cookie Modal Failed')
            time.sleep(1)

def step3_clickGetStartedBtn(driver):
    flag = 1
    while (flag):
        try:
            getStartedButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="get-started-btn"]')))
            getStartedButton.click()
            print('>>>>>3', 'Click Get Started Button Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>3', 'Click Get Started Button Failed')
            time.sleep(1)


def step3_clickExpertbox(driver):
    flag = 1
    while(flag):    
        try:
            expertRadio = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="radio"][value="FREELANCED_BEFORE"]')))
            expertRadio.click()
            time.sleep(1)
         # next button click event
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()  
            time.sleep(2)
            print('>>>>>3', 'Click I am a expert Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>3', 'Click I am a expert Failed')
            time.sleep(1)

def step3_clickToEarn(driver):
    flag = 1
    while(flag):    
        try:
        #### https://www.upwork.com/nx/create-profile/goal          
        # slide 2: 
         # To earn my main income  
            earnRadio = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="radio"][value="MAIN_INCOME"]')))
            earnRadio.click()
            time.sleep(1)
         # next button click event
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()  
            time.sleep(2)
            print('>>>>>3', 'Click ToEarn Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>3', 'Click ToEarn Failed')
            time.sleep(1)

def step3_clickSelectWork(driver):
    flag = 1
    while(flag):    
        try:
        #### https://www.upwork.com/nx/create-profile/work-preference        
        # slide 3: 
         # select work ways
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="checkbox"][aria-labelledby="button-box-29"]')))
            element.click()
            for _ in range(2):  # Perform 3 Tab key presses
                element.send_keys(Keys.TAB)
                element = driver.switch_to.active_element
                element.send_keys(Keys.SPACE)
            time.sleep(1)
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
            print('>>>>>3', 'Click Select Work ways Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>3', 'Click Select Work ways Failed')
            time.sleep(1)


def step3_getStarted(driver):
    print('>>>>>Step3', 'get started')
    
    switch_window(driver, 2)
    # closeOtherTabs(driver)

    step3_closeCookieModal(driver)
    time.sleep(2)
    step3_clickGetStartedBtn(driver)
    step3_clickExpertbox(driver)
    step3_clickToEarn(driver)
    step3_clickSelectWork(driver)
    
def step4_createProfile_slide_1(driver):
    print('>>>>>Step4', 'Create Profile and Skill select')
    flag = 1
    time.sleep(1)
    while(flag):    
        try:
        # slide 1
         # fill out manually button-click event
            #modal of "I am a free lancer, looking for work"   
            uploadButton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="resume-fill-manually-btn"]')))
            uploadButton.click()
            flag = 0
            print('>>>>>4_1', 'manually button-click Success')
        except Exception as e:
            # print(e)  
            print('>>>>>4_1', 'manually button-click Failed')
            time.sleep(1)
            
def step4_createProfile_slide_2(driver):        
    flag = 1
    time.sleep(2)
    while(flag):    
        try:    
        # slide 2
         # fill Your professional role
            role = "BlockChain | Node.js | React | JAVA"
            element = driver.switch_to.active_element
            element = perform_Tab_on_element(driver, element, 1)
            element.send_keys(role)
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)
            
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_2', 'fill role Failed')
            time.sleep(1)
            
def step4_createProfile_slide_3_Add_experience_main_1(driver):        
    flag = 1
    time.sleep(2)

    while(flag):    
        try:             
        # slide 3
         # Add experience
            add_experience_Button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="add-experience-label"]')))
            add_experience_Button.click()
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_2', 'Add_experience_main_1 click failed') 
            time.sleep(1)
            
def step4_createProfile_slide_3_Add_experience_modal(driver):        
    flag = 1
    time.sleep(2)
    title = "Software Developer"
    company = "Telecomm"
    location = "Guelph"
    description = "I am a senior software engineer"
    start_year = "2017"
    end_year = "2022"
    while(flag):    
        try:       
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="title-label"][placeholder="Ex: Software Engineer"]')))
            element.send_keys(title)
            time.sleep(5)
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="company-label"][placeholder="Ex: Microsoft"]')))        
            element.send_keys(company)
            time.sleep(5)
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="location-label"][placeholder="Ex: London"]')))
            element.send_keys(location)
            element = perform_Tab_on_element(driver, element, 4)
         # select startDate
            element.send_keys(Keys.SPACE)  # select startMonth
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(Keys.SPACE)  # select January
            time.sleep(3)
            element = driver.switch_to.active_element
            element = perform_Tab_on_element(driver, element, 1)
            element.send_keys(Keys.SPACE)  
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(start_year)  # select start Year
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)   
            
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-labelledby="end-date-month"][aria-controls="dropdown-menu"]')))
            element.send_keys(Keys.SPACE)  # select end Month
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(Keys.SPACE)  # select January
            time.sleep(3)
            element = driver.switch_to.active_element
            element = perform_Tab_on_element(driver, element, 1)
            element.send_keys(Keys.SPACE)  
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(end_year)  # select end Year
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)   
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-labelledby="description-label"]')))
            
            element.send_keys(description)  # insert Description
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)  # save button click
            print('>>>>>4_3', 'Add experience Moal Save')
            flag = 0               
        except Exception as e:
            # print(e)  
            print('>>>>>4_3', 'Add experience Moal Fail')
            time.sleep(1)
            
def step4_createProfile_slide_3_Add_experience_main_2(driver):        
    flag = 1
    time.sleep(2)
    while(flag):
        try:             
        # slide 3
         # Add experience
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
            print('>>>>>4_3', 'Success, "Next your education"')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_3', 'Add_experience_main_1 click failed') 
            time.sleep(1)
                        
def step4_createProfile_slide_4_Add_education_main_1(driver):
    flag = 1
    time.sleep(2)

    while(flag):    
        try:             
        # slide 4
         # Add education button
            add_experience_Button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="add-education-label"]')))
            add_experience_Button.click()
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_2', 'Add_experience_main_1 click failed') 
            time.sleep(1)
                        
                        
                        
                        
def step4_createProfile_slide_4_Add_education_modal_school(driver):       
    flag = 1
    time.sleep(2)
    school = "Toronto University"
    while(flag):    
        try:          
        # slide 4
         # Add education
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="school-label"][placeholder="Ex: Northwestern University"]')))
            element.send_keys(school)
            time.sleep(5)       
            flag = 0   
        except Exception as e:
            # print(e)  
            print('>>>>>4_4', 'Add education School Failed')
            time.sleep(1)              
    print('>>>>>4_4', 'Add education School Scuccess')
        
def step4_createProfile_slide_4_Add_education_modal_degree(driver):   
    flag = 1
    time.sleep(2)
    degree = "Bachelor of Computer Applications"
    while(flag):    
        try:          
        # slide 4
         # Add education
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"][placeholder="Ex: Bachelors"]')))        
            element.send_keys(degree)
            time.sleep(3)
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)     
            element = driver.switch_to.active_element
            element = perform_Tab_on_element(driver, element, 2)
            flag = 0   
        except Exception as e:
            # print(e)  
            print('>>>>>4_4', 'Add education degree Failed')
            time.sleep(1)                              
    print('>>>>>4_4', 'Add education degree Success')
        
def step4_createProfile_slide_4_Add_education_modal_FieldStudy(driver):      
    flag = 1
    time.sleep(2)
    field_Study = "Computer engineering"
    while(flag):    
        try:          
        # slide 4
         # Add education
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"][placeholder="Ex: Computer Science"]')))
            element.send_keys(field_Study)     
            time.sleep(3)
            
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)     
            element = driver.switch_to.active_element
            element = perform_Tab_on_element(driver, element, 2)
            flag = 0   
        except Exception as e:
            # print(e)  
            print('>>>>>4_4', 'Add education field study Failed')
            time.sleep(1)     
    print('>>>>>4_4', 'Add education field study Success')                              
    return element

def step4_createProfile_slide_4_Add_education_modal(driver):        
    step4_createProfile_slide_4_Add_education_modal_school(driver)
    step4_createProfile_slide_4_Add_education_modal_degree(driver)
    element = step4_createProfile_slide_4_Add_education_modal_FieldStudy(driver)
    flag = 1
    datesAttendedFrom = "2012"
    datesAttendedTo = "2016"
    education_Description = "Certificate in Applied Mathematics Certificate in Computer Software"
    time.sleep(1)   
    while(flag):    
        try:    
            # element = perform_Tab_on_element(driver, element, 1)
            element.send_keys(Keys.SPACE)  
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(datesAttendedFrom)  # select start Year
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)
            
            element = perform_Tab_on_element(driver, element, 1)
            element.send_keys(Keys.SPACE)  
            time.sleep(3)
            element = driver.switch_to.active_element
            element.send_keys(datesAttendedTo)  # select start Year
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)
            
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-labelledby="description-label"]')))
            
            element.send_keys(education_Description)  # insert Description
            element = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)  # save button click
            
            flag = 0   
        except Exception as e:
            # print(e)  
            print('>>>>>4_4', 'Add education Date Failed')
            time.sleep(1)
    print('>>>>>4_4', 'Add education Success')
       
def step4_createProfile_slide_4_Add_education_main_2(driver):        
    flag = 1
    time.sleep(2)
    while(flag):    
        try:             
        # slide 4
         # Add education
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
            print('>>>>>4_4', '"Next your education" click Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_4', '"Next your education" click Failed')  
            time.sleep(1)

def step4_createProfile_slide_5(driver):        
    flag = 1
    time.sleep(2)
    while(flag):    
        try:                 
        # slide 5
         # Add language     
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test="dropdown-toggle"][aria-labelledby="dropdown-label-english"]')))
            element.send_keys(Keys.SPACE)  # My level is        
            element = driver.switch_to.active_element
            element  = perform_Tab_on_element(driver, element, 3)
            element.send_keys(Keys.SPACE) 
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
            print('>>>>>4_5', '"Next add your skills" click Success')
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_5', '"Next add your skills" click Failed')
            time.sleep(1)    

def step4_createProfile_slide_6(driver):     
    blockchain = "Blockchain"
    java = "Java"
    javaScript = "JavaScript"
    node = "Node.js"
    react = "React"
    api = "API"   
    flag = 1
    time.sleep(2)
    while(flag):    
        try:     
        # slide 6 
         # Your skills
            element = driver.switch_to.active_element
            element  = perform_Tab_on_element(driver, element, 2)
            # element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[role="combobox"][aria-describedby="skill-selector-description"]')))           
            element.send_keys(blockchain)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 
            
            element = driver.switch_to.active_element
            element.send_keys(java)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 

            element = driver.switch_to.active_element
            element.send_keys(javaScript)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 
            
            element = driver.switch_to.active_element
            element.send_keys(node)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 
            
            element = driver.switch_to.active_element
            element.send_keys(react)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 
            
            element = driver.switch_to.active_element
            element.send_keys(api)
            time.sleep(2)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE) 
            
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
            
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_6', 'Skill insert Failed')
            time.sleep(1)
    print('>>>>>4_1', 'Skill insert Success')

def step4_createProfile_slide_7(driver):        
    profile = "10+ years of IT experience in all phases of SDLC, like Requirement Analysis, Design, Development, Testing, and Implementation."
    flag = 1
    time.sleep(2)    
    while(flag):    
        try:                 
        # slide 7
         # your profile
            driver.refresh()
            time.sleep(10)
            # element  = perform_Tab_on_element(driver, element, 1)
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-labelledby="overview-label"][aria-describedby="overview-counter"]')))
            element.send_keys(profile)
            
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()

            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_7', 'Profile insert Failed')
            time.sleep(1)
    print('>>>>>4_7', 'Profile overview insert Success')

def step4_createProfile_slide_8(driver):        
    flag = 1
    time.sleep(2)
    suggestServices = "Blockchain, NFT & Cryptocurrency, Web Development, Web & Mobile Design, Mobile Development, Game Design & Development, Desktop Application Development"
    suggestService = "Legal"
    while(flag):    
        try:                 
        # slide 8
         # Suggested Services 
            # element = driver.switch_to.active_element
            # element  = perform_Tab_on_element(driver, element, 1)
            dropdown_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="air3-dropdown-toggle-label ellipsis"]')))           
            driver.execute_script("arguments[0].textContent = arguments[1];", dropdown_element, suggestServices)
            
            # dropdown = Select(dropdown_element)
            # # Select an option by visible text
            # dropdown.select_by_visible_text(suggestService)
            
            nextButton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-test="next-button"][data-ev-label="wizard_next"]')))
            nextButton.click()
                        
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_8', 'Suggested Services insert Failed')
            time.sleep(1)
    print('>>>>>4_8', 'Suggested Services insert Success')

def step4_createProfile_slide_9(driver):        
    flag = 1
    time.sleep(2)

    while(flag):    
        try:                 
        # slide 9 
         # Hourly rate
            hourlyRate = "30"
            element = driver.switch_to.active_element
            element  = perform_Tab_on_element(driver, element, 1)
            element.send_keys(hourlyRate)
            element  = perform_Tab_on_element(driver, element, 4)
            element.send_keys(Keys.SPACE) 
            
            flag = 0
        except Exception as e:
            # print(e)  
            print('>>>>>4_1', 'Hourly rate Failed')
            time.sleep(1)
        
def step4_createProfile_slide_10(driver):        
    flag = 1
    time.sleep(2)

    while(flag):    
        try:             
        # slide 10
         # person information
            image_path = '/picture.png'
            birthday = "1996-07-09"
            street_address = "2036 Lock Street"
            city = "Guelph"
            zipcode = "N1H 2T2"
            phoneNum = "519-820-4588"
            element = driver.switch_to.active_element
            element  = perform_Tab_on_element(driver, element, 1)            
            # box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.air3-wizard-body.air3-wizard-grid-container.container \
            #                                                                         air3-avatar.air3-avatar-uploader")))
            element.send_keys(image_path)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(birthday)    
            element  = perform_Tab_on_element(driver, element, 3)
            element.send_keys(street_address)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(city)
            time.sleep(3)
            element  = perform_Tab_on_element(driver, element, 2)
            element.send_keys(Keys.SPACE)
            element  = perform_Tab_on_element(driver, element, 3)
            element.send_keys(zipcode)
            element  = perform_Tab_on_element(driver, element, 3)
            element.send_keys(phoneNum)
            element  = perform_Tab_on_element(driver, element, 3)
            element.send_keys(Keys.SPACE)
            
            submit_profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.container .air3-card .submit-profile-top-btn.air3-btn.air3-btn-primary.width-md m-0")))
            submit_profile.click()
            
            time.sleep(3)
            
            element = driver.switch_to.active_element
            element  = perform_Tab_on_element(driver, element, 2) 
            element.send_keys(Keys.SPACE)
                        
            flag = 0
        except:
            print("person information Failed")
            time.sleep(1)
        time.sleep(3)


def openMinuteInBox(driver):
    time.sleep(1)
    print('>>>>>', 'Opening MinuteInBox' )
    driver.get('https://www.minuteinbox.com/')

    flag = 1
    while (flag) :
        try:
            spanbox= WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.animace")))
            email = spanbox.text

            print(">>>>>", 'Found Email Success', email)
            flag = 0
        except Exception as e:
            print(">>>>>", 'Finding Email Failed')
            time.sleep(1)
        
    return email


def openUpwork(driver, email):

    time.sleep(3)
    print('>>>>>', 'Opening Upwork' )

    driver.switch_to.new_window('tab')
    driver.get('https://www.upwork.com/nx/signup/')

    step1_joinClientOrLancer(driver)

    step2_createNewAccountPage(driver, email)
    step2_switchTabAndVerify(driver)

    step3_getStarted(driver)

    step4_createProfile_slide_1(driver)   
    step4_createProfile_slide_2(driver)
    step4_createProfile_slide_3_Add_experience_main_1(driver)
    step4_createProfile_slide_3_Add_experience_modal(driver)
    step4_createProfile_slide_3_Add_experience_main_2(driver)
    step4_createProfile_slide_4_Add_education_main_1(driver)
    step4_createProfile_slide_4_Add_education_modal(driver)
    step4_createProfile_slide_4_Add_education_main_2(driver)
    step4_createProfile_slide_5(driver)
    step4_createProfile_slide_6(driver)
    step4_createProfile_slide_7(driver)
    step4_createProfile_slide_8(driver)
    step4_createProfile_slide_9(driver)
    step4_createProfile_slide_10(driver)

    time.sleep(2)

def openTempMail(driver):
    time.sleep(1)
    driver.get('https://temp-mail.org/en')
    print('>>>>>', 'Opened temp-mail' )

    window_handles = driver.window_handles
    for handle in window_handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
            driver.close()
    print('>>>>>', 'Closed Other tabs' )

    driver.switch_to.window(driver.window_handles[0])    

    time.sleep(2)

    # Click CloudFlare 
    # pass_cloud_fare(driver)
    # find_element_available(driver, '//*[@id="ctp-checkbox-container"]')
    # driver.find_element(By.XPATH, '//*[@id="content"]').click()
