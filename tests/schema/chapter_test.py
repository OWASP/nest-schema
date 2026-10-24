"""Chapter schema tests."""

from pathlib import Path

import pytest
import yaml

from owasp_schema.utils.schema_validators import validate_data
from tests.conftest import tests_data_dir


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        ("blog_empty.yaml", "$.blog: '' is not a 'uri'"),
        ("blog_invalid.yaml", "$.blog: 'invalid-blog-uri' is not a 'uri'"),
        ("blog_null.yaml", "$.blog: None is not a 'uri'"),
        ("community_empty.yaml", "$.community: [] should be non-empty"),
        (
            "community_non_unique.yaml",
            "$.community: [{'platform': 'discord', 'url': 'https://discord.com/example'}, "
            "{'platform': 'discord', 'url': 'https://discord.com/example'}] "
            "has non-unique elements",
        ),
        ("community_null.yaml", "$.community: None is not of type 'array'"),
        ("currency_empty.yaml", "$.currency: '' does not match '^[A-Z]{3}$'"),
        ("currency_invalid_length.yaml", "$.currency: 'US' does not match '^[A-Z]{3}$'"),
        ("currency_invalid_lowercase.yaml", "$.currency: 'usd' does not match '^[A-Z]{3}$'"),
        ("event_platforms_empty.yaml", "$.event_platforms: [] should be non-empty"),
        (
            "event_platforms_non_unique.yaml",
            "$.event_platforms: [{'platform': 'connpass', 'url': 'https://example.connpass.com'}, "
            "{'platform': 'connpass', 'url': 'https://example.connpass.com'}] "
            "has non-unique elements",
        ),
        ("event_platforms_null.yaml", "$.event_platforms: None is not of type 'array'"),
        ("events_empty.yaml", "$.events: [] should be non-empty"),
        (
            "events_non_unique.yaml",
            "$.events: [{'url': 'https://example.com/event1'}, "
            "{'url': 'https://example.com/event1'}] has non-unique elements",
        ),
        ("events_null.yaml", "$.events: None is not of type 'array'"),
        ("leaders_empty.yaml", "$.leaders: [] should be non-empty"),
        (
            "leaders_non_unique.yaml",
            "$.leaders: [{'github': 'leader1'}, {'github': 'leader1'}] has non-unique elements",
        ),
        ("leaders_null.yaml", "$.leaders: None is not of type 'array'"),
        ("leaders_undefined.yaml", "$: 'leaders' is a required property"),
        ("location_empty.yaml", "$.location: 'country' is a required property"),
        ("location_null.yaml", "$.location: None is not of type 'object'"),
        ("location_undefined.yaml", "$: 'location' is a required property"),
        ("logo_empty.yaml", "$.logo: [] should be non-empty"),
        (
            "logo_non_unique.yaml",
            "$.logo: [{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}, "
            "{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}] has non-unique elements",
        ),
        ("logo_null.yaml", "$.logo: None is not of type 'array'"),
        ("mailing_list_empty.yaml", "$.mailing_list: '' is not of type 'array'"),
        ("mailing_list_invalid.yaml", "$.mailing_list: 'https://xyz' is not of type 'array'"),
        ("mailing_list_null.yaml", "$.mailing_list: None is not of type 'array'"),
        ("meetup_group_empty.yaml", "$.meetup_group: '' should be non-empty"),
        ("meetup_group_null.yaml", "$.meetup_group: None is not of type 'string'"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("name_undefined.yaml", "$: 'name' is a required property"),
        ("repositories_empty.yaml", "$.repositories: [] should be non-empty"),
        (
            "repositories_non_unique.yaml",
            "$.repositories: [{'url': 'https://repo1.com'}, "
            "{'url': 'https://repo1.com'}] has non-unique elements",
        ),
        ("repositories_null.yaml", "$.repositories: None is not of type 'array'"),
        ("social_media_empty.yaml", "$.social_media: [] should be non-empty"),
        (
            "social_media_non_unique.yaml",
            "$.social_media: [{'platform': 'youtube', 'url': 'https://youtube.com/channel/123'}, "
            "{'platform': 'youtube', 'url': 'https://youtube.com/channel/123'}] "
            "has non-unique elements",
        ),
        ("social_media_null.yaml", "$.social_media: None is not of type 'array'"),
        ("sponsors_empty.yaml", "$.sponsors: [] should be non-empty"),
        (
            "sponsors_non_unique.yaml",
            "$.sponsors: [{'name': 'CyberSec Corp', 'url': 'https://cybersec.com'}, "
            "{'name': 'CyberSec Corp', 'url': 'https://cybersec.com'}] has non-unique elements",
        ),
        ("sponsors_null.yaml", "$.sponsors: None is not of type 'array'"),
        ("tags_empty.yaml", "$.tags: [] is too short"),
        (
            "tags_non_unique.yaml",
            "$.tags: ['example-tag-1', 'example-tag-1', 'example-tag-1'] has non-unique elements",
        ),
        ("tags_null.yaml", "$.tags: None is not of type 'array'"),
        ("tags_undefined.yaml", "$: 'tags' is a required property"),
        ("website_empty.yaml", "$.website: '' is not a 'uri'"),
        ("website_null.yaml", "$.website: None is not a 'uri'"),
    ],
)
def test_negative(chapter_schema, file_path, error_message):
    assert (
        validate_data(
            chapter_schema,
            yaml.safe_load(
                Path(tests_data_dir / "schema/chapter/negative" / file_path).read_text(),
            ),
        )
        == error_message
    )


def test_positive(chapter_schema):
    for file_path in Path(tests_data_dir / "schema/chapter/positive").rglob("*.yaml"):
        assert (
            validate_data(
                chapter_schema,
                yaml.safe_load(
                    file_path.read_text(),
                ),
            )
            is None
        )
