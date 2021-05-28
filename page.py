from locators import Registration


class Regpage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        #browser.get(link)


    def fill_username(self, my_name):
        name = self.browser.find_element(*Registration.NAME)
        name.send_keys(my_name)

    def fill_lastname(self, my_lastname):
        surname = self.browser.find_element(*Registration.SURNAME)
        surname.send_keys(my_lastname)

    def fill_email(self, mail):
        email = self.browser.find_element(*Registration.EMAIL)
        email.send_keys(mail)

    def fill_phone(self, num):
        number = self.browser.find_element(*Registration.PHONE)
        number.send_keys(num)

    def fill_password(self, numbers):
        passwd = self.browser.find_element(*Registration.PASSWORD)
        passwd.send_keys(numbers)

    def fill_confirm_password(self, numbers):
        confirm = self.browser.find_element(*Registration.CONFIRMPASSWD)
        confirm.send_keys(numbers)

    def click_agree_with_terms(self):
        boks = self.browser.find_element(*Registration.CHECKBOKS)
        boks.click()

    def click_button_registration(self):
        button = self.browser.find_element(*Registration.REGISTRATION)
        button.click()

    def check_home_page_displayed(self):
        home = self.browser.find_element(*Registration.HOME_PAGE)
        assert home.is_displayed() == True, f"excpect home page, got smt error"

    def check_error(self):
        error = self.browser.find_element(*Registration.ERROR)
        assert error.is_displayed() == True, f"expect error, got ok"

    def click_button_exit(self):
        my_acc = self.browser.find_element(*Registration.EXIT)
        my_acc.click()
        exit = self.browser.find_element(*Registration.BUTTON)
        exit.click()

    def check_login_field_displayed(self):
        field_login = self.browser.find_element(*Registration.FIELD_LOGIN)
        assert field_login.is_displayed() == True, f"expect field_login got smt other"


    def click_link_to_autorization(self):
        already_registered = self.browser.find_element(*Registration.ALREADY_REGISTERED)
        already_registered.click()

    def click_button_entrance(self):
        button = self.browser.find_element(*Registration.ENTRANCE)
        button.click()
