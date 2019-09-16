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
    main_page.perform_search_by_query(desired_location)
    context.browser.close_pop_up_ad_window()


@then("I must get {hotels_quantity} hotels as a result")
def step_impl(context, hotels_quantity):
    try:
        assert_that(len(results_page.get_list_of_results),
                    equal_to(int(hotels_quantity)))
    except AssertionError:
        context.browser.take_screenshot("assert_list_of_hotels_equal_to")
        raise AssertionError


@then("if I scroll down to the last hotel")
def step_impl(context):
    context.browser.js_scroll_into_view(results_page.get_list_of_results[-1])
    time.sleep(2)


@then("I should see more than {hotels_quantity} hotels")
def step_impl(context, hotels_quantity):
    try:
        assert_that(len(results_page.get_list_of_results),
                    greater_than(int(hotels_quantity)))
    except AssertionError:
        context.browser.take_screenshot(
            "assert_list_of_hotels_greater_than")
        raise AssertionError


@then("first result must have sponsored label")
def step_impl(context):
    try:
        assert_that(results_page.get_sponsored_label().text,
                    equal_to("Sponsored"))
    except AssertionError:
        context.browser.take_screenshot(
            "assert_sponsored_label_exists")
        raise AssertionError
