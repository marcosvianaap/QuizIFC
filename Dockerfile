FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade setuptools

RUN pip3 install -r requirements.txt

CMD ["gunicorn","app:app","-b","0.0.0.0","-w","4"]

#CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]