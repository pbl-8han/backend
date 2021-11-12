import os
import io
from google.cloud import vision

from google.cloud.vision_v1.types.image_annotator import LocalizedObjectAnnotation
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\yuta1\\Google_Json\\pbl8-330506-05907161ebc4.json"
# json_pathは、サービスアカウントキーのパス

import cv2
import datetime
import time
import schedule

FALE_PASS = 'C:\\Users\\yuta1\\Downloads\\PBL_try\\photo.png'

def people_count(image_pass):

    client= vision.ImageAnnotatorClient()

    #ファイル読み込み
    file_name = os.path.abspath(image_pass)

    with io.open(file_name,'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content = content)

    #APIにリクエスト
    response = client.object_localization(image = image, max_results = 50).localized_object_annotations

    #Personオブジェクトを数える
    count = 0
    for res in response:
        if res.name == "Person":
                count += 1
            
    return count



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

        #画像をVisionApiに送る
        print(people_count(FALE_PASS))

        #時間を取得する
        dt_now = datetime.datetime.now()
        print(dt_now)


      # 一分のインターバルを設定
      time.sleep(60)

# 12:00になったら撮影処理を実行するように時間を指定
schedule.every().day.at("15:01").do(capture)

# 時間になるまでループ
while True:

  # 一分ごとに時間を確認
  schedule.run_pending()
  time.sleep(60)