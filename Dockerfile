FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r ./requirement.txt

CMD [ "python3", "MainApplication.py" ]
