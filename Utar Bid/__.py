from bs4 import BeautifulSoup
import json

with open("bid.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

tr_list = soup.find_all("tr", align="center")
db = json.load(open("subject.json", "r"))


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
        print(_)
        if _ in db["UEEA2634"]:
            db["UEEA2634"].remove(_)
            sub_list.append(subject_config[key][_]["reqMid"])
            break
print(sub_list)
print(db)
