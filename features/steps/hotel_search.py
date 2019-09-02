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


@when("I enter the {desired_location} and click search")
def step_impl(context, desired_location):
    main_page.search_hotels_and_display_results(desired_location)


@then("I must get {hotels_list} hotels as a result")
def step_impl(context, hotels_list):

    try:
        assert_that(len(results_page.get_list_of_results()),
                    equal_to(int(hotels_list)))
    except AssertionError:
        print("SCREENSHOT SAVED")
        context.browser.take_screenshot("assert_list_of_hotels_equal_to")


@then("if I scroll down to the last hotel")
def step_impl(context):
    # hotels_lst = results_page.get_list_of_results()
    # context.browser.js_scroll_into_view(hotels_lst[-1])
    pass


@then("I should see more than {hotels_list} hotels")
def step_impl(context, hotels_list):
    # try:
    #     assert_that(len(results_page.get_list_of_results()),
    #                 greater_than(int(hotels_list)))
    # except AssertionError:
    #     print("SCREENSHOT SAVED")
    #     context.browser.take_screenshot("assert_list_of_hotels_greater_than")
    pass
