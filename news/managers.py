from __future__ import annotations

from django.db import models
from django.contrib.postgres.search import SearchRank, SearchVector, SearchQuery
import typing

if typing.TYPE_CHECKING:
    from typing import List, Dict


# https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/search/

class ArticleQuerySet(models.QuerySet):
    def rank_by_term(self, term: str, limit: int = 10):
        vector = SearchVector("description")
        query = SearchQuery(term)
        return self.annotate(rank=SearchRank(vector, query)).order_by("-rank")[:limit]

    def by(self, author: str):
        return self.filter(author=author)


class ArticleManager(models.Manager.from_queryset(ArticleQuerySet)):
    def create_from_response(self, json_response: List[Dict[str, str]]):
        for obj in json_response:
            self.create(
                title=obj["title"],
                author=obj["author"],
                description=obj["description"],
                url=obj["url"],
                content=obj[
                    "content"
                ],  # curated by API to 200 chars, useless at free tier
            )
