import cv2
import datetime
import time
import schedule

# 画像を撮影する処理
def capture():

  # 曜日を取得して土日以外に限定する
  week_num = datetime.date.today().weekday()
  if week_num < 6:

    # ループ処理で90回(1時間半の間)実行
    for i in range(0, 90, 1):

      # 撮影した画像のファイル名をphoto.pngに決定
      fileName = "photo.png"

      # カメラに接続し撮影
      capture = cv2.VideoCapture(0)

      # 取得した画像データは変数imageに格納
      ret, image = capture.read()

      if ret == True:

        # 取得した画像を出力
        cv2.imwrite(fileName, image)
        print("taking picture is completed!!")

      # 一分のインターバルを設定
      time.sleep(60)

# 12:00になったら撮影処理を実行するように時間を指定
schedule.every().day.at("12:00").do(capture)

# 時間になるまでループ
while True:

  # 一分ごとに時間を確認
  schedule.run_pending()
  time.sleep(60)