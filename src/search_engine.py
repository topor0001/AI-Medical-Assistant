"""Простой поисковый модуль базы знаний."""

from __future__ import annotations

from .models import KnowledgeCard, SearchResult, normalize_text
from .repository import KnowledgeRepository


class SearchEngine:
    """Выполняет поиск по карточкам базы знаний.

    Поиск специально сделан простым и прозрачным: он не использует ML и внешние
    сервисы, поэтому его легко объяснить на защите.
    """

    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def search(self, query: str, limit: int = 20) -> list[SearchResult]:
        """Ищет карточки по id, названию, тегам, категории, срочности и тексту."""

        normalized_query = normalize_text(query)
        if not normalized_query:
            return []

        results: list[SearchResult] = []
        for card in self.repository.all_cards():
            score, matched_by = self._score_card(card, normalized_query)
            if score > 0:
                results.append(SearchResult(card=card, score=score, matched_by=matched_by))

        results.sort(key=lambda item: (-item.score, item.card.id))
        return results[:limit]

    def filter_by_category(self, category: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_category.get(normalize_text(category), []))

    def filter_by_tag(self, tag: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_tag.get(normalize_text(tag), []))

    def filter_by_urgency(self, urgency: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_urgency.get(normalize_text(urgency), []))

    @staticmethod
    def _score_card(card: KnowledgeCard, query: str) -> tuple[int, list[str]]:
        score = 0
        matched_by: list[str] = []

        card_id = normalize_text(card.id)
        title = normalize_text(card.title)
        category = normalize_text(card.category)
        urgency = normalize_text(card.urgency)
        tags = [normalize_text(tag) for tag in card.tags]
        full_text = card.full_text_for_search()

        if query == card_id:
            score += 100
            matched_by.append("id")
        elif query in card_id:
            score += 70
            matched_by.append("id_part")

        if query == title:
            score += 90
            matched_by.append("title_exact")
        elif query in title:
            score += 60
            matched_by.append("title")

        if query == category:
            score += 50
            matched_by.append("category")

        if query == urgency:
            score += 40
            matched_by.append("urgency")

        if query in tags:
            score += 55
            matched_by.append("tag_exact")
        elif any(query in tag for tag in tags):
            score += 35
            matched_by.append("tag")

        if query in full_text:
            score += 15
            matched_by.append("content")

        # Поиск по отдельным словам запроса.
        words = [word for word in query.split() if len(word) >= 3]
        if words and all(word in full_text for word in words):
            score += 20
            matched_by.append("all_words")

        return score, matched_by
