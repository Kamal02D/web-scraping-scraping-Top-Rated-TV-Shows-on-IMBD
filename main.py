# scraping the top 250 series and copy them as json to a file
from bs4 import BeautifulSoup
import requests
import lxml
import json
import time
print("getting data ...")
url = requests.get("https://www.imdb.com/chart/toptv/", headers={"Accept-Language": "en-US,en;q=0.5"})
html = url.text
soup = BeautifulSoup(html, "lxml")
list = soup.find("tbody" , class_="lister-list").find_all("tr")
date = time.localtime(time.time())
date = f"{date.tm_year}/{date.tm_mon}/{date.tm_mday}"
#(date)
result = {"scraping_date": date}
list_series = []
for elm in list:
    poster = elm.findNext("td", class_="posterColumn")
    rank = poster.find("span", {"name" : "rk"})["data-value"]
    rating = poster.find("span", {"name" : "ir"})["data-value"]
    titleColumn = elm.findNext("td", class_="titleColumn")
    title = titleColumn.find("a").text
    release = titleColumn.find("span" , class_="secondaryInfo").text
    release = release[1:len(release)-1]
    release = int(release)
    img_link = poster.img["src"]

    obj_serie = {
           "name": title,
           "release_year": release,
           "rank": rank,
           "rating": rating,
           "poster": img_link
    }
    list_series.append(obj_serie)
result["data"] = list_series
print(f"writing data into : C:\\Users\\user\\Desktop\\scraping_{date.replace('/','_')}.json")
with open(f"C:\\Users\\user\\Desktop\\scraping_{date.replace('/','_')}.json" , "w") as f:
    f.write(json.dumps(result, indent=2))
print("done")