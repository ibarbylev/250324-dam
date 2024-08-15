def show_cats(cursor) -> None:
    query = 'SELECT * FROM sakila.category;'
    cursor.execute(query)
    cats = [f'{c[0]:2d} {c[1]}' for c in cursor.fetchall()]

    print(*cats, sep='\n')


def show_movies(cursor, num_cat: str) -> None:
    query = f"""
        SELECT 
            f.title,
            f.release_year,
            f.description,
            c.film_id,
            GROUP_CONCAT(DISTINCT name.last_name
                SEPARATOR ', ') actors
        FROM
            sakila.film f
                LEFT JOIN
            sakila.film_category c ON c.film_id = {num_cat}
                LEFT JOIN
            sakila.film_actor a ON a.film_id = c.film_id
                LEFT JOIN
            sakila.actor name ON name.actor_id = a.actor_id
        GROUP BY name.last_name
        LIMIT 10;
    """
    cursor.execute(query)
    movies = cursor.fetchall()
    print(*movies, sep='\n')


# SELECT
#     f.title,
#     f.release_year,
#     f.description,
#     c.film_id,
#     GROUP_CONCAT(DISTINCT name.last_name
#         SEPARATOR ', ') actors
# FROM
#     sakila.film f
#         LEFT JOIN
#     sakila.film_category c ON c.film_id = f.film_id
#         LEFT JOIN
#     sakila.film_actor a ON a.film_id = c.film_id
#         LEFT JOIN
#     sakila.actor name ON name.actor_id = a.actor_id
# GROUP BY name.last_name
# LIMIT 10