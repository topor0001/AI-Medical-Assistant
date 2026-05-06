from src.repository import KnowledgeRepository


def test_repository_loads_diagnostic_cards():
    repo = KnowledgeRepository("kb").load()

    assert len(repo.cards) >= 20
    assert repo.get_by_id("DIAG-SYMPTOM-002") is not None
    assert repo.get_by_id("DIAG-EMERGENCY-001") is not None
    assert not repo.parse_errors
