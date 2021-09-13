import torch
import cv2
import pandas as pd
import numpy as np
cap=cv2.VideoCapture(0)
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
success , img =cap.read()
result=model(img)
# result.show()
#   # img1 predictions (tensor)
predicts=result.pandas().xyxy[0]  # img1 predictions (pandas)
predicts['count']=1
results=predicts[['name','count']]
data=results.groupby(['name']).sum()

