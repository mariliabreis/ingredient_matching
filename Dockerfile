FROM python:3.8.6-buster
COPY ingredient_matching /ingredient_matching
COPY requirements.txt /requirements.txt
COPY data /data
COPY main.py /main.py
COPY models /models
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0
