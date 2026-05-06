from src.linker import Linker
from src.repository import KnowledgeRepository


def test_related_cards_for_chest_pain():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("DIAG-SYMPTOM-002")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-002" in target_ids
    assert "DIAG-EMERGENCY-001" in target_ids
    assert "DIAG-DIFDIAG-001" in target_ids
    assert all(not item.is_missing for item in related)
