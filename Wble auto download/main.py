import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
from threading import Thread

cookies = {
    "_gcl_au": "1.1.253385308.1695707420",
    "_hjSessionUser_2382141": "eyJpZCI6ImFjMTM3OGY0LWNjMWYtNTMxMS1iNWJhLTBkYjA2ZjE5MGYyMCIsImNyZWF0ZWQiOjE2OTU3MDc0MjEwNDcsImV4aXN0aW5nIjpmYWxzZX0=",
    "twk_uuid_5e6f2c5a8d24fc226587c56e": "%7B%22uuid%22%3A%221.70gh3ORvMZ8s9OXdePJnndNJ6UxcxY3MluIb3VVnUKKduspTy5T9nmDkNVmZ5hLBorqXHxyPjtZRMQ17GExwfY20AXOQ6usX7FvKIUjCxjCQJqvm7BXb%22%2C%22version%22%3A3%2C%22domain%22%3A%22utar.edu.my%22%2C%22ts%22%3A1695707422611%7D",
    "_ga_6K76WHHYJ7": "GS1.1.1695707420.1.0.1695707429.51.0.0",
    "_ga": "GA1.1.775589891.1694591203",
    "_ga_RWQ0EW0BZB": "GS1.1.1695708550.2.0.1695708553.0.0.0",
    "MoodleSessionTestewbleSL": "9pmhiAc03X",
    "MoodleSessionewbleSL": "at63hikd262fsmt7ku3ua73rm4",
    "MOODLEID_ewbleSL": "%25B1%259CN%251D%25E7%252B%25E1",
}
headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https://ewble-sl.utar.edu.my/course/view.php?id=14389",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://ewble-sl.utar.edu.my",
}

s = requests.Session()
s.headers = headers
s.cookies.update(cookies)

folder_path = Path("Subject [69]")

if not folder_path.exists():
    folder_path.mkdir()


def main(url):
    response = s.get(
        url,
    )
    # soup = BeautifulSoup()

    with open("test.html", "w+", encoding="utf-8") as f:
        f.write(response.text)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the href attributes
    hrefs = [a.get("href") for a in soup.find_all("a")]
    folder_name = soup.title.string.split(": ")[1]
    folder_name = re.sub(r"[^a-zA-Z0-9\s]", "", folder_name).replace("  ", " ")

    # Create the folder using Path
    folder_path = Path(f"Subject [69]/{folder_name}")

    # Check if the folder already exists, and create it if it doesn't
    if not folder_path.exists():
        folder_path.mkdir()

    # Print the hrefs
    for href in hrefs:
        print(href)
        if "view.php" not in href or href.startswith("http") is False:
            continue
        r = s.get(href)
        filename = r.headers.get("Content-Disposition")
        if filename is not None:
            filename = filename.split('filename="')[1].split('"')[0].replace("_", " ")
            print(filename)

            with open(f"{folder_path}/{filename}", mode="wb+") as f:
                f.write(r.content)


r = s.get("https://ewble-sl.utar.edu.my/")
soup = BeautifulSoup(r.text, "html.parser")

# Find all the href attributes
hrefs = [a.get("href") for a in soup.find_all("a")]
download_list = []
for link in hrefs:
    if "https://ewble-sl.utar.edu.my/course/view.php?id=" in link:
        download_list.append(link)

print(download_list)
# quit()
for url in download_list:
    Thread(target=main, args=(url,)).start()
