"""Test cases for the social-media schema validation."""

import pytest

from tests.conftest import common_negative_test, common_positive_test

SCHEMA_NAME = "social_media"


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("description_empty.yaml", "$.description: '' is too short"),
        ("description_null.yaml", "$.description: None is not of type 'string'"),
        (
            "platform_empty.yaml",
            "$.platform: '' is not one of ['bluesky', 'linkedin', 'mastodon', 'x', 'youtube', 'facebook']",
        ),
        (
            "platform_invalid.yaml",
            "$.platform: 'bitcoin' is not one of ['bluesky', 'linkedin', 'mastodon', 'x', "
            "'youtube', 'facebook']",
        ),
        (
            "platform_null.yaml",
            "$.platform: None is not one of ['bluesky', 'linkedin', 'mastodon', 'x', 'youtube', 'facebook']",
        ),
        ("platform_undefined.yaml", "$: 'platform' is a required property"),
        ("url_empty.yaml", "$.url: '' is not a 'uri'"),
        ("url_invalid.yaml", "$.url: 'https://bsky' is not a 'uri'"),
        ("url_null.yaml", "$.url: None is not of type 'string'"),
        ("url_undefined.yaml", "$: 'url' is a required property"),
    ],
)
def test_negative(common_schema, file_path, error_message):
    """Test invalid cases for the social-media schema."""
    common_negative_test(common_schema, SCHEMA_NAME, file_path, error_message)


def test_positive(common_schema):
    """Test valid cases for the social-media schema."""
    common_positive_test(common_schema, SCHEMA_NAME)
