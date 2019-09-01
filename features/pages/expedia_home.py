from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
from features.browser import Browser


class MainPage(Browser):

    # Locators
    _hotels_button = "#tab-hotel-tab-hp"
    _search_box = "#hotel-destination-hp-hotel"

    def get_hotels_button(self):
        return WDW(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._hotels_button)))

    def get_search_box(self):
        return WDW(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self._search_box)))

    def click_hotels_button(self):
        self.get_hotels_button().click()

    def perform_search_by_query(self, search_query):
        sb = self.get_search_box()
        sb.clear()
        sb.send_keys(search_query)
        sb.send_keys(Keys.RETURN)
        time.sleep(1)
        sb.send_keys(Keys.RETURN)

    def search_hotels_and_display_results(self, search_query):
        self.click_hotels_button()
        self.perform_search_by_query(search_query)
