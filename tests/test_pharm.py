from src.linker import Linker
from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine


def test_pharm_cards_are_loaded():
    repo = KnowledgeRepository("kb").load()

    assert repo.get_by_id("PHARM-DRUG-001") is not None
    assert repo.get_by_id("PHARM-DRUG-002") is not None
    assert repo.get_by_id("PHARM-DRUGCLASS-001") is not None
    assert repo.get_by_id("PHARM-REGIMEN-001") is not None
    assert repo.get_by_id("PHARM-INTERACTION-001") is not None
    assert repo.get_by_id("PHARM-ADR-001") is not None
    assert repo.get_by_id("PHARM-DOSING-001") is not None
    assert repo.get_by_id("PHARM-NONPHARM-001") is not None


def test_pharm_regimen_links_are_resolved():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("PHARM-REGIMEN-001")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-001" in target_ids
    assert "PROT-PROTOCOL-001" in target_ids
    assert "PHARM-DRUG-001" in target_ids
    assert "PHARM-DRUG-002" in target_ids
    assert all(not item.is_missing for item in related)


def test_search_pharm_drug_and_interaction():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    enalapril_ids = [result.card.id for result in search.search("эналаприл")]
    interaction_ids = [result.card.id for result in search.search("метформин контраст")]

    assert "PHARM-DRUG-001" in enalapril_ids
    assert "PHARM-INTERACTION-001" in interaction_ids
