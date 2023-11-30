# state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.quicktransportsolutions.com/quickfreight/loadboard/carrier-searchby-citystate.php?page={}&companyname=&phy_state={}&phy_city=&trucks=None&tractors=None&searchmode=3"
prefix = "https://www.quicktransportsolutions.com/"

# Create a dictionary where the keys are state codes and the values are the associated page numbers
state_pages = {
    # 'AK': 127,
    # 'AL': 885,
    # 'AZ': 796,
    # 'AR': 421,
    # 'CA': 8644,
    # 'CO': 1024,
    # 'CT': 432,
    # 'DE': 161,
    # 'DC': 28,
    # 'FL': 4227,
    # 'GA': 2846,
    # 'HI': 20,
    # 'ID': 315,
    # 'IL': 1762,
    # 'IN': 1114,
    # 'IA': 643,
    # 'KS': 485,
    # 'KY': 896,
    # 'LA': 533,
    # 'ME': 277,
    # 'MD': 1051,
    # 'MA': 595,
    # 'MI': 1519,
    # 'MN': 1336,
    # 'MS': 582,
    # 'MO': 818,
    # 'MT': 233,
    # 'NE': 553,
    # 'NV': 355,
    # 'NH': 166,
    # 'NJ': 1592,
    # 'NM': 340,
    # 'NY': 2143,
    # 'NC': 1626,
    # 'ND': 207,
    # 'OH': 1442,
    # 'OK': 749,
    # 'OR': 660,
    # 'PA': 1805,
    # 'PR': 55,  
    # 'RI': 125,
    # 'SC': 764,
    # 'SD': 172,
    # 'TN': 844,
    # 'TX': 5786,
    'UT': 511,
    # 'VT': 79,
    # 'VA': 856,
    # 'WA': 1115,
    # 'WV': 293,
    # 'WI': 1177,
    # 'WY': 180,
    # 'AB': 141,
    # 'BC': 239,
    # 'MB': 75,
    # 'NB': 44,
    # 'NL': 57,
    # 'NS': 20,
    # 'NT': 100,---
    # 'NU': 100,---
    # 'ON': 441,
    # 'PE': 4,
    # 'QC': 222,
    # 'SK': 45,
    # 'YT': 3,
}

# Create a list to store all the links
all_links = []

for state_code, max_page in state_pages.items():
    # for page in range(1, max_page + 1):
    for page in range(1, 51):
        url = base_url.format(page, state_code)

        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            well_divs = soup.find_all("div", class_="well")

            for well_div in well_divs:
                anchor = well_div.find("a")
                if anchor:
                    href = anchor.get("href")
                    complete_link = prefix + href
                    print("State:", state_code, "Page:", page, "Link:", complete_link)  # Print state, page, and link
                    all_links.append([state_code, page, complete_link])  # Add the link to the all_links list
            
            # Now, all_links contains all the links from all states and pages


        else:
            print("Failed to fetch the page for state", state_code, "and page", page, "Status code:", response.status_code)


# Save the links to a CSV file with one link per row
with open("utah_links.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["State", "Page", "Link"])  # Write header row
    for link_details in all_links:
        csv_writer.writerow(link_details)  # Write each link separately

print("Links saved to utah_links.csv")