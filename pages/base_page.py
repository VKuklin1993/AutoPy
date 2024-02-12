from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_url(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_is_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_is_clicable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
