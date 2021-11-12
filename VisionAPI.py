import os
import io
from google.cloud import vision

from google.cloud.vision_v1.types.image_annotator import LocalizedObjectAnnotation
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\yuta1\\Google_Json\\pbl8-330506-05907161ebc4.json"
# json_pathは、サービスアカウントキーのパス


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

print(people_count('C:\\Users\\yuta1\\Downloads\\PBL_try\\11.jpg'))