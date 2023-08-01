import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from http.cookiejar import CookieJar

from tools import load_cookies_new

# Load cookies from CookieJar
cookie_jar = load_cookies_new()


chromedriver = os.path.join(os.getcwd(), 'chromedriver_windows')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_argument("--incognito")

driver = webdriver.Chrome(chromedriver, options=options)

# Open the desired page to extract its domain

page_domain = 'www.ticketmaster.de' #driver.current_url.split('/')[2]

# Add the cookies from CookieJar to Selenium WebDriver
for cookie in cookie_jar:
    if page_domain.endswith(cookie.domain):
        driver.add_cookie({
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
            'expires': cookie.expires
        })

driver.get("https://www.ticketmaster.de/checkout/checkout.php")
# Refresh the page to apply the cookies
# driver.refresh()



# Now the page should be loaded with the cookies applied
# You can continue interacting with the page using Selenium WebDriver

# Close the driver when you're done
# driver.quit()