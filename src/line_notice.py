import requests
from pathlib import Path


class LineNotice:
  __URL = "https://notify-api.line.me/api/notify"
  def __init__(self, token) -> None:
      self.__headers = {'Authorization': 'Bearer ' + token}

  def __send(self, message, path=None):
    if not message:
        raise ValueError('message must not be None.')
    if not isinstance(message, str):
        raise TypeError(
            f'message must be str. But input message type was: {type(message)}')
    headers = self.__headers
    payload = {'message': message}
    files = {}
    if path:
      if isinstance(path, Path):
          TypeError(
              f'message must be pathlib.Path. But input message type was: {type(path)}')
      if not path.exists():
          raise ValueError(f'image file does not exist: {path}')
      extention = path.suffix
      if not extention:
          raise ValueError(
              'image must not be a directory. But the input was: {path}')
      elif extention not in ['.png', '.jpg']:
          raise ValueError(f'image must have .png or .jpg as its extention. But {extention} file was input.')
      files = {'imageFile': open(str(path), 'rb')}
    r = requests.post(self.__URL, headers=headers, params=payload, files=files)
    if not r.ok:
        raise Exception(
            'The message, image can not be sent for some reason.')
    return r

  def sendMessage(self,message):
    return self.__send(message)

  def sendMessageWithImage(self,message,path):
    return self.__send(message,path)
