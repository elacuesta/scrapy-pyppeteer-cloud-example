FROM scrapinghub/scrapinghub-stack-scrapy:2.0-20200325
RUN apt-get update -qq && \
    apt-get install -qy \
        libappindicator1 \
        libasound2 \
        libatk1.0-0 \
        libc6 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libfontconfig1 \
        libgbm-dev \
        libgcc1 \
        libgconf-2-4 \
        libgdk-pixbuf2.0-0 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libstdc++6 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxrandr2 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        xdg-utils \
        unzip && \
    rm -rf /var/lib/apt/lists

ENV CHROMIUM_PATH https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64
ENV CHROMIUM_REVISION 754300
RUN wget ${CHROMIUM_PATH}/${CHROMIUM_REVISION}/chrome-linux.zip -P /chrome && \
    unzip /chrome/chrome-linux.zip -d /chrome && \
    rm /chrome/chrome-linux.zip && \
    chmod -R 777 /chrome
ENV CHROMIUM_LOCAL_PATH /chrome/chrome-linux/chrome

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV SCRAPY_SETTINGS_MODULE scrapy_pyppeteer_cloud_example.settings
COPY . /app
RUN python setup.py install
