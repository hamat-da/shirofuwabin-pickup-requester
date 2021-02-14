FROM python:3.8-alpine
WORKDIR /tmp
RUN apk add --no-cache \
  fontconfig \
  chromium \
  chromium-chromedriver && \
  wget --no-cache -nv http://moji.or.jp/wp-content/ipafont/IPAfont/ipag00303.zip && \
  mkdir -p /usr/share/fonts/ipa && \
  unzip ipag00303.zip -x *.txt -d /usr/share/fonts/ipa && \
  fc-cache -f && \
  apk del --no-cache --purge fontconfig && \
  rm -rf /tmp/* && \
  addgroup executor && \
  adduser -D -G executor executor && \
  mkdir -p /home/executor/app && \
  pip3 install --no-cache-dir pipenv
WORKDIR /home/executor
COPY --chown=executor:executor Pipfile* /home/executor/
RUN pipenv install --system --deploy --clear
COPY --chown=executor:executor . /home/executor/app
USER executor
CMD ["python3", "app/src/main.py"]