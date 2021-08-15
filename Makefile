# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY: install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest

# Defines the default target that `make` will to try to make, 
# or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "\n\n---------------HELP-----------------\n"
	@echo "Available targets:"
	@echo "test       Run the test suite (default)"
	@echo "\n------------------------------------\n\n"

## Clean up runtime artifacts (needed after a version update)
# .PHONY: clean
# clean:
# 	find . -type f -name "*.py[co]" -delete
# 	find . -type d -name "__pycache__" -delete
# 	rm -f node_modules/.uptodate .pydeps
# 	rm -rf build