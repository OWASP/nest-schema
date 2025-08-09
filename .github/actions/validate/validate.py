"""Validate schema files against OWASP JSON schema."""

import sys
from pathlib import Path

import yaml

from owasp_schema import get_schema
from owasp_schema.utils.schema_validators import validate_data

WORKSPACE_PATH = Path("/github/workspace")


def main():
    """Automatically finds and validates an OWASP metadata file."""
    sys.stdout.write("INFO: Checking for OWASP metadata file.\n")

    metadata_files = list(WORKSPACE_PATH.glob("*.owasp.yaml"))

    if not metadata_files:
        sys.stderr.write("ERROR: OWASP metadata file not found.\n")
        sys.exit(1)

    if len(metadata_files) > 1:
        sys.stderr.write("ERROR: Found multiple OWASP metadata files.\n")
        sys.exit(1)

    file_path = metadata_files[0]
    file_name = file_path.name
    schema_name = file_name.split(".")[0]

    sys.stdout.write(
        f"INFO: Found '{file_name}'. Validating against the '{schema_name}' schema.\n",
    )

    try:
        with file_path.open("r") as f:
            data = yaml.safe_load(f)
    except PermissionError:
        sys.stderr.write("ERROR: Could not access OWASP metadata file.\n")
        sys.exit(1)

    if error_message := validate_data(schema=get_schema(schema_name), data=data):
        sys.stderr.write(f"ERROR: Validation failed! {error_message}\n")
        sys.exit(1)

    sys.stdout.write("SUCCESS: Validation passed!\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
