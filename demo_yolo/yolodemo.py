import  cv2
import numpy as np


cap=cv2.VideoCapture(0)
whT=320

classesFile='coco.names'
classNames=[]
with open (classesFile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')
# print(classNames)

modeL_config='yolov3.cfg'
model_weights='yolov3.weights'
net=cv2.dnn.readNetFromDarknet(modeL_config,model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_GPU)




while True:
    success , img =cap.read()
    cv2.imshow('Image',img)
    blob=cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)
    layer_names=net.getLayerNames()
    output_names=[layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    outputs=net.forward(output_names)

    print(len(outputs))
 
    





    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()
