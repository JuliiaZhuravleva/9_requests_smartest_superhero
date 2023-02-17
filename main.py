import requests


def get_all_heroes():
    url = base_url + '/all.json'
    resp = requests.get(url)
    json = resp.json()
    return json


def get_smartest_hero_name(list_of_heroes):
    smartest_hero_name = None
    smartest_hero_int = 0
    for h in list_of_heroes:
        h_int = h['powerstats']['intelligence']
        if h_int > smartest_hero_int:
            h_name = h['name']
            smartest_hero_name = h_name
            smartest_hero_int = h_int
    return smartest_hero_name


superheroes = ['Hulk', 'Captain America', 'Thanos']
base_url = 'https://akabab.github.io/superhero-api/api'
all_heroes = get_all_heroes()

compared_heroes = [hero for hero in all_heroes if hero['name'] in superheroes]

smartest_hero = get_smartest_hero_name(compared_heroes)

print(smartest_hero)