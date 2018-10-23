import os


def mystem_plain(file_path):
    try:
        mystem_path = os.path.join(".", "mystem.exe")
        file_path_mystem = file_path.replace("plain", "mystem-plain")
        os.system(mystem_path + " -cid " + file_path + " " + file_path_mystem)
    except Exception as e:
        print("Во время работы mystem произошла ошибка!")
        print(e)


def mystem_xml(file_path):
    try:
        mystem_path = os.path.join(".", "mystem.exe")
        file_path_mystem = file_path.replace("plain", "mystem-xml")
        os.system(mystem_path + " -cid --format xml " + file_path + " " + file_path_mystem)
    except Exception as e:
        print("Во время работы mystem произошла ошибка!")
        print(e)


if __name__ == "__main__":
    print(1)
