FROM python:3.6
LABEL maintainer="zachmailloux@gmail.com"
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
