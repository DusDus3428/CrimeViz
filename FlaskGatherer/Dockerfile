FROM python:3.12.0-bookworm
WORKDIR /app
COPY . .
RUN mkdir -p /instance
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "--app=app.py", "run", "--host=0.0.0.0"]