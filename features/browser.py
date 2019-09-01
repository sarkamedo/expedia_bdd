from selenium import webdriver


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
