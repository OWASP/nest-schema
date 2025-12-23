include docs/Makefile

.PHONY: docs

build-package:
	@cp *.json src/owasp_schema/ 2>/dev/null
	poetry build

bump-major:
	poetry run bump2version major --allow-dirty

bump-minor:
	poetry run bump2version minor --allow-dirty

bump-patch:
	poetry run bump2version patch --allow-dirty

check: \
    pre-commit

check-test: \
	check \
	test

clean-package:
	rm -rf dist/ build/ *.egg-info/

clean-dependencies:
	@rm -rf .venv

install:
	poetry install

pre-commit:
	@pre-commit run -a

publish-package:
	poetry publish

test:
	@DOCKER_BUILDKIT=1 docker build \
		--cache-from test-owasp-schema \
		-f docker/Dockerfile.test . \
		-t test-owasp-schema
	@docker run --rm test-owasp-schema pytest


update-dependencies:
	poetry update
