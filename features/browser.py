from selenium import webdriver
import datetime, time


class Browser(object):

    driver = webdriver.Chrome()

    def close_current_tab_or_window(context):
        context.driver.close()

    def quit_browser(context):
        context.driver.quit()

    def visit_link(context, link):
        context.driver.get(link)

    def get_window_handles(context):
        return context.driver.window_handles

    def get_current_window_handle(context):
        return context.driver.current_window_handle

    def switch_to_window(context, window_index):
        context.driver.switch_to.window(
            context.driver.window_handles[window_index])

    def js_scroll_into_view(context, target):
        context.driver.execute_script(
            'arguments[0].scrollIntoView(true);', target)

    def take_screenshot(context, filename):
        timpestamp = datetime.datetime\
            .fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        context.driver.save_screenshot(f"features/screenshots/{filename}_{timpestamp}.png")
