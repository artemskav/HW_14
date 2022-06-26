import sqlite3
from typing import Dict, Any


def search_films(title): # поиск по названию
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM netflix ORDER BY release_year DESC"""
        cursor.execute(query)
        result = cursor.fetchall()
    data_film = {}
    for film in result:
        if film[2] == title:
            data_film['title'] = film[2]
            data_film['country'] = film[5]
            data_film['release_year'] = film[7]
            data_film['genre'] = film[11]
            data_film['description'] = film[12]
    return data_film

def search_by_years(year_1, year_2): # поиск по годам
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = "SELECT title, release_year FROM netflix where release_year between ? and ? LIMIT 100 "

    cursor.execute(query, (year_1, year_2))
    result = cursor.fetchall()
    films_by_years = []
    for film in result:
        data_by_years = {}
        data_by_years["title"] = film[0]
        data_by_years["release_year"] = film[1]
        films_by_years.append(data_by_years)
    return films_by_years

def search_by_rating(query): # по рейтингу
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    film_by_rating = []
    for film in result:
        data_by_rating = {}
        data_by_rating["title"] = film[0]
        data_by_rating["rating"] = film[1]
        data_by_rating["description"] = film[2]
        film_by_rating.append(data_by_rating)
    return film_by_rating

def fresh_films(genre): # по жанру
    genre = genre.lower()
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM netflix where listed_in like '%{genre}%' ORDER BY release_year DESC LIMIT 10"
        cursor.execute(query)
        result = cursor.fetchall()
    search_fresh_films = []
    for film in result:
        data_film = {}
        data_film['title'] = film[2]
        data_film['description'] = film[12]
        search_fresh_films.append(data_film)
    return search_fresh_films

