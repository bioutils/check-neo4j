# simple script to check if can connect to neo4j database

import os
from neo4j import GraphDatabase
from dotenv import load_dotenv


def check_database(tx):
    query = """
                RETURN 'Yes the database is accessible'
            """
    result = tx.run(query)
    return result.single()[0]


def simple_check():
    load_dotenv()

    URI = os.getenv("NEO4J_DATABASE_URL")
    NAME = os.getenv("NEO4J_DATABASE_NAME")
    USER = os.getenv("NEO4J_DATABASE_USERNAME")
    PASS = os.getenv("NEO4J_DATABASE_PASSWORD")

    driver = GraphDatabase.driver(URI, auth=(USER, PASS))

    with driver.session(database=NAME) as session:
        check = session.execute_read(check_database)
        print(check)

    driver.close()


if __name__ == "__main__":
    simple_check()
