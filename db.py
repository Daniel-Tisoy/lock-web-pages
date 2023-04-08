import sqlite3


class DbQueries:
    """Class to automate sqlite3 queries,
    required: database name
    """

    def __init__(self, db_name, table_name, sites_column, id_column):

        self.db_name = db_name
        self.table_name = table_name
        self.sites_column = sites_column
        self.id_column = id_column

    def create_table(self):
        """format an sql query string with the given variables

        Args:
            table_name (string): table name
            parameters (string): column names with their
              respective configuration, separated by commas
        """
        sql_query = f'CREATE TABLE {self.table_name} (?)'
        self.execute_query(sql_query, self.column)
        print("create table succesfully")

    def list_data(self):
        """list all the data in the fiven table name
        takes the given table name in the instantiation


        Returns:
            list: list of tuples with all the data
            example: [(id, "name", age),(id, "name", age)]
        """
        sql_query = f"SELECT * FROM {self.table_name}"
        result = self.execute_query(sql_query).fetchall()
        return result

    def add(self, url):
        """inserts a record in a table
            the given url will be the input in the sql string
        this functionn will modify the given url so it will
       with the sqlite execute parameter

        Args:
            url (string): in this case is the website url to block
        """

        url = (url,)
        sql_query = f'INSERT INTO {self.table_name}({self.sites_column}) VALUES (?)'
        self.execute_query(sql_query, url)
        print("record added succesfully")

    def delete(self, id):
        """deletes a record by given id

        Args:
            id (string): id of the website in the database

        """
        query = f"DELETE FROM {self.table_name} WHERE {self.id_column}= ?"
        self.execute_query(query, (id,))

    def execute_query(self, query, parameters=()):
        """makes a sql query with sqlite3 format

        Args:
            query (string): sql query string
            parameters (tuple, optional): variables needed
             when the query has "?" inside. Defaults to ().

        Returns:
            Object: sqlite3 cursor ready to fetch if it contains data
        """

        with sqlite3.connect(self.db_name) as conection:
            cursor = conection.cursor()
            result = cursor.execute(query, parameters)
            conection.commit()

        return result
