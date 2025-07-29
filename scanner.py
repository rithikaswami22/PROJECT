from urllib.parse import urljoin
from colorama import Fore, Style
import requests
from bs4 import BeautifulSoup

def show_banner():
    print(Fore.CYAN + "="*50)
    print("      Web App Vulnerability Scanner ")
    print("="*50 + Style.RESET_ALL)

def get_internal_links(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        links = [urljoin(url, link.get("href")) for link in soup.find_all("a") if link.get("href") and link.get("href").endswith(".php")]
        return links
    except:
        return []


def scan_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        res = requests.get(url + "?input=" + payload)
        if payload in res.text:
            print(Fore.RED + f"[!] XSS found at: {url}" + Style.RESET_ALL)
            return True
        else:
            print(Fore.GREEN + f"[-] No XSS at: {url}" + Style.RESET_ALL)
            return False
    except:
        print(Fore.YELLOW + f"[x] Could not connect to: {url}" + Style.RESET_ALL)
        return None

# ========================= MAIN =============================
show_banner()
target = input("Enter website URL (with http:// or https://): ")
pages = get_internal_links(target)
print("[DEBUG] Links to scan:")
for link in pages:
    print(link)
print(f"\n[+] Found {len(pages)} internal links. Starting XSS scan...\n")

with open("scan_results.txt", "w") as file:
    for link in pages:
        result = scan_xss(link)
        if result:
            file.write(f"[!] XSS found at: {link}\n")
        elif result == False:
            file.write(f"[-] No XSS at: {link}\n")
        else:
            file.write(f"[x] Could not connect to: {link}\n")
