FROM python:3.6.5-slim
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]