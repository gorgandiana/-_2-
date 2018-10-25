import download
import metadata
import mystem
from bs4 import BeautifulSoup as soup
import tree
import crowler
import create_csv


tree.make_folders()
list_of_urls = crowler.main(2)
create_csv.create_csv()
for url in list_of_urls:
    if download.main(url) != 0:
        print("Страница {0} скачана".format(url))
        meta_data = metadata.main(url)
        print("Метаданные собраны")
        date = meta_data["created"]
        date = date.split(".")
        month = str(int(date[1]))  # чтобы убрать первый ноль в месяцах вроде мая
        year = date[2]
        num_page = url.split('/')[-1].split(".")[0]
        file_path = "izvestiaur\\plain\\{0}\\{1}\\{2}.txt".format(year, month, num_page)
        meta_data["path"] = file_path
        create_csv.append_to_csv(meta_data)
        with open("text.html", "r", encoding="utf-8") as f:
            text = f.read()
        soup_html = soup(text, "lxml")
        download.add_meta(url, meta_data)
        with open("plain_text.txt", encoding="utf-8") as f:
            file_text = f.read()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_text)
        mystem.mystem_plain(file_path)
        print("Файл добавлен в директорию mystem-plain")
        mystem.mystem_xml(file_path)
        print("Файл добавлен в директорию mystem-xml")

