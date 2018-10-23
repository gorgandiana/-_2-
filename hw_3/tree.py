import os

def make_folders():
    root_directory = os.path.join(".", "izvestiaur")  #имя корневой директории
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)
        list_directories = ["plain", "mystem-xml", "mystem-plain"]
        for i in list_directories:
            directory = os.path.join(root_directory, i)
            for year in range(2004, 2019):
                directory_new = os.path.join(directory, str(year))
                for month in range(1, 13):
                    directory_month = os.path.join(directory_new, str(month))
                    if not os.path.exists(directory_month):
                        os.makedirs(directory_month)


if __name__ == "__main__":
    make_folders()
