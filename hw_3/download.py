import urllib.request
from bs4 import BeautifulSoup as soup
import re
import metadata


def download(url):
    try:
        page = urllib.request.urlopen(url)
        page_html = page.read()
        soup_html = soup(page_html, "lxml")
        html = soup_html.prettify()  # исправляет html текст, кодировку и разные косяки, выводит в качестве красивого дерева
        return html
    except Exception as i:
        print("Возникла ошибка на странице " + url)
        print(i)
        return 0


def take_text(soup_html):
    all_div = soup_html.select("div[style=\"margin-top:5px;\"]")
    all_div = all_div[1:]
    text_list = []
    for item in all_div:
        text_list.append(item.get_text())
    with open("plain_text.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(text_list))


def prettify_text():
    with open("plain_text.txt", encoding="utf-8") as f:
        text_lines = f.readlines()
    formated_text = []
    for line in text_lines:
        if re.findall("[a-zA-Zа-яА-я]", line, re.DOTALL):  # не спотыкается о пробельные символы
            formated_text.append(line.strip())
    with open("plain_text.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(formated_text))


def add_meta(url, meta):
    author = meta["author"]
    header = meta["header"]
    created = meta["created"]
    topic = meta["topic"]
    meta_list = ["@au " + author, "@ti " + header, "@da " + created, "@topic " + topic, "@url " + url]
    with open("plain_text.txt", encoding="utf-8") as f:
        lines = f.readlines()
    meta_list.extend(lines)
    with open("plain_text.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(meta_list))


def main(url):
    text = download(url)
    if text != 0:
        with open("text.html", "w", encoding="utf-8") as f:
            f.write(text)
        soup_html = soup(text, "lxml")
        take_text(soup_html)
        prettify_text()
        return 1
    else:
        return 0

if __name__ == "__main__":
    main(url = "http://izvestiaur.ru/news/view/313.html")

