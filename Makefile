format_project:
	black .
	flake8 .

check_format:
	black --check .
	flake8 .

clean:
	rm -rf __pycache__



