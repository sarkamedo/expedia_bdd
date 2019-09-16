from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
from features.browser import Browser


class ResultsPage(Browser):

    # Locators
    _list_of_results = (By.CSS_SELECTOR, ".listing__link.uitk-card-link")
    _sponsored_label = (By.CSS_SELECTOR, "span.uitk-badge-text")

    @property
    def get_list_of_results(self):
        return WDW(self.driver, 10).until(
            EC.visibility_of_all_elements_located((self._list_of_results)))

    def get_sponsored_label(self):
        return WDW(self.driver, 10).until(EC.visibility_of_element_located((self._sponsored_label)))
