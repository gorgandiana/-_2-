import urllib.request
import json


TOKEN = 'f10b1c123de6d6c6a729aee18640d19b61c10512'


def take_users():
    with open('users.txt', encoding='utf-8') as f:
        text = f.read()
    list_text = text.split(', ')
    user = input('Введите имя пользователя: ')
    while user not in list_text:
        print('Пользователя {0} нет в списке. Пожалуйста повторите ввод: '.format(user))
        user = input('Введите имя пользователя: ')
    return list_text, user


def repos_description(user):
    url = 'https://api.github.com/users/{0}/repos?access_token={1}&per_page=100'.format(user, TOKEN)
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    json_raw = json.loads(text)  # список словарей, но в питоне воспринимается как файл в формате json
    repos_dict = {}
    for i in json_raw:
        name = i['name']
        description = i['description']  # первое - название переменной, второе в кавычках это сам ключ в словаре
        language = i['language']
        repos_dict[name] = [description, language]
    return repos_dict


def repos_print(repos_dict, user):
    print('Репозитории пользователя {0}: '.format(user))
    for key in repos_dict.keys():
        if repos_dict[key][0] is not None:
            print('{0}:\t{1}'.format(key, repos_dict[key][0]))  #[0] и [1] - description и language в массиве
        else:
            print('{0}:\t'.format(key))


def languages(repos_dict, user):
    langs = []
    for key in repos_dict.keys():
        lang = repos_dict[key][1]
        if lang is not None and lang not in langs:
            langs.append(lang)
    print('Пользователь {0} использует языки: {1}'.format(user, ', '.join(langs)))
    return langs


def count_langs(langs, repos_dict):   #{} словарь,
    for i in langs:
        reps = []
        for key in repos_dict.keys():
            if repos_dict[key][1] == i:
                reps.append(key)
        print('Язык {0} используется в {1} репозиториях'.format(i, str(len(reps))))


def data(users):
    data_users = {}
    for user in users:
        try:
            url = 'https://api.github.com/users/{0}?access_token={1}'.format(user, TOKEN)
            response = urllib.request.urlopen(url)
            text = response.read().decode('utf-8')
            json_raw = json.loads(text)
            data_users[user] = [json_raw['public_repos'], json_raw['followers']]
        except Exception as e:
            print(e)
    return data_users


def max_repos(data_users):
    num_reps = []
    for key in data_users.keys():
        num_reps.append(data_users[key][0])
    max_rep = max(num_reps)
    for key in data_users.keys():
        if data_users[key][0] == max_rep:
            print('У пользователя {0} наибольшее кол-во репозиториев ({1})'.format(key, max_rep))
            break


def max_followers(data_users):
    num_followers = []
    for key in data_users.keys():
        num_followers.append(data_users[key][1])
    max_followers = max(num_followers)
    for key in data_users.keys():
        if data_users[key][1] == max_followers:
            print('У пользователя {0} наибольшее кол-во подписчиков ({1})'.format(key, max_followers))
            break

        




def main():
    users = take_users()
    list_text = users[0]
    user = users[1]
    repos_dict = repos_description(user)
    repos_print(repos_dict, user)
    langs = languages(repos_dict, user)
    count_langs(langs, repos_dict)
    data_users = data(list_text)
    max_repos(data_users)
    max_followers(data_users)

main()

    
        



