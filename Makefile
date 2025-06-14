# Makefile for fa2svg release automation

.PHONY: clean build upload release bump_version tag push_tag

clean:
	rm -rf dist

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/* --config-file .pypirc

bump_version:
	@python scripts/bump_version.py

tag:
	@VERSION=$$(python -c 'import fa2svg._version; print(fa2svg._version.__version__)'); \
	git add fa2svg/_version.py; \
	git commit -m "Bump version to $$VERSION"; \
	git tag v$$VERSION

push_tag:
	@VERSION=$$(python -c 'import fa2svg._version; print(fa2svg._version.__version__)'); \
	git push origin v$$VERSION

release:
	@if [ -z "$(VERSION)" ]; then \
	  make bump_version; \
	fi; \
	make clean build tag upload push_tag 