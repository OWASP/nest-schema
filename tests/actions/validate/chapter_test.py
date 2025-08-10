"""Tests for the GitHub Action validator script on chapter files."""

import pytest
from actions.validate import main as action

from tests.conftest import tests_data_dir


@pytest.fixture
def mock_workspace(tmp_path, monkeypatch):
    """Fixture to mock the GitHub workspace."""
    monkeypatch.setattr(action, "WORKSPACE_PATH", tmp_path)
    return tmp_path


@pytest.mark.parametrize(
    ("filename", "expected_error"),
    [
        ("blog_empty.yaml", "'' is not a 'uri'"),
        ("chapter_empty.yaml", "None is not of type 'object'"),
    ],
)
def test_negative(mock_workspace, capsys, filename, expected_error):
    """Test that invalid chapter files fail validation."""
    (mock_workspace / "chapter.owasp.yaml").write_text(
        (tests_data_dir / "actions/validate/chapter/negative" / filename).read_text(),
    )

    with pytest.raises(SystemExit) as exit_info:
        action.main()

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: Validation failed!" in captured.err
    assert expected_error in captured.err


def test_positive(mock_workspace, capsys):
    """Test that a valid chapter file passes validation."""
    (mock_workspace / "chapter.owasp.yaml").write_text(
        (tests_data_dir / "actions/validate/chapter/positive/valid_chapter.yaml").read_text(),
    )

    with pytest.raises(SystemExit) as exit_info:
        action.main()

    assert exit_info.value.code == 0
    captured = capsys.readouterr()
    assert "SUCCESS: Validation passed!" in captured.out
