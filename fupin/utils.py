import json
from selenium import webdriver


def create_chrome_driver(*, headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options)
    # 最大化窗口
    browser.maximize_window()
    # 调整缩放比
    browser.execute_script("document.body.style.zoom = '50%';")
    # 伪装成普通浏览器
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument', 
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    return browser


def dump_cookies(browser, cookies_file):
    with open(cookies_file, 'w') as file:
        cookies = browser.get_cookies()
        json.dump(cookies, file)


def add_cookies(browser, cookies_file):
    with open(cookies_file, 'r') as file:
        cookies_list = json.loads(file)
        for cookie_dict in cookies_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)
