"""Test cases for the community schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "community"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("description_empty.yaml", "'' is too short"),
        ("description_null.yaml", "None is not of type 'string'"),
        ("name_empty.yaml", "'' is too short"),
        ("name_null.yaml", "None is not of type 'string'"),
        ("name_undefined.yaml", "'name' is a required property"),
        ("platform_empty.yaml", "'' is not one of ['discord', 'slack', 'github-discussions']"),
        ("platform_invalid.yaml", "'telegram' is not one of ['discord', 'slack', 'github-discussions']"),
        ("platform_null.yaml", "None is not one of ['discord', 'slack', 'github-discussions']"),
        ("platform_undefined.yaml", "'platform' is a required property"),
        ("url_empty.yaml", "'' is not a 'uri'"),
        ("url_invalid.yaml", "'discord.com/invalid' is not a 'uri'"),
        ("url_null.yaml", "None is not a 'uri'"),
        ("url_undefined.yaml", "'url' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid community schema cases."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid community schema cases."""
    common_positive_test(common_schema, SCHEMA_NAME)
