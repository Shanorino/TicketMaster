import http.cookiejar
import pickle
import browser_cookie3


def save_cookies_new():
    cj = browser_cookie3.chrome() #(domain_name='.ticketmaster.de')
    cookies = []

    for cookie in cj:
        if True: #cookie.domain == '.ticketmaster.de':
            cookie_dict = vars(cookie)
            cookie_dict['rest'] = cookie_dict.pop('_rest')
            cookies.append(cookie_dict)

    with open('cookies.pkl', 'wb') as f:
        pickle.dump(cookies, f)


def load_cookies_new():
    valid_cookie_attributes = {'version', 'name', 'value', 'port', 'port_specified',
                               'domain', 'domain_specified', 'domain_initial_dot',
                               'path', 'path_specified', 'secure', 'expires', 'discard',
                               'comment', 'comment_url', 'rfc2109', 'rest'}

    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)

    cj = http.cookiejar.CookieJar()

    for cookie_dict in cookies:
        # rest_values = cookie_dict.pop('_rest', {})
        # cookie_dict.update(rest_values)
        # Ignore any attributes not recognized by the Cookie constructor.
        cookie_dict = {k: v for k, v in cookie_dict.items() if k in valid_cookie_attributes}
        cookie = http.cookiejar.Cookie(**cookie_dict)
        cj.set_cookie(cookie)
    return cj


save_cookies_new()
