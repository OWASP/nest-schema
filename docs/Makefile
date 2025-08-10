clean-docs-docker:
	@docker container rm -f owasp-schema-docs >/dev/null 2>&1 || true
	@docker image rm -f docker-docs >/dev/null 2>&1 || true
	@docker volume rm -f docker_docs-venv >/dev/null 2>&1 || true

docs:
	@docker build \
		-f docs/docker/Dockerfile.local \
		-t owasp-schema-docs \
		. && \
	docker run --name owasp-schema-docs \
		-p 8002:8002 \
		-v .:/home/owasp \
		-v docs-venv:/home/owasp/.venv \
		--rm \
		owasp-schema-docs \
		sh -c "python docs/scripts/generate_schema_docs.py && mkdocs serve -a 0.0.0.0:8002"

update-docs-dependencies:
	cd docs && poetry update
