import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import requests
from tqdm import tqdm
def atakan():
    pass
def main():
    # Chrome options configuration
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.binary_location = os.environ.get('CHROME_BIN', '/usr/bin/chromium')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    categories = {
        "red": "kirmizi",
        "orange": "turuncu",
        "yellow": "sari",
        "grey": "gri"
    }

    for keys, m_link in categories.items():
        main_link = "https://www.terorarananlar.pol.tr/tarananlar#" + m_link
        driver.refresh()
        print(f"Processing category: {keys}")

        # Create directory
        category_dir = f"images/{keys}"
        os.makedirs(category_dir, exist_ok=True)

        try:
            driver.get(main_link)
            time.sleep(1.5)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            image_elements = soup.find_all(class_='deactivated-list-card-img position-relative')
            base_url = 'https://www.terorarananlar.pol.tr/'

            # Get community data only once outside the loop
            community = soup.select('.deactivated-list-card-content')
            last_span_texts = [com.find_all('span')[-1].get_text(strip=True).replace("/", "_") for com in community if com.find_all('span')]

            for img, last_span_text in zip(image_elements, last_span_texts):
                style = img.get('style')
                if style:
                    match = re.search(r'background-image:\s*url\((.*?)\);', style)
                    if match:
                        relative_url = match.group(1)
                        full_url = base_url + relative_url.lstrip('/')
                        try:
                            image_response = requests.get(full_url)
                            filename = full_url.split('/')[-1]

                            subdir = os.path.join(category_dir, last_span_text)
                            os.makedirs(subdir, exist_ok=True)

                            with open(f"{subdir}/{filename}", 'wb') as image_file:
                                image_file.write(image_response.content)

                        except Exception as e:
                            print(f"Error downloading image: {str(e)}")

        except Exception as e:
            print(f"Error processing category {keys}: {str(e)}")

    driver.quit()

if __name__ == "__main__":
    main()
