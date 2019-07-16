FROM python:3.7-alpine

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "range.py"]
CMD ["run"]