import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import requests
from tqdm import tqdm

def main():
    # Chrome options configuration
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = os.environ.get('CHROME_BIN', '/usr/bin/chromium')

    # Initialize WebDriver with explicit service
    service = Service(executable_path=os.environ.get('CHROMEDRIVER_PATH', '/usr/bin/chromedriver'))
    driver = webdriver.Chrome(service=service, options=chrome_options)

    categories = {
        "red": "kirmizi",
        "orange": "turuncu",
        "yellow": "sari",
        "grey": "gri"
    }

    for keys, m_link in categories.items():
        main_link = "https://www.terorarananlar.pol.tr/tarananlar#" + m_link
        print(f"Processing category: {keys}")

        # Create directory
        os.makedirs(f"images/{keys}", exist_ok=True)

        try:
            driver.get(main_link)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            image_elements = soup.find_all(class_='deactivated-list-card-img position-relative')
            base_url = 'https://www.terorarananlar.pol.tr/'

            for img in tqdm(image_elements, desc=f"Downloading {keys} images"):
                style = img.get('style')
                if style:
                    match = re.search(r'background-image:\s*url\((.*?)\);', style)
                    if match:
                        relative_url = match.group(1)
                        full_url = base_url + relative_url.lstrip('/')
                        try:
                            image_response = requests.get(full_url)
                            filename = full_url.split('/')[-1]
                            with open(f"images/{keys}/{filename}", 'wb') as image:
                                image.write(image_response.content)
                        except Exception as e:
                            print(f"Error downloading image: {str(e)}")

        except Exception as e:
            print(f"Error processing category {keys}: {str(e)}")

    driver.quit()

if __name__ == "__main__":
    main()
