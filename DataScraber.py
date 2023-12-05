import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time


def scraper():
    data = []
    url = "https://finviz.com/insidertrading.ashx"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tr_elements = soup.find_all('tr')

        for tr in tr_elements:
            if tr.th:
                continue

            td = tr.find_all('td')
            row_data = {}
            if len(td) == 10:
                # Extract and store data based on the column headers
                row_data['Ticker'] = td[0].text.strip()
                row_data['Owner'] = td[1].text.strip()
                row_data['Relationship'] = td[2].text.strip()
                row_data['Date'] = td[3].text.strip()
                row_data['Transaction'] = td[4].text.strip()
                row_data['Cost'] = td[5].text.strip()
                row_data['#Shares'] = td[6].text.strip()
                row_data['Value ($)'] = td[7].text.strip()
                row_data['#Shares Total'] = td[8].text.strip()
                row_data['Timestamp'] = td[9].text.strip()
            data.append(row_data)

    # Specify the CSV file path
    csv_file_path = 'data/buy_transactions.csv'

    # Extract and save only 'Buy' transactions
    buy_entries = [entry for entry in data if entry.get('Transaction') == 'Buy']

    # Extract prices for 'Buy' transactions
    buy_prices = [float(entry['Cost'].replace('$', '').replace(',', '')) for entry in buy_entries]

    # Write the data to the CSV file
    with open(csv_file_path, 'a', newline='') as csv_file:
        fieldnames = ['Ticker', 'Owner', 'Relationship', 'Date', 'Transaction', 'Cost', '#Shares', 'Value ($)',
                      '#Shares Total', 'Timestamp']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for entry in buy_entries:
            writer.writerow(entry)
    print("finished csv filing the csv file")

schedule.every().day.at("16:00").do(scraper)

while True:
    schedule.run_pending()
    time.sleep(1)
