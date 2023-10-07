import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
from threading import Thread
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
cookies = {
    "JSESSIONID": "FD416B179C0BB5E7F02D5CA09B1144C8",
    "sysid": "a6c6287c-fb59-49a3-8615-46e38d0f26fc",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate',
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://portal.utar.edu.my",
    "Connection": "keep-alive",
    "Referer": "http://portal.utar.edu.my/stuIntranet/examination/pastPaper/pastPaperSearch.jsp",
    # 'Cookie': 'sysid=a6c6287c-fb59-49a3-8615-46e38d0f26fc; JSESSIONID=2C4721306F73A3C27E0E07217D590584',
    "Upgrade-Insecure-Requests": "1",
}
s = requests.Session()
s.headers = headers
s.cookies.update(cookies)
s.verify = False


def obtain_download_list():
    response = s.post(
        "https://portal.utar.edu.my/stuIntranet/examination/pastPaper/pastPaperSearch.jsp",
        headers=headers,
        cookies=cookies,
        data=data,
    )
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the <a> tag inside the <td> and extract the 'href' attribute
    elements_with_onclick = soup.find_all(attrs={"onclick": True})
    # Extract the "onclick" attribute value from each element
    download_bucket = []
    for element in elements_with_onclick:
        download_url = f"""https://portal.utar.edu.my/stuIntranet/examination/pastPaper/{element.get("onclick").split("'")[1]}"""
        download_bucket.append(download_url)
    return download_bucket


def downloader(url):
    r = s.get(url)
    filename = r.headers.get("Content-Disposition")
    if filename is not None:
        filename = filename.split("filename=")[1].replace("_", " ")

        # Use regular expression to split the string
        match = re.match(r"([A-Za-z0-9]+) ([A-Za-z]+)(\d{4})(\.pdf)", filename)

        if match:
            course_code, month, year, file_extension = match.groups()
            # Reformat the string
            filename = f"[{year}] {course_code} {month}{file_extension}"
            folder_path = Path(f"./Past Year/{course_code}")
            # https://portal.utar.edu.my/stuIntranet/examination/pastPaper/downloadFile.jsp?text=78312.pdfz&fname=UEMH4333_SEPTEMBER2022
            # Check if the folder already exists, and create it if it doesn't
            if not folder_path.exists():
                folder_path.mkdir()
        else:
            print("Invalid input format.")

        with open(f"{folder_path}/{filename}", mode="wb+") as f:
            f.write(r.content)


if __name__ == "__main__":
    subject = input("Subject Name / Course Code >> ")
    data = {"reqKey": subject, "submit": "Quick Search"}

    folder_path = Path("./Past Year")

    if not folder_path.exists():
        folder_path.mkdir()

    download_list = obtain_download_list()

    for url in download_list:
        Thread(target=downloader, args=(url,)).start()
