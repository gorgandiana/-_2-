import csv


def create_csv():
    meta_data = ["path", "author", "header", "created", "sphere", "topic",
                 "style", "audience_age",	"audience_level",
                 "audience_size",	"source",	"publication",
                 "publ_year",	"medium", "country", "region",
                 "language"]
    new_list = []
    new_list.append(meta_data)
    with open("izvestiaur\\meta_data.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(new_list)


def append_to_csv(meta_data):
    meta_data = meta_data.values()
    new_list = []
    new_list.append(meta_data)
    with open("izvestiaur\\meta_data.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(new_list)
