FROM python:3
WORKDIR /tmp
COPY . .
ENTRYPOINT ["python3"]
RUN pip install boto3
CMD ["price_diff.py"]