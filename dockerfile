# FROM docker.io/python:3-slim
FROM python:latest

# # Install dependencies.
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy code.
ADD main.py /main.py
ADD social.py /social.py
ADD tools.py /tools.py

CMD ["python", "/main.py"]