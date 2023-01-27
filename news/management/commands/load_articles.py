import os
import httpx

from django.core.management.base import BaseCommand, CommandError
from news.models import Article

BASE_URL = "https://newsapi.org/v2/everything"
API_KEY = os.environ.get("NEWSAPI_API_KEY", "")


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("keyword", type=str, default="Internet")

    def handle(self, *args, **options):
        params = {"apiKey": API_KEY, "q": options['keyword']}
        if API_KEY == "":
            raise CommandError("The API key is not set.")

        resp: httpx.Response = httpx.get(BASE_URL, params=params)
        # not bothering with pagination in demo
        print(f"adding {len(resp.json()['articles'])} news articles")
        if resp.status_code == 200:
            Article.objects.create_from_response(resp.json()['articles'])
        else:
            raise CommandError(f"Status: {resp.status_code}: {resp.json()['message']}")

