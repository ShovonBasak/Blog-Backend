FROM python:3.11.4
WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app/logs
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app.main:app"]
