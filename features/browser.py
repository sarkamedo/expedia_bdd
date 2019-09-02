from selenium import webdriver
import datetime
import time


class Browser():

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
        time_stamp = datetime.datetime\
            .fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        file_path = f"features/screenshots/{filename}-{time_stamp}.png"
        context.driver.save_screenshot(file_path)
        return print(f"Screenshot was saved as {file_path}")
