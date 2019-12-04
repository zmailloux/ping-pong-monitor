FROM python:3.6
LABEL maintainer="zachmailloux@gmail.com"
COPY . /dashboard
WORKDIR /dashboard
RUN pip install -r requirements.txt
EXPOSE 8080
WORKDIR /dashboard/app
ENTRYPOINT ["python"]
CMD ["app.py"]
