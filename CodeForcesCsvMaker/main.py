import csv
import requests
from bs4 import BeautifulSoup


def get_parsed(url):
    response = requests.get(url)
    parsed = BeautifulSoup(response.content, "html.parser")
    return parsed


def get_codeforces_links(url):
    parsed = get_parsed(url)
    divs = parsed.find_all('div', attrs={'style': 'float: left;'})
    links = []
    for div in divs:
        links += div.find_all('a')
    links_dic = [{"name": link.text, "url": "https://codeforces.com" + link['href']}
                 for link in links if 'problem' in link['href']]
    return links_dic


def get_progvar_links(url):
    response = requests.get(url)
    return response.json()['results']


def write_csv(file_name, headers, content):
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for data in content:
            writer.writerow(data)


def main():
    url = str(input("Enter Sheet Url: "))
    file_name = str(input("Enter file name: "))
    if "progvar" in url:
        links = get_progvar_links(url)
        write_csv(file_name, ["__str__", "url",
                  "solved_count", "dacu", "number"], links)
    else:
        links = get_codeforces_links(url)
        write_csv(file_name, ['name', 'url'], links)


if __name__ == "__main__":
    main()
