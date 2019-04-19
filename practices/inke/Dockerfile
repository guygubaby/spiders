FROM python:3.6-alpine
COPY . /src
WORKDIR /src
RUN ls -l chrome_driver && pwd \
    && pip install -i https://pypi.douban.com/simple/ --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python","inke.py"]