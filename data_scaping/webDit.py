from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://th-deg.de/en"
visited = set()
output_file = "deg_campus_data.txt"

# Setup Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.netloc == "th-deg.de" and parsed.path.startswith("/en")

def scrape(url):
    if url in visited:
        return

    try:
        print(f"Scraping: {url}")
        driver.get(url)
        time.sleep(2)  # Wait for JS to load
        html = driver.page_source
    except Exception as e:
        print(f"Failed to load {url}: {e}")
        return

    visited.add(url)

    soup = BeautifulSoup(html, "html.parser")
    page_text = soup.get_text(separator="\n", strip=True)

    # Save content
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- {url} ---\n")
        f.write(page_text + "\n")

    # Find and crawl new links
    for tag in soup.find_all("a", href=True):
        link = urljoin(url, tag['href'])
        if is_valid_url(link) and link not in visited:
            scrape(link)

if __name__ == "__main__":
    print("🚀 Starting Selenium crawl...")
    scrape(BASE_URL)
    driver.quit()
    print(f"✅ Done. All content saved to: {output_file}")
