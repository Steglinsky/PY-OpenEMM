# requirements
import os
import re
import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

ISO885915 = '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div[2]/div[' \
            '1]/select/option[1] '
ISO88591 = '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div[2]/div[' \
           '1]/select/option[2] '
GB2312 = '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div[2]/div[' \
         '1]/select/option[3] '
UTF8 = '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div[2]/div[' \
       '1]/select/option[4] '
basic_password = 'basic_password'
login_value = 'admin'
date_value = 'MM.DD'
file_path = 'C:/Lists/MM.DD'


# is ready function
def is_ready():
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                        'left_navigation_level1_active_round')))
        print('Page is ready')
    except TimeoutException:
        print('Loading took too much time')


# login function
def login(address='domain'):
    driver.get(str(address) + ':8080/logon.do?action=0')
    driver.find_element_by_name('username').send_keys(login_value)
    driver.find_element_by_name('password').send_keys(basic_password)
    driver.find_element_by_class_name('action_button').click()
    print('Logged in ' + address)


# change password function
def change_password():
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[7]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[7]/ul/li[4]/a').click()
    is_ready()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[3]/table/tbody/tr/td[1]/span/a').click()
    is_ready()
    driver.find_element_by_id('password').send_keys(basic_password)
    driver.find_element_by_id('repeat').send_keys(basic_password)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[3]/div[1]/a').click()


def new_list():
    is_ready()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/a').click()
    is_ready()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/ul/li[2]/a').click()
    is_ready()
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[1]/div[2]/div[1]/input").send_keys(
        Keys.CONTROL, 'a')
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[1]/div[2]/div[1]/input").send_keys(
        Keys.BACKSPACE)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[1]/div[2]/div[1]/input").send_keys(
        date_value)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[1]/a').click()


def data_import(list_name):
    is_ready()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/a').click()
    is_ready()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/ul/li[3]/a').click()
    # indicate file location
    driver.refresh()
    driver.find_element_by_name('csvFile').send_keys(file_path + list_name)
    driver.find_element_by_link_text('Proceed').click()
    # find correct checkbox
    count = driver.find_elements_by_xpath("//*[@type='checkbox']")
    int_string = []
    for j in range(len(count)):
        string = count[j].get_attribute('name')
        x = string.split('_')
        int_string.append(int(x[2]))
    maximum = max(int_string)
    driver.find_element_by_name("agn_mlid_" + str(maximum)).click()
    # start upload
    driver.find_element_by_link_text('Start import').click()
    is_ready()
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[4]/div[2]/a').click()
    except:
        pass
    is_ready()
    # confirm upload
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div[2]/div/a').click()


def is_clear():
    clear_exists = driver.find_element_by_xpath \
        ('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[3]/table/tbody') \
        .get_attribute('innerText')
    if 'clear' in clear_exists:
        print('True')
        return True
    else:
        print('False')
        return False


def remove_data(address='domain'):
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[4]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[4]/ul/li[2]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[3]/div[2]/table/tbody/tr/td[3]/select').send_keys('M', Keys.RETURN)



def mailing_set(address='domain'):
    global raw_today
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[1]/a').click()
    is_ready()
    mailings_list = driver.find_element_by_class_name(
        'ie7hack').get_attribute('innerHTML')
    process_mailings_1 = (mailings_list[20:106])
    process_mailings_2 = process_mailings_1.replace('amp;', '')
    process_mailings_3 = 'http://' + address + ':8080' + process_mailings_2
    print(mailings_list)
    print(process_mailings_1)
    print(process_mailings_2)
    print(process_mailings_3)
    driver.get(process_mailings_3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/ul/li[6]/a').click()
    is_ready()
    mailing_ready = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div[3]').get_attribute('innerHTML')
    if 'Mailing:' in mailing_ready:
        print('Mailing not ready')
    else:
        print('Mailing ready')


def create(name='name', subject='subject', sender_email='sender_email', sender_name='sender_name',
           reply_email='reply_email', reply_name='reply_name', charset=UTF8, line_feed='1', mail_format='1',
           measure='1',
           mailing_id='05.25'):
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[1]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[1]/ul/li[2]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div['
                                 '1]/a[1]').click()
    is_ready()
    # fill in the mailing information
    driver.find_element_by_name('shortname').send_keys(name)
    driver.find_element_by_name('emailSubject').send_keys(subject)
    driver.find_element_by_name('media[0].fromEmail').send_keys(sender_email)
    driver.find_element_by_name('media[0].fromFullname').send_keys(sender_name)
    driver.find_element_by_name('media[0].replyEmail').send_keys(reply_email)
    driver.find_element_by_name('media[0].replyFullname').send_keys(reply_name)
    # ISO885915 ISO88591 GB2312 UTF8
    driver.find_element_by_xpath(charset).click()
    # 1 - 22
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div['
                                 '2]/div[2]/select/option[' + line_feed + ']').click()
    # 1 - 3
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div['
                                 '2]/div[3]/select/option[' + mail_format + ']').click()
    # 1 - 3
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div[2]/div['
                                 '2]/div[4]/select/option[' + measure + ']').click()
    # general
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[4]/div[2]/div['
                                 '1]/div[1]/div[1]/select/option[2]').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[4]/div[1]/div/'
                                 'a').click()

    mailing_lists = Select(driver.find_element_by_id('settings_general_mailingliste'))
    all_templates = (driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div['
                                                  '3]/form/div[4]/div[2]/div[1]/div[1]/div[2]/select').get_attribute(
        'innerHTML'))
    matched_lines = [line for line in all_templates.split('\n') if mailing_id in line]
    value = re.findall(r'<option value=\"(.*)\">', matched_lines[0])
    mailing_lists.select_by_value(value[0])
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[6]/div[1]/a").click()


def send(day='2', hour='10', minute='31', stepping='5'):
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/ul/li[6]/a').click()
    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div'
                                 '/div[3]/div[3]/div[2]/div[8]/div/a').click()
    is_ready()
    volume_1 = (driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/form").get_attribute(
        'innerText'))
    volume_2 = re.search('contains (.*?) recipients', volume_1)
    block_size = int(volume_2[1]) / 10
    final_block_size = math.ceil(block_size)

    is_ready()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div[2]/div['
                                 '1]/div/select/option[' + day + ']').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div[2]/div['
                                 '2]/select[1]/option[' + hour + ']').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div[2]/div['
                                 '2]/select[2]/option[' + minute + ']').click()
    # block size
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "1]/input").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "1]/input").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "1]/input").send_keys(final_block_size)
    # stepping
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "2]/input").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "2]/input").send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[4]/div[2]/div["
                                 "2]/input").send_keys(stepping)
    if block_size > 0:
        # Approve & Send
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[5]/div[1]").click()
        is_ready()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/form/div[2]/div['
                                     '2]/div[1]/div/a').click()
        is_ready()
    else:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[5]/div[2]/a").click()

