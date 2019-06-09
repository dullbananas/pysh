PHONY: cov, test, travisbuild

travisbuild:
	coverage run --source shellp -m pytest -v
	coverage xml
	python-codacy-coverage -r coverage.xml

test:
	python3 -m pytest

cov:
	coverage run --source shellp -m pytest
	coverage html
