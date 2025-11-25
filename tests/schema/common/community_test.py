"""Test cases for the community schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "community"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("description_empty.yaml", "$.description: '' is too short"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("name_undefined.yaml", "$: 'name' is a required property"),
        (
            "platform_empty.yaml",
            "$.platform: '' is not one of ['discord', 'github-discussions', 'matrix', "
            "'reddit', 'slack']",
        ),
        (
            "platform_invalid.yaml",
            "$.platform: 'telegram' is not one of ['discord', 'github-discussions', 'matrix', "
            "'reddit', 'slack']",
        ),
        (
            "platform_null.yaml",
            "$.platform: None is not one of ['discord', 'github-discussions', 'matrix', "
            "'reddit', 'slack']",
        ),
        ("platform_undefined.yaml", "$: 'platform' is a required property"),
        ("url_empty.yaml", "$.url: '' is not a 'uri'"),
        ("url_invalid.yaml", "$.url: 'discord.com/invalid' is not a 'uri'"),
        ("url_null.yaml", "$.url: None is not a 'uri'"),
        ("url_undefined.yaml", "$: 'url' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid community schema cases."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid community schema cases."""
    common_positive_test(common_schema, SCHEMA_NAME)
