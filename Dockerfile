FROM python:3.9.7-bullseye

EXPOSE 5000

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install .

ENV FLASK_APP 'run.py'

CMD [ "flask", "run", "-h", "0.0.0.0"]