pp = PYTHONPATH="$$PYTHONPATH:$$(dirname $$(pwd))"

.PHONY: test
test:
	python test.py test
.PHONY: reset
reset:
	python test.py reset
	find . -name "*.log" -exec rm {} \;
	find output/ -name "*.html" -exec rm {} \;
.PHONY: clean
clean:
	make reset
.PHONY: install
install:
	pip install prove
	pip install sqlite
	pip install GitPython
	pip install Jinja2


profile:
	python -m cProfile devprof.py




.PHONY: verify
verify:
