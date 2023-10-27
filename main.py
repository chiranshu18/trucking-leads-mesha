# state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

import requests
from bs4 import BeautifulSoup

base_url = "https://www.quicktransportsolutions.com/quickfreight/loadboard/carrier-searchby-citystate.php?page={}&companyname=&phy_state={}&phy_city=&trucks=None&tractors=None&searchmode=3"

# Create a dictionary where the keys are state codes and the values are the associated page numbers
state_pages = {
    'AL': 885,
    'AK': 127,
    'AZ': 796,
    'AR': 421,
    'CA': 8644,
    'CO': 1024,
    'CT': 432,
    'DE': 100,
    'DC': 100,
    'FL': 100,
    'GA': 100,
    'HI': 100,
    'ID': 100,
    'IL': 100,
    'IN': 100,
    'IA': 100,
    'KS': 100,
    'KY': 100,
    'LA': 100,
    'ME': 100,
    'MD': 100,
    'MA': 100,
    'MI': 100,
    'MN': 100,
    'MS': 100,
    'MO': 100,
    'MT': 100,
    'NE': 100,
    'NV': 100,
    'NH': 100,
    'NJ': 100,
    'NM': 100,
    'NY': 100,
    'NC': 100,
    'ND': 100,
    'OH': 100,
    'OK': 100,
    'OR': 100,
    'PA': 100,
    'PR': 100,  
    'RI': 100,
    'SC': 100,
    'SD': 100,
    'TN': 100,
    'TX': 100,
    'UT': 100,
    'VT': 100,
    'VA': 100,
    'WA': 100,
    'WV': 100,
    'WI': 100,
    'WY': 100,
    'AB': 100,
    'BC': 100,
    'MB': 100,
    'NB': 100,
    'NL': 100,
    'NS': 100,
    'NT': 100,
    'NU': 100,
    'ON': 100,
    'PE': 100,
    'QC': 100,
    'SK': 100,
    'YT': 100,
}

# Create a list to store all the links
all_links = []

for state_code, max_page in state_pages.items():
    for page in range(1, max_page + 1):
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
                    print("State:", state_code, "Page:", page, "Link:", href)  # Print state, page, and link
                    all_links.append(href)  # Add the link to the all_links list

        else:
            print("Failed to fetch the page for state", state_code, "and page", page, "Status code:", response.status_code)

# Now, all_links contains all the links from all states and pages

