from src.repository import KnowledgeRepository
from src.validator import KnowledgeBaseValidator


def test_validator_has_no_errors():
    repo = KnowledgeRepository("kb").load()
    report = KnowledgeBaseValidator(repo).validate()

    assert report.is_valid, report.to_markdown()
