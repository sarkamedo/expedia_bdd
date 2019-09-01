# comment the following two lines if you encounter issues with importing local modules
import sys
sys.path.append(".")

from features.pages.expedia_home import MainPage
from features.pages.expedia_search_results import ResultsPage
from features.browser import Browser
from hamcrest import *
from behave import *
import time

main_page = MainPage()
results_page = ResultsPage()

@given("I'm on a hotels tab")
def step_impl(context):
    context.browser.visit_link("https://www.expedia.com/")
    main_page.click_hotels_button()


@when("I enter the desired location and click search")
def step_impl(context):
    main_page.search_hotels_and_display_results("Key West")
    # This was done to just simulate real user. Assertion works without all this extra window switching
    if len(context.browser.get_window_handles()) > 1:
        context.browser.switch_to_window(1)
        context.browser.close_current_tab_or_window()
        context.browser.switch_to_window(0)
        time.sleep(4)

@then("I must get 20 hotels as a result")
def step_impl(context):
    assert_that(len(results_page.get_list_of_results()), equal_to(20))

@then("if I scroll down it should load another 20 hotels")
def step_impl(context):
    pass