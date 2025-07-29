# Web Application Vulnerability Scanner

##Summary

This is a basic **Web Application Vulnerability Scanner** built in Python. It focuses on identifying potential **XSS (Cross Site Scripting)** vulnerabilities in `.php` web pages by injecting a harmless payload and checking the response.

The tool extracts internal links from a given target URL and scans each for reflected XSS vulnerabilities.

---

##Objective

To build a beginner-level automated tool that scans a website and detects possible **XSS vulnerabilities** by:

- Crawling internal links ending in `.php`
- Injecting a JavaScript payload
- Checking if the payload is reflected back in the response

---

##How It Works

1. The user enters the target URL (e.g., http://testphp.vulnweb.com).
2. The script uses **BeautifulSoup** to extract all internal `.php` links.
3. Each link is tested with a **basic XSS payload**:
   ```html
   <script>alert('XSS')</script># PROJECT
