import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
                            CREATE TABLE IF NOT EXISTS songplays 
                            (       
                                artist              varcahr,               
                                auth                varchar,
                                firstName           varchar,
                                gender              varchar,
                                itemInSession       int,
                                lastName            varchar,
                                lenght              float,
                                level               varchar,
                                location            varchar,
                                method              varchar,
                                page                varchar,
                                registration        int,
                                sessionId           int,
                                song                varchar,
                                status              int,
                                ts                  timestamp,
                                userAgent           varchar,
                                userId              varchar
                            )
                            """)

staging_songs_table_create = ("""
                                num_songs             int,
                                artist_id             varchar,
                                artist_latitude       real,
                                artist_longitude      real,
                                artist_location       varchar,
                                artist_name           varchar,
                                song_id               varchar,
                                title                 varchar,
                                duration              float,
                                year                  int
                            """)

songplay_table_create = ("""
                        CREATE TABLE IF NOT EXISTS songplays 
                        (
                          songplay_id      SERIAL           PRIMARY KEY,
                          start_time       timestamp        NOT NULL,
                          user_id          int              NOT NULL,
                          level            varchar,
                          song_id          int              NOT NULL, 
                          artist_id        int              NOT NULL, 
                          session_id       int,
                          location         varchar, 
                          user_agent       varchar,
                        )
                        """)

user_table_create = ("""
                    CREATE TABLE IF NOT EXISTS users 
                    (
                        user_id         int             PRIMARY KEY, 
                        first_name      varchar, 
                        last_name       varchar, 
                        gender          varchar, 
                        level           varchar
                    )
                    """)

song_table_create = ("""
                    CREATE TABLE IF NOT EXISTS songs 
                    (
                        song_id       varchar         PRIMARY KEY, 
                        title         varchar         NOT NULL, 
                        artist_id     varchar, 
                        year          int, 
                        duration      float           NOT NULL
                    )
                    """)

artist_table_create = ("""
                       CREATE TABLE IF NOT EXISTS artists 
                       (
                           artist_id      varchar     PRIMARY KEY, 
                           name           varchar     NOT NULL, 
                           location       varchar, 
                           latitude       real, 
                           longitude      real
                        )
                        """)

time_table_create = ("""
                    CREATE TABLE IF NOT EXISTS time 
                    (
                        start_time       timestamp    PRIMARY KEY, 
                        hour             int, 
                        day              int, 
                        week             int, 
                        month            int, 
                        year             int, 
                        weekday          int
                    )
                    """)

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
