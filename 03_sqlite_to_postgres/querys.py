select_film_work = """SELECT 
                    id, 
                    title, 
                    description,
                    rating, 
                    "type",
                    created_at,
                    updated_at
                FROM main.film_work"""

insert_film_work = """INSERT INTO content.film_work
                   (id, 
                   title,
                   description,
                   rating,
                   "type",
                   created,
                   modified)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING """

select_genre = """SELECT 
                    id, 
                    name, 
                    description,
                    created_at,
                    updated_at
                FROM main.genre"""

insert_genre = """INSERT INTO content.genre 
                    (id, 
                    name, 
                    description,
                    created,
                    modified)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING"""

select_person = """SELECT 
                    id, 
                    full_name, 
                    created_at,
                    updated_at
                FROM main.person"""

insert_person = """INSERT INTO content.person
                   (id, 
                   full_name,
                   created,
                   modified)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT DO NOTHING """

select_genre_film_work = """SELECT 
                                id, 
                                film_work_id, 
                                genre_id,
                                created_at
                            FROM main.genre_film_work"""

insert_genre_film_work = """INSERT INTO content.genre_film_work
                               (id, 
                               filmwork_id,
                               genre_id,
                               created)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT DO NOTHING """

select_person_film_work = """SELECT 
                                id, 
                                film_work_id, 
                                person_id,
                                role,
                                created_at
                            FROM main.person_film_work"""

insert_person_film_work = """INSERT INTO content.person_film_work
                               (id, 
                                filmwork_id, 
                                person_id,
                                role,
                                created)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING"""
