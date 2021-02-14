import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
import settings
import logging
import line_notice
from pathlib import Path
from datetime import datetime as dt

tdatetime = dt.now()
tstr = tdatetime.strftime('%Y%m%d')

LOG_FORMAT = settings.LOG_FORMAT
EMAIL = settings.EMAIL
PASS = settings.PASS
MEMO = settings.MEMO
MAX_COUNT = settings.MAX_COUNT
LOGLEVEL = settings.LOGLEVEL
ENABLE_LINE_NOTICE = settings.ENABLE_LINE_NOTICE
TOKEN_LINE_NOTICE = settings.TOKEN_LINE_NOTICE
LOG_FILEPATH=settings.LOG_FILEPATH
FILENAME = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../image/"+tstr+".png")


def main():
  logging.basicConfig(level=LOGLEVEL, format=LOG_FORMAT, filename=LOG_FILEPATH)
  options = set_option()
  out_log('EMAIL', EMAIL)
  driver = webdriver.Chrome(options=options)
  login(driver)
  pickup_request(driver)

def set_option():
  options = Options()
  options.add_argument('--headless')
  options.add_argument('--incognito')
  options.add_argument('--hide-scrollbars')
  options.add_argument('--disable-dev-shm-usage')
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox')

  return options

def out_log(key,value):
  logging.info('%s:%s', key, value)

def login(driver):
  driver.get('https://www.shirofuwabin.jp/login/input')
  time.sleep(3)
  email_box = driver.find_element_by_name("email")
  email_box.send_keys(EMAIL)
  pass_box = driver.find_element_by_name("password")
  pass_box.send_keys(PASS)
  time.sleep(1)
  pass_box.submit()
  time.sleep(3)

def pickup_request(driver):
  MONTH_COUNT_XPATH = "/html/body/div[4]/form/div[1]/p[3]/span"
  driver.get('https://www.shirofuwabin.jp/order')
  time.sleep(5)
  monthCount = driver.find_element_by_xpath(MONTH_COUNT_XPATH)
  out_log('monthcount', monthCount.text)
  if(int(monthCount.text) > MAX_COUNT):
    out_log('over count MAX','MAX_COUNT')
    driver.quit()
  else:
    delivery_on = driver.find_element_by_name(
        "delivery_on").get_attribute("value")
    receive_on = driver.find_element_by_name(
        "receive_on").get_attribute("value")
    out_log('delivery_on', delivery_on)
    out_log('receive_on', receive_on)

    memo_box = driver.find_element_by_name("memo")
    memo_box.send_keys(MEMO)
    submit_btn = driver.find_element_by_name("_check")
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    driver.set_window_size(w, h)
    driver.save_screenshot(FILENAME)
    if ENABLE_LINE_NOTICE:
      notice = line_notice.LineNotice(token=TOKEN_LINE_NOTICE)
      notice.sendMessageWithImage('集荷依頼中', Path(FILENAME))
    time.sleep(5)
    submit_btn.click()
    time.sleep(5)
    if ENABLE_LINE_NOTICE:
      notice = line_notice.LineNotice(token=TOKEN_LINE_NOTICE)
      notice.sendMessage('集荷依頼完了')
    driver.quit()


main()
