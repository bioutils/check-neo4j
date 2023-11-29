# check-neo4j

simple script to check if a particular neo4j database is up and accessible

## Setup
(make virtualenv)
```
python -m venv venv
python activate venv
```

(install the python modules)
```
pip install -r requirements.txt
```

(set variables in an `.env` file, like below, see the file `.env-example`)
```
NEO4J_DATABASE_USERNAME="neo4j"
NEO4J_DATABASE_PASSWORD="neo4j"
NEO4J_DATABASE_NAME="neo4j"
NEO4J_DATABASE_URL="neo4j://localhost:7687"
```

Note: to connect to NCI neo4j dev instances, you would need to be behind the NCI firewall (i.e. VPN)

## Run
(run script)
```
python check_neo4j.py
```

(The script will either return the message `Yes the database is accessible` (indicating success), 
or it will return an error message of some sort)
