from pathlib import Path

from src.markdown_parser import parse_markdown_file


def test_parse_markdown_card():
    path = Path("kb/diagnostics/symptoms/diag_symptom_chest_pain.md")
    card = parse_markdown_file(path)

    assert card.id == "DIAG-SYMPTOM-002"
    assert card.title == "Боль в груди"
    assert card.category == "symptom"
    assert "chest_pain" in card.tags
    assert "Боль в груди" in card.content
