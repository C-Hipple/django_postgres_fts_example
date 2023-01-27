from django.core.management.base import BaseCommand
from news.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("term", type=str)

    def handle(self, *args, **options):
        results = Article.objects.rank_by_term(options["term"])
        for result in results:
            print(result.rank, result.title)
