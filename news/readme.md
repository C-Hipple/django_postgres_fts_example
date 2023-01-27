
# Postgres Full Text Search via Django

This is a simple docker compose app which has a two management commands

`load_articles`

which takes a search keyword argument and queries a service called `newsapi` to load 100 news articles related to your search term into postgres


`search_by_term`




## Installation

Clone the repo, 

```
echo 
docker compose build

docker compose run --rm web python manage.py migrate
```
