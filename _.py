import requests

cookies = {
    "csrftoken": "bOWXWZI2uz4f6irOYToFIoj37ot8dLDx882i4o4xprD6j7iVavYGNLX0c4VruNwZ",
    "sessionid": "tk6tfu76b8i6w5t0y32qwod03uab7y50",
}

headers = {
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # 'Cookie': 'csrftoken=bOWXWZI2uz4f6irOYToFIoj37ot8dLDx882i4o4xprD6j7iVavYGNLX0c4VruNwZ; sessionid=tk6tfu76b8i6w5t0y32qwod03uab7y50',
    "Origin": "https://esicw.cidblink.com",
    "Referer": "https://esicw.cidblink.com/courses/2/module/6/chapter/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Opera";v="103", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

data = {
    "csrfmiddlewaretoken": "4OKaetO7nAcB9hvX2InyM8QaZG4NMxVh18QvmSaCisLsm6m4ekXzRvu74mw63zOJ",
    "action": "update_content_progress",
    "duration": "99999",
    "complete": "true",
}

response = requests.post(
    "https://esicw.cidblink.com/courses/2/module/10/chapter/update_progress/",
    cookies=cookies,
    headers=headers,
    data=data,
)
with open("response.txt", "w+", encoding="utf-8") as f:
    f.write(response.text)
