#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv
import time


def scrape_headlines(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Unable to open website")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all(["h1", "h2", "h3"])

    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])

        for headline in headlines:
            text = headline.get_text(strip=True)

            if text:
                writer.writerow([text])
                print(text)

            time.sleep(0.2)

    print("Headlines saved to headlines.csv")


def main():
    url = input("Enter website URL: ")
    scrape_headlines(url)


if __name__ == "__main__":
    main()
