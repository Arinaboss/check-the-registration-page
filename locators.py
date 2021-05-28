from selenium.webdriver.common.by import By

class Registration:
    NAME = (By.CSS_SELECTOR, '[class="form-input rounded-md shadow-sm block mt-1 w-full"]')
    SURNAME = (By.CSS_SELECTOR, '[name="last_name"]')
    EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    PHONE = (By.CSS_SELECTOR, '[name="phone"]')
    PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    CONFIRMPASSWD = (By.CSS_SELECTOR, '[name="password_confirmation"]')
    CHECKBOKS = (By.CSS_SELECTOR, '[type="checkbox"]')
    REGISTRATION = (By.CSS_SELECTOR, '[type="submit"]')
    ERROR = (By.CSS_SELECTOR, '[class="mt-3 list-disc list-inside text-sm text-red-600"]')

    HOME_PAGE = (By.CSS_SELECTOR, '[class="min-h-screen bg-gray-100"]')
    EXIT = (By.CSS_SELECTOR, '[class="h-8 w-8 rounded-full object-cover"]')
    BUTTON = (By.XPATH, '//a[text()="Выйти"]')

    FIELD_LOGIN = (By.CSS_SELECTOR, '[class="w-full sm:max-w-md mt-6 px-6 py-4 bg-white shadow-md overflow-hidden sm:rounded-lg"]')
    ALREADY_REGISTERED = (By.CSS_SELECTOR, '[class="underline text-sm text-gray-600 hover:text-gray-900"]')
    ENTRANCE = (By.CSS_SELECTOR, '[type="submit"]')

