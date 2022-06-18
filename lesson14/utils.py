import sqlite3


def search_by_name(title):
    """поиск по временному интервалу"""
    with sqlite3.connect("netflix.db") as base:
        cursor = base.cursor()
        query = (f"\n"
                 f"            select title, country, release_year, listed_in, description\n"
                 f"            FROM netflix\n"
                 f"            WHERE title like '%{title}%'\n"
                 f"            AND type = 'Movie'\n"
                 f"            order by release_year desc\n"
                 f"            limit 1\n"
                 f"           ")
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        return {"title": data[0],
                "country": data[1],
                "release_year": data[2],
                "genre": data[3],
                "description": data[4]
                }


def search_by_years(year1, year2):
    """поиск по временному интервалу"""
    with sqlite3.connect("netflix.db") as base:
        cursor = base.cursor()
        query = (f"\n"
                 f"            select title, release_year \n"
                 f"            FROM netflix\n"
                 f"            WHERE  release_year between {year1} AND {year2} \n"
                 f"            AND type = 'Movie'\n"
                 f"            limit 100\n"
                 f"           ")
        cursor.execute(query)
        data = cursor.fetchall()
        resalt = []
        for movie in data:
            resalt.append({'title': movie[0],
                           'release_year': movie[1]})
        cursor.close()
        return resalt


def search_by_rating(lvl):
    """поиск по возрастным ограничениям"""
    rating_lvl = {
        "children": "'G'",
        "family": "'G', 'PG', PG-13",
        "adult": "'G', 'NC-17'"
    }
    if lvl not in ['children', 'family', 'adult']:
        return f'такой категории нет'

    with sqlite3.connect("netflix.db") as base:
        cursor = base.cursor()
        query = (f"\n"
                 f"            select title, rating, description\n"
                 f"            FROM netflix\n"
                 f"            WHERE  rating in ({rating_lvl[lvl]})\n"
                 f"            AND type = 'Movie'\n"
                 )
        cursor.execute(query)
        data = cursor.fetchall()
        resalt = []
        for movie in data:
            resalt.append({'title': movie[0],
                           'rating': movie[1],
                           'description': movie[2]})
        cursor.close()
        return resalt


def search_by_listed_in(genre):
    """поиск по заданному жарну"""
    with sqlite3.connect("netflix.db") as base:
        cursor = base.cursor()
        query = (f"""
            SELECT title, description, listed_in, release_year
            FROM netflix
            WHERE listed_in like '%{genre}%'
            order by release_year desc 
            LIMIT 10
        """)
        cursor.execute(query)
        data = cursor.fetchall()
        resalt = []
        for movie in data:
            resalt.append({'title': movie[0],
                           'description': movie[1]})
        cursor.close()
        return resalt


def acter_list(acter1, acter2):
    '''поиск по актёрам, которые играли с заданными'''
    with sqlite3.connect("netflix.db") as base:
        """при вызове столбца cast выдаёт ошибку, 
        все остальные столбцы выводятся, пришлось городить костили"""
        cursor = base.cursor()
        query = ("""
        select *
        from netflix
        """)
        cursor.execute(query)
        data = cursor.fetchall()
        temp_string = ''
        resalt1 = ''
        resalt2 = ''
        resalt_acter1 = []
        resalt_acter2 = []
        for acters in data:
            if acter1 in acters[4]:
                temp_string += acters[4]
                resalt1 = temp_string.split(', ')
            if acter2 in acters[4]:
                temp_string += acters[4]
                resalt2 = temp_string.split(', ')

        for acter in resalt1:
            if resalt1.count(acter) > 2 and acter1 != acter:
                resalt_acter1.append(acter)
        for acter in resalt2:
            if resalt2.count(acter) > 2 and acter2 != acter:
                resalt_acter2.append(acter)

        cursor.close()
        return list(set(resalt_acter1)), list(set(resalt_acter2))


# print(acter_list('Rose McIver', 'Ben Lamb')) тест поиска по парам актёров


def search_by_list(tipe, genre, year):
    """поиск по заданному жарну"""
    with sqlite3.connect("netflix.db") as base:
        cursor = base.cursor()
        query = (f"""
            SELECT type, title, description, listed_in, release_year
            FROM netflix
            WHERE listed_in like '%{genre}%'
            AND type like '%{tipe}%'
            AND release_year == {year}
            order by title desc
        """)
        cursor.execute(query)
        data = cursor.fetchall()
        resalt = []
        for movie in data:
            resalt.append({'title': movie[1],
                           'description': movie[2]})
        cursor.close()
        return resalt