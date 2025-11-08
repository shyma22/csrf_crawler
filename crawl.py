import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
visited=set()
def check_url(url):
    parsed_url=urlparse(url)
    return bool(parsed_url.netloc) and bool(parsed_url.scheme)
def get_form(url):
    soup=BeautifulSoup(requests.get(url).content,"html.parser")
    return soup.find_all("form")
def check_csrf(form):
    for input_tag in form.find_all("input"):
        if "csrf" in input_tag.get("name","").lower():
            return True
    return False
def crawl(url):
    if url in visited:
        return
    visited.add(url)
    print(f"[+] Scanning: {url}")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        forms = get_form(url)
        for form in forms:
            if not check_csrf(form):
                print(f"[!] CSRF Token Missing in form at: {url}")
    except Exception as e:
        print(f"[Error] {e}")
if __name__ == "__main__":
    target = input("Enter the website URL to scan: ").strip()
    crawl(target)