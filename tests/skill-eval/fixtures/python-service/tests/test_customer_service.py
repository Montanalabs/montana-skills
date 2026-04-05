from src.customer_service import normalize_customer_name


def test_normalize_customer_name_collapses_internal_whitespace() -> None:
    assert normalize_customer_name("  Ada   Lovelace  ") == "Ada Lovelace"
