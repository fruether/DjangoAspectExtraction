pp = PYTHONPATH="$$PYTHONPATH:$$(dirname $$(pwd))"

.PHONY: test
test:
	${pp} prove --ext=.t.py -e 'python -W ignore'

reset: