from bs4 import BeautifulSoup as soup


def get_meta(soup_html, url):
    dict_meta = {"path": " ", "author": "Noname", "header": " ", "created": " ", "sphere": "публицистика", "topic": " ",
                 "style": "нейтральный", "audience_age": "н-возраст",	"audience_level": "н-уровень",
                 "audience_size": "республиканская",	"source": url,	"publication": "Известия Удмуртской республики",
                 "publ_year": " ",	"medium": "газета", "country": "Россия", "region": "Удмуртская республика",
                 "language": "русский"}
    dict_meta["header"] = get_title(soup_html).strip()
    dict_meta["created"] = get_date(soup_html).strip()
    dict_meta["topic"] = get_topic(soup_html).strip()
    dict_meta["publ_year"] = get_year(soup_html).strip()
    return dict_meta


def get_title(soup_html):
    try:
        title = soup_html.title.string
        return title
    except Exception as e:
        print("Заголовок не найден!")
        print(e)
        return "unknown"


def get_topic(soup_html):
    try:
        topic = soup_html.select("div[class=\"news-name\"]")
        topic = topic[0]
        topic = topic.get_text()
        topic = topic.split()
        topic = topic[2]
        return topic
    except Exception as e:
        print("Тема не найдена")
        print(e)
        return "unknown"


def get_date(soup_html):
    date = soup_html.select("div[class=\"article-date\"]")[0]
    try:
        date = date.get_text().strip()
        date = date.split()[0:3]
        if "январ" in date[1]:
            date[1] = "01"
        elif "феврал" in date[1]:
            date[1] = "02"
        elif "март" in date[1]:
            date[1] = "03"
        elif "апрел" in date[1]:
            date[1] = "04"
        elif "мая" in date[1]:
            date[1] = "05"
        elif "июн" in date[1]:
            date[1] = "06"
        elif "июл" in date[1]:
            date[1] = "07"
        elif "август" in date[1]:
            date[1] = "08"
        elif "сентябр" in date[1]:
            date[1] = "09"
        elif "октябр" in date[1]:
            date[1] = "10"
        elif "ноябр" in date[1]:
            date[1] = "11"
        elif "декабр" in date[1]:
            date[1] = "12"
        return ".".join(date)
    except Exception as e:
        print("Дата не найдена на странице!")
        print(e)
        return "unknown"


def get_year(soup_html):
    if get_date(soup_html) == "unknown":
        return "unknown"
    year = get_date(soup_html).split(".")[2]
    return year


def main(url):
    with open("text.html", "r", encoding="utf-8") as f:
        text = f.read()
    soup_html = soup(text, "lxml")
    meta_data = get_meta(soup_html, url)
    return meta_data


if __name__ == "__main__":  #если запускать файл через другую программу, нужно чтобы работала не вся функци
    url = "http://izvestiaur.ru/news/view/313.html"
    main(url)

