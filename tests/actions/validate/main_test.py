"""Tests for the GitHub Action's core file-finding logic."""

import pytest
from actions.validate import main as action

from tests.conftest import tests_data_dir


@pytest.fixture
def mock_workspace(tmp_path, monkeypatch):
    """Fixture to mock the GitHub workspace."""
    monkeypatch.setattr(action, "WORKSPACE_PATH", tmp_path)
    return tmp_path


def test_validation_fails_when_no_file_found(capsys):
    """Test that the action fails correctly when no file is found."""
    with pytest.raises(SystemExit) as exit_info:
        action.main()

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: OWASP metadata file not found." in captured.err


def test_validation_fails_when_multiple_files_found(mock_workspace, capsys):
    """Test that the action fails correctly when multiple files are found."""
    (mock_workspace / "project.owasp.yaml").write_text(
        (tests_data_dir / "actions/validate/project/positive/valid_project.yaml").read_text(),
    )
    (mock_workspace / "chapter.owasp.yaml").write_text(
        (tests_data_dir / "actions/validate/chapter/positive/valid_chapter.yaml").read_text(),
    )

    with pytest.raises(SystemExit) as exit_info:
        action.main()

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: Found multiple OWASP metadata files." in captured.err
