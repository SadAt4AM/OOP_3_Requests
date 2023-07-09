import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

heroes = ['Hulk', 'Captain America', 'Thanos']

def max_inta(url, heroes):
    respond = requests.get(url).json()
    #список индексов героев
    index_hero = [i for i in range(len(respond)) if respond[i].get('name') in heroes]
    dictionary = dict()
    for x in index_hero:
        #сопоставление имен и показателей, да, сперва идет показатель, потом только имя
        dictionary.setdefault((respond[x].get('powerstats').get('intelligence')), [])
        dictionary[respond[x].get('powerstats').get('intelligence')].append(respond[x].get('name'))

    return ', '.join(dictionary[max(dictionary.keys())])


print('Список героев для сравнения: ', *[hero + ',' for hero in heroes],)

print('Самый умный герой: ', max_inta(url, heroes))
