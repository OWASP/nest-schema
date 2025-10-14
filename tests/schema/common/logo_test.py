"""Test cases for the logo schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "logo"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("large_empty.yaml", "$.large: '' is not a 'uri'"),
        ("large_invalid.yaml", "$.large: 'image/large.png' is not a 'uri'"),
        ("large_null.yaml", "$.large: None is not of type 'string'"),
        ("large_undefined.yaml", "$: 'large' is a required property"),
        ("medium_empty.yaml", "$.medium: '' is not a 'uri'"),
        ("medium_invalid.yaml", "$.medium: 'image/medium.png' is not a 'uri'"),
        ("medium_null.yaml", "$.medium: None is not of type 'string'"),
        ("medium_undefined.yaml", "$: 'medium' is a required property"),
        ("small_empty.yaml", "$.small: '' is not a 'uri'"),
        ("small_invalid.yaml", "$.small: 'image/small.png' is not a 'uri'"),
        ("small_null.yaml", "$.small: None is not of type 'string'"),
        ("small_undefined.yaml", "$: 'small' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid logo schema cases."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid logo schema cases."""
    common_positive_test(common_schema, SCHEMA_NAME)
