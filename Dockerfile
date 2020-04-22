FROM scrapinghub/scrapinghub-stack-scrapy:2.0-20200325
ENV TERM xterm
ENV SCRAPY_SETTINGS_MODULE scrapy_pyppeteer_cloud_example.settings
RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# pyppeteer stuff
RUN pyppeteer-install
RUN apt-get update && apt-get install -y libx11-xcb-dev libxcomposite1 \
                                         libxdamage1 libxi6 libxtst6 libnss3 \
                                         libxss1 libxrandr2 libasound2 \
                                         libatk1.0-0 libgtk-3-0

RUN python setup.py install
