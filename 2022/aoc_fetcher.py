import requests
import browser_cookie3

def get_data(year, day):
    cookies = browser_cookie3.firefox(domain_name='.adventofcode.com')
    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', verify=True, cookies=cookies, timeout=3)
    return response.text
