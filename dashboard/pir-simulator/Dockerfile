FROM python:3.6
LABEL maintainer="zachmailloux@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["pir_simulator.py"]
