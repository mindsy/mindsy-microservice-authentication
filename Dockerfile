FROM python:3.6
COPY ./ ./src
WORKDIR ./src
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
CMD python app.py
EXPOSE 5000