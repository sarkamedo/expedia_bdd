from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
from features.browser import Browser


class ResultsPage(Browser):

    # Locators
    _list_of_results = ".listing__link.uitk-card-link"
    _sponsored_label = "span.uitk-badge-text"

    def get_list_of_results(self):
            element = WDW(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self._list_of_results)))
            return element

    def get_sponsored_label(self):
        return WDW(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._sponsored_label)))
