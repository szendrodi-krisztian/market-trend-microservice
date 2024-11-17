FROM python:3.13-slim
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
COPY --from=orm . /app/orm
WORKDIR /app
EXPOSE 5050
CMD [ "python", "-u", "main.py" ]