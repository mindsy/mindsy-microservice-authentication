FROM mindsy/flask:latest

COPY app.py ./
WORKDIR ./

CMD python app.py

EXPOSE 5000
