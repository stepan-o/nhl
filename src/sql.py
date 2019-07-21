def create_nhl_draft(table_name, data_path):
    """
    SQL query to create new table with NHL Draft data
    :return:
    """
    query = (
        """
        drop table if exists '{0}'; 
        """.format(table_name),
        """
        create table '{0}'
        (
            csplayerid integer,
            name       varchar(35),
            nat        char(3),
            b_date     date,
            b_place    varchar(50),
            b_city     varchar(30),
            b_state    char(2),
            b_country  varchar(25),
            ateam      varchar(45),
            league     varchar(35),
            year       date,
            dteam      integer,
            overall    integer,
            round      integer,
            in_round   integer,
            height     numeric,
            weight     numeric,
            pos        varchar(2),
            shoots     char
        );
        """.format(table_name),
        """
        alter table '{0}'
            owner to nhl;
        """.format(table_name),
        """
        copy '{0}'
            from '{1}' DELIMITER ',' CSV HEADER;
        """.format(table_name, data_path),
        """
        alter table '{0}'
            add column id serial primary key;
        """.format(table_name)
        )
    return query


def test_nhl_draft(table_name):
    query = (
        """
        drop table if exists '{0}'; 
        """.format(table_name),
        """
        create table '{0}'
        (
            csplayerid integer,
            name       varchar(35),
            nat        char(3),
            b_date     date,
            b_place    varchar(50),
            b_city     varchar(30),
            b_state    char(2),
            b_country  varchar(25),
            ateam      varchar(45),
            league     varchar(35),
            year       date,
            dteam      integer,
            overall    integer,
            round      integer,
            in_round   integer,
            height     numeric,
            weight     numeric,
            pos        varchar(2),
            shoots     char
        );
        """.format(table_name),
        """
        alter table '{0}'
            owner to nhl;
        """.format(table_name)
    )
    return query
