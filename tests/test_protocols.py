from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine
from src.linker import Linker


def test_protocol_cards_are_loaded():
    repo = KnowledgeRepository("kb").load()

    assert repo.get_by_id("PROT-PROTOCOL-001") is not None
    assert repo.get_by_id("PROT-EMERGENCY_P-001") is not None
    assert repo.get_by_id("PROT-FOLLOW_UP-001") is not None


def test_protocol_related_cards_are_resolved():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("PROT-PROTOCOL-001")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-001" in target_ids
    assert "PROT-ROUTING-001" in target_ids
    assert "PHARM-REGIMEN-001" in target_ids
    assert all(not item.is_missing for item in related)


def test_search_hypertension_protocol():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    results = search.search("артериальная гипертензия протокол")
    ids = [result.card.id for result in results]

    assert "PROT-PROTOCOL-001" in ids
