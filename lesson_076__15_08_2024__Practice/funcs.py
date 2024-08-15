def show_cats(cursor) -> None:
    query = 'SELECT * FROM sakila.category;'
    cursor.execute(query)
    cats = [f'{c[0]:2d} {c[1]}' for c in cursor.fetchall()]

    print(*cats, sep='\n')


def show_movies(cursor, num_cat: str) -> None:
    query = f"""
        SELECT 
            f.title, f.release_year, f.description, c.film_id
        FROM
            sakila.film f
                LEFT JOIN
            sakila.film_category c ON c.film_id = {num_cat} LIMIT 10;
    """
    cursor.execute(query)
    movies = cursor.fetchall()
    print(*movies, sep='\n')
