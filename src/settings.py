import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get("EMAIL",'')
PASS = os.environ.get("PASS",'')
MEMO = os.environ.get("MEMO",'')
MAX_COUNT = int(os.environ.get("MAX_COUNT",4))
ENABLE_LINE_NOTICE = bool(os.environ.get("ENABLE_LINE_NOTICE", ''))
TOKEN_LINE_NOTICE = os.environ.get("TOKEN_LINE_NOTICE", '')
LOG_FORMAT = os.environ.get(
    "LOG_FORMAT", '%(levelname)s : %(asctime)s : %(message)s')
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
LOG_FILEPATH = os.environ.get('LOG_FILEPATH', '')
