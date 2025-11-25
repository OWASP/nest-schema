"""Project schema tests."""

from pathlib import Path

import pytest
import yaml

from owasp_schema.utils.schema_validators import validate_data
from tests.conftest import tests_data_dir


@pytest.mark.parametrize(
    ("file_path", "error_message"),
    [
        (
            "audience_invalid.yaml",
            "$.audience[0]: 'hacker' is not one of ['breaker', 'builder', 'defender']",
        ),
        ("audience_empty.yaml", "$.audience: [] should be non-empty"),
        ("audience_null.yaml", "$.audience: None is not of type 'array'"),
        ("audience_undefined.yaml", "$: 'audience' is a required property"),
        ("blog_empty.yaml", "$.blog: '' is not a 'uri'"),
        ("blog_invalid.yaml", "$.blog: 'https://invalid/' is not a 'uri'"),
        ("blog_null.yaml", "$.blog: None is not a 'uri'"),
        ("community_empty.yaml", "$.community: [] should be non-empty"),
        (
            "community_non_unique.yaml",
            "$.community: [{'platform': 'discord', 'url': 'https://discord.com/example'}, "
            "{'platform': 'discord', 'url': 'https://discord.com/example'}] "
            "has non-unique elements",
        ),
        ("community_null.yaml", "$.community: None is not of type 'array'"),
        ("demo_empty.yaml", "$.demo: [] should be non-empty"),
        ("demo_invalid.yaml", "$.demo[0]: 'https://invalid/' is not a 'uri'"),
        (
            "demo_non_unique.yaml",
            "$.demo: ['https://example.com/', 'https://example.com/'] has non-unique elements",
        ),
        ("demo_null.yaml", "$.demo: None is not of type 'array'"),
        ("documentation_empty.yaml", "$.documentation: [] should be non-empty"),
        (
            "documentation_invalid.yaml",
            "$.documentation[0]: 'xyz-abc' is not a 'uri'",
        ),
        (
            "documentation_non_unique.yaml",
            "$.documentation: ['https://example.com/docs', "
            "'https://example.com/docs'] has non-unique elements",
        ),
        ("documentation_null.yaml", "$.documentation: None is not of type 'array'"),
        ("downloads_empty.yaml", "$.downloads: [] should be non-empty"),
        (
            "downloads_invalid.yaml",
            "$.downloads[0]: 'xyz-abc' is not a 'uri'",
        ),
        (
            "downloads_non_unique.yaml",
            "$.downloads: ['https://abc.com/download', "
            "'https://abc.com/download'] has non-unique elements",
        ),
        ("downloads_null.yaml", "$.downloads: None is not of type 'array'"),
        ("events_empty.yaml", "$.events: [] should be non-empty"),
        (
            "events_non_unique.yaml",
            "$.events: [{'url': 'https://example.com/event1'}, "
            "{'url': 'https://example.com/event1'}] has non-unique elements",
        ),
        ("events_null.yaml", "$.events: None is not of type 'array'"),
        ("leaders_empty.yaml", "$.leaders: [] should be non-empty"),
        (
            "leaders_max.yaml",
            "$.leaders: [{'name': 'Leader One'}, {'name': 'Leader Two'}, "
            "{'name': 'Leader Three'}, {'name': 'Leader Four'}, {'name': 'Leader Five'}, "
            "{'name': 'Leader Six'}] is too long",
        ),
        (
            "leaders_non_unique.yaml",
            "$.leaders: [{'github': 'leader1'}, {'github': 'leader1'}] has non-unique elements",
        ),
        ("leaders_null.yaml", "$.leaders: None is not of type 'array'"),
        ("leaders_undefined.yaml", "$: 'leaders' is a required property"),
        ("level_invalid.yaml", "$.level: 2.5 is not one of [2, 3, 3.5, 4]"),
        ("level_undefined.yaml", "$: 'level' is a required property"),
        (
            "license_invalid.yaml",
            "$.license[0]: 'INVALID-LICENSE-VALUE' is not one of ['AGPL-3.0', "
            "'Apache License 2.0', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', "
            "'CC-BY-4.0', 'CC-BY-NC-ND-4.0', 'CC-BY-SA-4.0', 'CC0-1.0', 'EUPL-1.2', "
            "'GPL-2.0', 'GPL-3.0', 'LGPL-2.1', 'LGPL-3.0', 'MIT', 'MPL-2.0', 'OTHER']",
        ),
        ("logo_empty.yaml", "$.logo: [] should be non-empty"),
        ("logo_null.yaml", "$.logo: None is not of type 'array'"),
        (
            "logo_non_unique.yaml",
            "$.logo: [{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}, "
            "{'small': 'https://example.com/smallLogo.png', "
            "'medium': 'https://example.com/mediumLogo.png', "
            "'large': 'https://example.com/largeLogo.png'}] has non-unique elements",
        ),
        ("mailing_list_empty.yaml", "$.mailing_list: '' is not of type 'array'"),
        ("mailing_list_invalid.yaml", "$.mailing_list: 'https://xyz' is not of type 'array'"),
        ("mailing_list_null.yaml", "$.mailing_list: None is not of type 'array'"),
        ("name_empty.yaml", "$.name: '' is too short"),
        ("name_invalid.yaml", "$.name: 'Name' is too short"),
        ("name_null.yaml", "$.name: None is not of type 'string'"),
        ("name_undefined.yaml", "$: 'name' is a required property"),
        ("pitch_empty.yaml", "$.pitch: '' is too short"),
        ("pitch_null.yaml", "$.pitch: None is not of type 'string'"),
        ("pitch_undefined.yaml", "$: 'pitch' is a required property"),
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
            "$.social_media: [{'platform': 'x', 'url': 'https://x.com'}, "
            "{'platform': 'x', 'url': 'https://x.com'}] has non-unique elements",
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
        ("tags_null.yaml", "$.tags: None is not of type 'array'"),
        (
            "tags_non_unique.yaml",
            "$.tags: ['example-tag-1', 'example-tag-1', 'example-tag-1'] has non-unique elements",
        ),
        ("type_empty.yaml", "$.type: '' is not one of ['code', 'documentation', 'tool']"),
        ("type_null.yaml", "$.type: None is not one of ['code', 'documentation', 'tool']"),
        ("type_undefined.yaml", "$: 'type' is a required property"),
        ("website_empty.yaml", "$.website: '' is not a 'uri'"),
        ("website_null.yaml", "$.website: None is not a 'uri'"),
    ],
)
def test_negative(project_schema, file_path, error_message):
    assert (
        validate_data(
            project_schema,
            yaml.safe_load(
                Path(tests_data_dir / "schema/project/negative" / file_path).read_text(),
            ),
        )
        == error_message
    )


def test_positive(project_schema):
    for file_path in Path(tests_data_dir / "schema/project/positive").rglob("*.yaml"):
        assert (
            validate_data(
                project_schema,
                yaml.safe_load(
                    file_path.read_text(),
                ),
            )
            is None
        )
