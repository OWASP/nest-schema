"""Tests for the GitHub Action validator script on project files."""

import pytest
import validate as validator

from tests.conftest import tests_data_dir


@pytest.fixture
def mock_workspace(tmp_path, monkeypatch):
    """Fixture to mock the GitHub workspace."""
    monkeypatch.setattr(validator, "WORKSPACE_PATH", tmp_path)
    return tmp_path


@pytest.mark.parametrize(
    ("filename", "expected_error"),
    [
        ("audience_empty.yaml", "[] should be non-empty"),
        ("project_empty.yaml", "None is not of type 'object'"),
    ],
)
def test_negative(mock_workspace, capsys, filename, expected_error):
    """Test that invalid project files fail validation."""
    invalid_content = (tests_data_dir / "action" / "project" / "negative" / filename).read_text()
    (mock_workspace / "project.owasp.yaml").write_text(invalid_content)

    with pytest.raises(SystemExit) as exit_info:
        validator.main()  # type: ignore[attr-defined]

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: Validation failed!" in captured.err
    assert expected_error in captured.err


def test_positive(mock_workspace, capsys):
    """Test that a valid project file passes validation."""
    valid_content = (
        tests_data_dir / "action" / "project" / "positive" / "valid_project.yaml"
    ).read_text()
    (mock_workspace / "project.owasp.yaml").write_text(valid_content)

    with pytest.raises(SystemExit) as exit_info:
        validator.main()  # type: ignore[attr-defined]

    assert exit_info.value.code == 0
    captured = capsys.readouterr()
    assert "SUCCESS: Validation passed!" in captured.out
