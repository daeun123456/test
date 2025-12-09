FROM python:3-alpine

RUN pip install flask

WORKDIR /app

COPY * /app/

EXPOSE 5555

CMD ["python3","app.py"]