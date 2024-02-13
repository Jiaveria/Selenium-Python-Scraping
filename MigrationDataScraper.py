import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


###############################   DUMMY INPUTS ###################################

dataset='S7_student_first_time'
selection_list = ['Location','Institution Type','Nationality','Application Criteria']
default_selection = False
filters = [
    {
        'FilterVariable' : 'Date',
        'FilterType' : "DOES NOT CONTAIN",
        'FilterCriteria' : ['2013-07-31','2013-09-30']
    },
    {
        'FilterVariable' : 'Student Type',
        'FilterType' : "DOES NOT CONTAIN", 
        'FilterCriteria' : ['Other']
    },
      {
        'FilterVariable' : 'Location',
        'FilterType' : "CONTAINS",
        'FilterCriteria' : ['Auckland','Bay of Plenty']
    },
    {
        'FilterVariable' : 'Nationality',
        'FilterType' : "CONTAINS",
        'FilterCriteria' : ['Pakistan','Bangladesh']
    }
]

################################ FUNCTION ###################################

def MigrationDataScraper(dataset,selection_list,filters,default_selection):

    options=webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://mbienz.shinyapps.io/migration_data_explorer/")
    element = driver.find_element(By.LINK_TEXT, 'Data Explorer')
    element.click()

    #category selection
    categories=driver.find_elements(By.NAME,'data_explorer-dname')
    for category in categories:
        if (category.get_attribute('value') == dataset):
            category.click()

    time.sleep(2)

    #variables selection
    div_element = driver.find_element(By.CLASS_NAME, 'list-group.inlist.inlist-multi')
    variables = div_element.find_elements(By.TAG_NAME, 'button')

    if (default_selection and len(selection_list)<=3):  # Max 4 variables allowed
        for variable in variables:
            if(variable.get_attribute('value') in selection_list):
                variable.click()
    elif (len(selection_list)<=4 and not default_selection):
        for variable in variables:
            if(variable.get_attribute('class') == 'list-group-item list-group-item-selected'):
                first_span = variable.find_element(By.XPATH, "./span[1]")  
                driver.execute_script("arguments[0].setAttribute('class', 'glyphicon glyphicon-unchecked')", first_span)
                variable.click()
                break
        for variable in variables:
            if(variable.get_attribute('value') in selection_list):
                variable.click()

    #Filters selection
    if (filters and len(filters)):
        for i in range (len(filters)): 
            filter_var = filters[i]['FilterVariable']
            filter_type = filters[i]['FilterType']
            filter_criteria = filters[i]['FilterCriteria']
            filter_div = driver.find_element(By.ID, 'data_explorer-cond-add')
            add_filter_btn = filter_div.find_element(By.TAG_NAME, 'button')
            add_filter_btn.click()

            time.sleep(0.5)
            if (filter_var == 'Date'):
                if (filter_type == 'DOES NOT CONTAIN'):
                    filter_type_div =  driver.find_element(By.ID,'data_explorer-cond-type')
                    conditions = filter_type_div.find_elements(By.XPATH, ".//div[@class='radio']//input")
                    time.sleep(0.5)

                    for con in conditions:
                        if con.get_attribute('value') == filter_type:
                            con.click()

                for j in range(len(filter_criteria)):
                    filter_criteria_div = driver.find_element(By.CSS_SELECTOR, 'div.list-group.inlist.inlist-multi[data-inlist="never-toggle"]')
                    filter_btn_tags = filter_criteria_div.find_elements(By.TAG_NAME, 'button')

                    time.sleep(0.5)

                    for flt in filter_btn_tags:
                        if(flt.get_attribute('value') == filter_criteria[j]):
                            flt.click()
                            break
                submit_btn = driver.find_element(By.CSS_SELECTOR, 'div.float-con button.btn.btn-default.btn-ok')
                submit_btn.click()
            
            if (filter_var != 'Date'): 
                filter_variable_div = driver.find_element(By.ID,'data_explorer-cond-var')
                options = filter_variable_div.find_elements(By.XPATH, ".//div[@class='radio']//input")
                
                time.sleep(0.5) 

                for opt in options:
                    if opt.get_attribute('value') == filter_var:
                        opt.click()
                        break


                filter_type_div =  driver.find_element(By.ID,'data_explorer-cond-type')
                conditions = filter_type_div.find_elements(By.XPATH, ".//div[@class='radio']//input")
                time.sleep(0.5)

                for con in conditions:
                    if con.get_attribute('value') == filter_type:
                        con.click()


                for j in range(len(filter_criteria)):
                    filter_criteria_div = driver.find_element(By.CSS_SELECTOR, 'div.list-group.inlist.inlist-multi[data-inlist="never-toggle"]')
                    filter_btn_tags = filter_criteria_div.find_elements(By.TAG_NAME, 'button')
                    time.sleep(0.5)
                    for flt in filter_btn_tags:
                        if(flt.get_attribute('value') == filter_criteria[j]):
                            flt.click()
                            break
                submit_btn = driver.find_element(By.CSS_SELECTOR, 'div.float-con button.btn.btn-default.btn-ok')
                submit_btn.click()
                


    time.sleep(2)

    download_btn=driver.find_element(By.ID,'data_explorer-csv-down')
    download_btn.click()


###################   FUNCTION CALL    ###################################

MigrationDataScraper(dataset,selection_list,filters,default_selection)