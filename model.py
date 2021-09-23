import torch
import cv2
import pandas as pd
import numpy as np
cap=cv2.VideoCapture(0)
img='test_images/table.jpg'
    # Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
def object_detector():
    # success , img =cap.read()
    result=model(img)
    result.show()
    predicts=result.pandas().xyxy[0]  # img1 predictions (pandas)
    predicts['count']=1
    results=predicts[['name','count']]
    data=results.groupby(['name']).sum()
    # data=data.reset_index()
    # time.sleep(10)
    data=data.to_dict()
    data=data['count']
    return data
