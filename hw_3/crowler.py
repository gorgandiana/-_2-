import urllib.request
from bs4 import BeautifulSoup as soup
import download


def find_news(url):
    html = download.download(url)
    if html == 0:
        return 0
    soup_html = soup(html, "lxml")
    content = soup_html.select("div[class=\"content-center-block\"]")[0]
    list_href = []
    for link in content.find_all("a"):
        list_href.append(link.get("href"))
    list_url = []
    for i in list_href:
        i = str(i)
        if i.endswith(".html"):
            url = "http://izvestiaur.ru" + i
            if url not in list_url:
                list_url.append(url)
    return list_url


def main(num_of_pages):
    all_urls = []
    for i in range(1, num_of_pages + 1):
        urls = find_news("http://izvestiaur.ru/news/?PAGEN_1={0}".format(str(i)))
        if urls != 0:
            all_urls.extend(urls)
    return all_urls


if __name__ == "__main__":
    print(main(2))

