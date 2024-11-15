from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}

USER_ID = os.environ["USER_ID"]
PASSWORD = os.environ["PASSWORD"]

BUSINESS_UNIT = "11100"
VENDOR_NAME = "Derm"
ITEM_CODE = "0425300"
PO_QTY = "30,000"
PRICE = "2.76"
DELIVERY_DATE = '12/20/2024'
SHIP_TO = '10100'
COMMENT_TYPE = 'CMB'
COMMENT_NAME = 'ALL'
DISPATCH_METHOD = 'Email'
EMAIL = 'jiovino@combe.com'


def sleep(x):
    time.sleep(x)


# instantiate Chrome with Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('css.combe.com/Default.aspx')
driver.get('peoplesoft.global.combe.com')

# log in
driver.find_element(By.XPATH, '//*[@id="login"]/table/tbody/tr/td/p[3]/a').click()
user_id = driver.find_element(By.ID, 'userid')
user_id.send_keys(USER_ID, Keys.TAB, PASSWORD, Keys.RETURN)

# instantiate the new PO
driver.find_element(By.ID, 'fldra_EPPO_PURCHASING').click()
driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr['
                              '2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/ul/li[2]/a')
business_unit_input = driver.find_element(By.NAME, 'PO_ADD_SRCH_BUSINESS_UNIT')
business_unit_input.clear()
business_unit_input.send_keys(BUSINESS_UNIT, Keys.RETURN)
sleep(1)

# search supplier by short name
driver.find_element(By.XPATH, '//*[@id="VENDOR_VENDOR_NAME_SHORT$prompt"]/img').click()
sleep(.5)
vendor_short_name = driver.find_element(By.ID, 'VENDOR_PO_VW_VENDOR_NAME_SHORT')
vendor_short_name.send_keys(VENDOR_NAME, Keys.RETURN)
driver.find_element(By.ID, 'SEARCH_RESULT1').click()
sleep(.4)

# enter first page item detail information
driver.find_element(By.ID, 'PO_HDR_BUYER_ID').send_keys(USER_ID)
driver.find_element(By.ID, 'INV_ITEM_ID$0').send_keys(ITEM_CODE)
driver.find_element(By.ID, 'PO_PNLS_WRK_QTY_PO$0').send_keys(PO_QTY)
driver.find_element(By.ID, 'PO_LINE_WK_PRICE_PO_C$0').send_keys(PRICE)

# second page for date
driver.find_element(By.ID, 'PO_PNLS_WRK_GOTO_SCHED$0').click()
sleep(.5)
date_field = driver.find_element(By.ID, 'PO_LINE_SHIP_DUE_DT$0')
date_field.clear()
date_field.send_keys(DELIVERY_DATE)
driver.find_element(By.ID, 'PO_LINE_SHIP_SHIPTO_ID$0')

# enter tax details
driver.find_element(By.ID, "GOTO_DISTRIB$0").click()
sleep(.5)
driver.find_element(By.ID, '#ICNo').click()
sleep(.5)
driver.find_element(By.XPATH, '//*[@id="PTGRIDTAB"]/table/tbody/tr/td[2]/a').click()
sleep(.5)
driver.find_element(By.ID, 'LOCATION$0').send_keys(SHIP_TO)
driver.find_element(By.ID, '#ICSave').click()
sleep(.4)
driver.find_element(By.ID, '#ICSave').click()
sleep(.3)
driver.find_element(By.ID, '#ICOK').click()
sleep(.2)
driver.find_element(By.ID, 'PO_PNLS_PB_PO_RETURN_PAGE')

# add comments
driver.find_element(By.ID, 'COMM_WRK1_COMMENTS_PB').click()
sleep(.3)
driver.find_element(By.ID, 'COMM_WRK_STD_COMMENT_PB$0').click()
sleep(.3)
driver.find_element(By.ID, 'COMM_WRK1_STD_COMMENT_TYPE').send_keys(COMMENT_TYPE)
driver.find_element(By.ID, 'COMM_WRK1_STD_COMMENT_TYPE').send_keys(COMMENT_NAME)
driver.find_element(By.ID, '#ICSave').click()
sleep(.3)
driver.find_element(By.ID, '#ICSave').click()
sleep(.3)

# approve, save, dispatch
driver.find_element(By.ID, 'PO_PNLS_WRK_APPROVE_PB').click()
driver.find_element(By.ID, '#ICSave').click()
sleep(.4)
dispatch_method_dropdown = driver.find_element(By.ID, 'PO_HDR_DISP_METHOD')
dispatch_method_dropdown.click()
dispatch_method_dropdown.send_keys(DISPATCH_METHOD, Keys.RETURN)
driver.find_element(By.ID, 'PO_PNLS_WRK_DISPATCH_PB').click()
sleep(.3)
driver.find_element(By.ID, 'PO_HDR_EMAIL_EMAILID$0').send_keys(EMAIL, Keys.RETURN)
sleep(.2)
