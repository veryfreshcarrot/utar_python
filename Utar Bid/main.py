import json
import requests
from bs4 import BeautifulSoup


db = json.load(open("subject.json", "r"))
requests.packages.urllib3.disable_warnings()
# read the image

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://unitreg.utar.edu.my",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://unitreg.utar.edu.my/portal/courseRegStu/login.jsp?message=invalidSecurity",
    "Upgrade-Insecure-Requests": "1",
}


class Utar:
    session = requests.Session()
    session.verify = False
    session.headers = headers

    def __init__(self) -> None:
        pass

    def login(self, id, password):
        with open("cookies.json") as cook:
            cookies = json.load(cook)
            r = self.session.get(
                "https://unitreg.utar.edu.my/portal/courseRegStu/schedule/masterScheduleSurvey.jsp",
                cookies=cookies,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    "Connection": "keep-alive",
                    # 'Cookie': 'JSESSIONID=F165D3FF417DFFC6BD8FB237875D6BFF.server2; JSESSIONID=F165D3FF417DFFC6BD8FB237875D6BFF.server2',
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                },
                verify=False,
            )

        r = self.session.get(
            "https://unitreg.utar.edu.my/portal/courseRegStu/login.jsp"
        )

        r = self.session.get("https://unitreg.utar.edu.my/portal/Kaptcha.jpg")
        open("_.png", "wb").write(r.content)
        key = input("Key: ")
        data = {
            "preKap": "",
            "reqFregkey": id,
            "reqPassword": password,
            "kaptchafield": key,
        }

        r = self.session.post(
            "https://unitreg.utar.edu.my/portal/courseRegStu/loginProSurvey.jsp",
            data=data,
        )
        with open("cookies.json", "w") as fp:
            json.dump(self.session.cookies.get_dict(), fp, indent=4)

        if r.status_code == 200:
            print("Logged in.")
            with open("saving.html", "w", encoding="UTF-8") as f:
                f.write(r.text)
            self.full_name = r.text.split("<td>Welcome, ")[1].split(" (")[0]
            print(self.full_name)

            return True

    def bid(self, course_code):
        print(f"Registering {course_code}")
        data = {
            "reqPaperType": "M",
            "reqFregkey": "",
            "reqUnit": course_code,
            "Save": "View",
        }

        r = self.session.post(
            "https://unitreg.utar.edu.my/portal/courseRegStu/registration/registerUnitSurvey.jsp",
            data=data,
        )

        with open("bid.html", "wb+") as f:
            f.write(r.content)
        soup = BeautifulSoup(r.content, features="lxml")

        reqSid = soup.find("input", {"name": "reqSid"}).get("value")
        reqSession = soup.find("input", {"name": "reqSession"}).get("value")
        reqFregkey = soup.find("input", {"name": "reqFregkey"}).get("value")
        reqreqPaperTypeSid = soup.find("input", {"name": "reqPaperType"}).get("value")
        reqWithClass = soup.find("input", {"name": "reqWithClass"}).get("value")

        tr_list = soup.find_all("tr", align="center")

        subject_config = {}
        zz = ""
        for _ in tr_list:
            soup = BeautifulSoup(str(_), "html.parser")
            if 'name="reqMid"' in str(_):
                zz += f"{_}\n\n\n"
                _list = soup.find_all("td")
                _list = [str(item.string) for item in _list]

                if _list[1] not in subject_config:
                    subject_config[_list[1]] = {}

                subject_config[_list[1]][_list[1] + _list[2]] = {
                    "available_space": int(_list[11]),
                    "reqMid": soup.find("input").get("value"),
                }
        sub_list = []
        print(subject_config)
        for key, value in subject_config.items():
            for _ in value:
                if _ in db["UEEA2634"]:
                    sub_list.append(subject_config[key][_]["reqMid"])
                    break
        print(sub_list)

        data = {
            "reqUnit": course_code,
            "reqSid": reqSid,
            "reqSession": reqSession,
            "reqFregkey": reqFregkey,
            "reqPaperType": reqreqPaperTypeSid,
            "reqWithClass": reqWithClass,
            "act": "insert",
            "reqMid": sub_list,
        }

        # print(data)
        r = self.session.post(
            "https://unitreg.utar.edu.my/portal/courseRegStu/registration/registerUnitProSurvey.jsp",
            data=data,
        )

        if "Inserted Successfully" in r.text:
            print("Successfully Registered !")

        else:
            print("Insert failed !")
            with open(f"insert_error.html", "w", encoding="UTF-8") as f:
                f.write(r.text)


_ = Utar()
_.login("2001461", "sohminxuan01110687902!")
for subject in db:
    _.bid(subject)
