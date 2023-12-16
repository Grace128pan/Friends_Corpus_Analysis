from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import csv
import time

# Function to convert FlexJobs' date format to a datetime object
def convert_to_datetime(date_text):
    try:
        if "New!" in date_text:
            return datetime.now()
        elif "today" in date_text:
            return datetime.now()
        elif "days ago" in date_text:
            days_ago = int(date_text.split()[0])
            return datetime.now() - timedelta(days=days_ago)
        elif "weeks ago" in date_text:
            weeks_ago = int(date_text.split()[0])
            return datetime.now() - timedelta(weeks=weeks_ago)
        else:
            return None
    except ValueError:
        return None

def find_jobs():
    print("Put some skill that you are not familiar with")
    unfamiliar_skill = input(">")
    print(f"Filtering out jobs requiring {unfamiliar_skill}")

    html_text = requests.get("https://www.flexjobs.com/search?search=python&location=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="m-0 row job clickable")

    # Set the threshold for the latest two weeks
    two_weeks_ago = datetime.now() - timedelta(weeks=2)

    # Create a CSV file and write headers
    csv_file_path = "C:\\Users\\grace\\PycharmProjects\\Jupyter coding\\scraped_jobs.csv"
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Company Location", "Required Skills", "Published Date", "More Info"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write headers to the CSV file
        writer.writeheader()

        # Iterate through jobs and write data to the CSV file
        for job in jobs:
            company_location = job.find_all("div", class_="col pe-0 job-locations text-truncate")
            skills = job.find_all("div", class_="job-description")
            more_info = job.div.a["href"]
            published_date = job.find_all("div", class_="job-age")

            # Extract text from multiple elements using get_text()
            company_location_text = ' '.join([location.get_text(strip=True) for location in company_location])
            skills_text = ' '.join([skill.get_text(strip=True) for skill in skills])
            published_date_text = ' '.join([date.get_text(strip=True) for date in published_date])

            # Convert published_date_text to a datetime object
            published_datetime = convert_to_datetime(published_date_text)

            # Check if the job is within the latest two weeks and does not require unwanted skill
            if (
                published_datetime
                and published_datetime >= two_weeks_ago
                and unfamiliar_skill.lower() not in skills_text.lower()
            ):
                # Write data to the CSV file
                writer.writerow({
                    "Company Location": company_location_text,
                    "Required Skills": skills_text,
                    "Published Date": published_date_text,
                    "More Info": more_info
                })

                print("Data written to CSV file.")

        print("Iteration completed.")

find_jobs()