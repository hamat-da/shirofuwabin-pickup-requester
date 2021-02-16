# shirofuwabin-pickup-requester

しろふわ便の注文をseleniumで自動化するプログラムです。
注文完了通知を[LINE Notify](https://notify-bot.line.me/ja/)で通知できます。

# Requirement

* [python](https://www.python.org/) 3.8

# 環境変数
|Name|Description|Default|
|:--|:--|:--|
|EMAIL|ログイン時のメールアドレス|-|
|PASS|ログイン時のパスワード|-|
|MEMO|備考||
|MAX_COUNT|注文最大数（月）|4|
|ENABLE_LINE_NOTICE|注文完了時LINEで通知するか|false|
|TOKEN_LINE_NOTICE|[LINE Notify](https://notify-bot.line.me/ja/)トークン|-|
|LOG_FILEPATH|ログファイルパス||

# License

"shirofuwabin-pickup-requester" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).