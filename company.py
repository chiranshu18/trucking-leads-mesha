import requests
from bs4 import BeautifulSoup
import csv

# Create an empty list to store all the data
all_data = []

# Load the CSV file with complete links
with open("utah_links.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        state_code, page, complete_link = row

        if page == "51":
            break

        # Fetch the HTML content of the link
        response = requests.get(complete_link)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the <address> tag
            address_tag = soup.find("address")

            if address_tag:
                # Find the <span> tags with different itemprop attributes and extract the text
                name_span = address_tag.find("span", itemprop="name")
                street_address_span = address_tag.find(
                    "span", itemprop="streetAddress")
                address_locality_span = address_tag.find(
                    "span", itemprop="addressLocality")
                address_region_span = address_tag.find(
                    "span", itemprop="addressRegion")
                postal_code_span = address_tag.find(
                    "span", itemprop="postalCode")

                telephone_span = address_tag.find("span", itemprop="telephone")

                if name_span:
                    company_name = name_span.text
                else:
                    company_name = "N/A"

                if street_address_span:
                    street_address = street_address_span.text
                else:
                    street_address = "N/A"

                if address_locality_span:
                    address_locality = address_locality_span.text
                else:
                    address_locality = "N/A"

                if address_region_span:
                    address_region = address_region_span.text
                else:
                    address_region = "N/A"

                if postal_code_span:
                    postal_code = postal_code_span.text
                else:
                    postal_code = "N/A"

                if telephone_span:
                    # Find the anchor tag within the telephone_span and extract its text
                    anchor = telephone_span.find("a")
                    if anchor:
                        telephone = anchor.text
                    else:
                        telephone = "N/A"
                else:
                    telephone = "N/A"

                print("State:", state_code, "Page:", page)
                print("Name:", company_name)
                print("Street Address:", street_address)
                print("Address Locality:", address_locality)
                print("Address Region:", address_region)
                print("Postal Code:", postal_code)
                print("Telephone:", telephone)
                print("--------------------------------------------")

                # Create a dictionary to store the data
                data = {
                    "Company Name": company_name,
                    "Street Address": street_address,
                    "Address Locality": address_locality,
                    "Address Region": address_region,
                    "Postal Code": postal_code,
                    "Telephone": telephone
                }

                all_data.append(data)

            else:
                print("No <address> tag found on", complete_link)
        else:
            print("Failed to fetch the page for state", state_code,
                  "and page", page, "Status code:", response.status_code)

# Save all the data to a CSV file
with open("utah_details.csv", "w", newline="") as csvfile:
    fieldnames = ["Company Name", "Street Address",
                  "Address Locality", "Address Region", "Postal Code", "Telephone"]
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()  # Write the header row
    csv_writer.writerows(all_data)  # Write the data rows

print("Extracted data saved to utah_details.csv")
