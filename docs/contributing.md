# Contributing to OWASP Schema

Thank you for your interest in contributing to the OWASP Schema project - we appreciate your support!

## Getting Started

1. Fork the repository
1. Clone your fork: `git clone https://github.com/your-username/nest-schema.git`
1. Install dependencies: `make install`
1. Run tests to ensure everything works: `make test`

## OWASP Schema Development

The OWASP Schema files are located in the root directory. This is a standalone `pyproject.toml` project with its own test suite.

Please follow these contribution guidelines for OWASP Schema-related changes:

- Order all schema attributes alphabetically where applicable.
- Use the `common.json` definition file for shared object definitions (e.g., chapter, project).
- Include all schema attributes in both required and optional positive test cases.
- Add negative tests for all mandatory attributes, covering empty, invalid, null, and undefined cases.
- Always set `additionalProperties` to `false` and list all mandatory fields in the `required` section.
- Always add `minItems`, `minLength`, and `uniqueItems` where applicable.
- When referencing definitions from `common.json`, test both the object's internal structure (in the `common` section) and its references in actual schemas (e.g., chapter, project).
- Run `make test` before submitting a PR.

## Testing and Building

You can run the following commands locally.

This command runs code quality checks:

```bash
make check
```

This command runs all tests for the schema validation:

```bash
make test
```

This command installs all required dependencies:

```bash
make install
```

This command builds the package for distribution:

```bash
make build
```

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-change`
1. Make your schema changes
1. Add or update tests for your changes
1. Run tests: `make test`
1. Commit your changes with a descriptive message
1. Push and create a pull request
