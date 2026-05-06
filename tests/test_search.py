from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine


def test_search_chest_pain():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    results = search.search("боль в груди")

    ids = [result.card.id for result in results]
    assert "DIAG-SYMPTOM-002" in ids


def test_filter_emergency():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    cards = search.filter_by_urgency("emergency")

    assert any(card.id == "DIAG-EMERGENCY-001" for card in cards)
