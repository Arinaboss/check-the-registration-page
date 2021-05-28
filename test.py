from page import Regpage
from selenium import webdriver
import pytest
import time

link = 'http://trading.devfo.xyz/register'
my_name = "Vera"
my_lastname = "Perlova"
my_phone = '+123456789012'
my_password = '12345678'
confirm_passwd = '12345678'


def test_user_registration_exit_authorization():
    browser = webdriver.Chrome()
    browser.get(link)
    page = Regpage(browser, link)
    page.fill_username(my_name)
    page.fill_lastname(my_lastname)
    page.fill_email(str(time.time())+"@net.com")
    page.fill_phone(my_phone)
    page.fill_password(my_password)
    page.fill_confirm_password(confirm_passwd)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.click_button_exit()
    page.fill_email(str(time.time())+"@net.com")
    page.fill_password(my_password)
    page.click_button_entrance()
    page.check_home_page_displayed()
    browser.quit()


@pytest.mark.parametrize('name', ['.,', '123', '   ', 'a y s', '@#$', 'ARINA mikki',
                                  'cfecewfdhwetfvdhwtefvcwhadtfwefdwjefdwejtfdwjefdwjefdcwafdcwhedcwhdwehfwedth'])
def test_error_exit_if_invalid_name(name):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    page = Regpage(browser, link)
    page.fill_username(name)
    page.fill_lastname(my_lastname)
    page.fill_email(str(time.time())+"@net.com")
    page.fill_phone(my_phone)
    page.fill_password(my_password)
    page.fill_confirm_password(confirm_passwd)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.check_error()
    browser.quit()


@pytest.mark.parametrize('lastname', ['123', '   ', 'a y s', '@#$', 'ARINA mikki',
                                      'cfecewfdhwetfvdhwtefvcwhadtfwefdwjefdwejtfdwjefdwjefdcwafdcwhedcwhdwehfwedth'])
def test_error_exist_if_invalid_lastname(lastname):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    page = Regpage(browser, link)
    page.fill_username(my_name)
    page.fill_lastname(lastname)
    page.fill_email(str(time.time())+"@net.com")
    page.fill_phone(my_phone)
    page.fill_password(my_password)
    page.fill_confirm_password(confirm_passwd)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.check_error()
    browser.quit()


def test_if_email_already_used():
    browser = webdriver.Chrome()
    browser.get(link)
    page = Regpage(browser, link)
    page.fill_username(my_name)
    page.fill_lastname(my_lastname)
    page.fill_email('kitikat@net.com')
    page.fill_phone(my_phone)
    page.fill_password(my_password)
    page.fill_confirm_password(confirm_passwd)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.check_home_page_displayed()
    browser.quit()


@pytest.mark.parametrize('phone', ['987', '789456123456789789',
                         '+123456789555',
                         '+12345678999',
                         '+1234567892222',
                         '             ',
                         'jnetwefour',
                         '!@#$%',
                        '+'])
def test_error_exist_if_invalid_number_phone(phone):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    page = Regpage(browser, link)
    page.fill_username(my_name)
    page.fill_lastname(my_lastname)
    page.fill_email(str(time.time())+"@net.com")
    page.fill_phone(phone)
    page.fill_password(my_password)
    page.fill_confirm_password(confirm_passwd)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.check_error()
    browser.quit()


@pytest.mark.parametrize('password, confpassord', [('        ', '        '),
                                                    ('12345678', '87654321',),
                                                   ('тригонометрия', 'тригонометрия'),
                                                   ('123', '123'),
                                                       ('hfxhxhtrxhtrxhxhxhfxhxhfxxbfdxsxhdjyfcjdchzgzgcghfxfbdzdszhfxgfdzdszgd',
                                                        'hfxhxhtrxhtrxhxhxhfxhxhfxxbfdxsxhdjyfcjdchzgzgcghfxfbdzdszhfxgfdzdszgd')])
def test_error_exist_if_password_invalid(password, confpassord):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    page = Regpage(browser, link)
    page.fill_username(my_name)
    page.fill_lastname(my_lastname)
    page.fill_email(str(time.time())+"@net.com")
    page.fill_phone(my_phone)
    page.fill_password(password)
    page.fill_confirm_password(confpassord)
    page.click_agree_with_terms()
    page.click_button_registration()
    page.check_error()
    browser.quit()



def test_user_authorization():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    page = Regpage(browser, link)
    page.click_link_to_autorization()
    page.fill_email('kamlukarina@gmail.com')
    page.fill_password(my_password)
    page.click_button_entrance()
    page.check_home_page_displayed()
    browser.quit()




