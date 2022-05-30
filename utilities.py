



def movie_by_title(title):
    db_connect = DbConnect('netflix.db')
    db_connect.cur.execute(
        f"""select title,country,release_year, listed_in, description
            from netflix
            where title like '%{title}%'
            order by  release_year desc
            limit 1""")
    result = db_connect.cur.fetchone()
    return {
        "title": result[0],
        "country": result[1],
        "release_year": result[2],
        "genre": result[3],
        "description": result[4]
    }


def movies_by_years(year1, year2):
    db_connect = DbConnect('netflix.db')
    query = f"""select title, release_year
                from netflix
                where release_year between {year1} and {year2}
                limit 100"""
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    result_list = []
    for movie in result:
        result_list.append({"title": movie[0],
                            "release_year": movie[1]})
    return result_list



    return