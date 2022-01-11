FROM python:3.9.7-slim

WORKDIR /home/app

COPY index.html .

EXPOSE 9000

CMD ["python3", "-m", "http.server", "9000"]