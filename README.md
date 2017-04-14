# gdt_search
Multiple Resource Search REST API using Python 

Steps to run the server:
	1. pip install -r requirments.txt
	2. gunicorn --log-file - api:app


To check: curl “127.0.0.1:5000?q=the+dark+knight”