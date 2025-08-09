"""Tests for the GitHub Action's core file-finding logic."""

import pytest
import validate as validator

from tests.conftest import tests_data_dir


@pytest.fixture
def mock_workspace(tmp_path, monkeypatch):
    """Fixture to mock the GitHub workspace."""
    monkeypatch.setattr(validator, "WORKSPACE_PATH", tmp_path)
    return tmp_path


def test_validation_fails_when_no_file_found(capsys):
    """Test that the action fails correctly when no file is found."""
    with pytest.raises(SystemExit) as exit_info:
        validator.main()  # type: ignore[attr-defined]

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: OWASP metadata file not found." in captured.err


def test_validation_fails_when_multiple_files_found(mock_workspace, capsys):
    """Test that the action fails correctly when multiple files are found."""
    project_content = (
        tests_data_dir / "action" / "project" / "positive" / "valid_project.yaml"
    ).read_text()
    chapter_content = (
        tests_data_dir / "action" / "chapter" / "positive" / "valid_chapter.yaml"
    ).read_text()

    (mock_workspace / "project.owasp.yaml").write_text(project_content)
    (mock_workspace / "chapter.owasp.yaml").write_text(chapter_content)

    with pytest.raises(SystemExit) as exit_info:
        validator.main()  # type: ignore[attr-defined]

    assert exit_info.value.code == 1
    captured = capsys.readouterr()
    assert "ERROR: Found multiple OWASP metadata files." in captured.err
