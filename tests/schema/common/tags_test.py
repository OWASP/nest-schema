"""Test cases for the tags schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "tags"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("empty.yaml", "$: [] is too short"),
        ("item_invalid.yaml", "$[1]: 2 is not of type 'string'"),
        (
            "non_unique.yaml",
            "$: ['example-tag-1', 'example-tag-1', 'example-tag-1'] has non-unique elements",
        ),
        ("null.yaml", "$: None is not of type 'array'"),
        ("too_short.yaml", "$: ['example-tag-1', 'example-tag-2'] is too short"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid tags schema cases."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid tags schema cases."""
    common_positive_test(common_schema, SCHEMA_NAME)
