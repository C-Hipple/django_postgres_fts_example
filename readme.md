# Postgres Full Text Search via Django

This is a simple docker compose app which has a two management commands:

`load_articles` which takes a search keyword argument and queries a service called `newsapi` to load 100 news articles related to your search term into postgres

`search_by_term` which takes a keyword argument and performs a full text search against the `descriptions` of the news articles, and 

## Installation

Clone the repo, then follow the setup steps:

1. Build container and set API key as environment variable

```
touch .env
echo NEWSAPI_API_KEY=<Our API key> > .env
docker compose build
```

2. Ensure django's postgres database has migrations applied
```
docker compose run --rm web python manage.py migrate
```

Done!

## Usage

The easiest way to then run commands is to do so from inside the container

```
docker compose run --rm web bash
```

Then you have direct access to django management tools:

```
python manage.py load_articles <term>
python manage.py search_by_term <keyword>
```

You can also open a django shell_plus if you'd like to play with your own queries

```
python manage.py shell_plus
```

### Running commands directly via compose

You can also run the commands externally if you'd like

```
docker compose run web python manage.py load_articles <term>
docker compose run web python manage.py search_by_term <keyword>
```

## Contributing
Just open a PR, or push to master, I'm a readme, not a cop.



