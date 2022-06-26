import sqlite3
import json
from collections import Counter

def two_actors(name_1, name_2): # 5 задача
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
    query = f"SELECT netflix.cast " \
            f"FROM netflix " \
            f"where netflix.cast like '%{name_1}%' and netflix.cast like '%{name_2}%'" \
            f"and netflix.cast != '' "
    result = connection.execute(query).fetchall()
    actors_list = [actor for film in result for actor in film]  # список строк с актерами
    actors_all = ''
    for i in range(len(actors_list)):   # объединение в одну строку всех списков с актерами
        actors_all += actors_list[i] + ","
    actors_all = [actor.strip(' ') for actor in actors_all.split(",")] # лишние пробелы и список из строки
    top_actor = Counter(actors_all) # функция Counter создает словарь с количеством одинаковых ключей в исходном списке
    for k, v in top_actor.items():
        if v >= 2 and k not in [name_1, name_2]:
            print(k)

two_actors('Rose McIver', 'Ben Lamb')

def films_by_query(typing, year, genre): # 6 задача
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        query = f"SELECT title, description FROM netflix where type = '{typing}' and release_year = '{year}' and netflix.listed_in like '%{genre}%' "
        result = dict(connection.execute(query).fetchall())
    return json.dumps(result, ensure_ascii=False, indent=2)

print(films_by_query("TV Show", "2011", "Dramas"))
