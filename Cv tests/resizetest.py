import cv2
import numpy
import json

configSource = open('config.json')


'''jsonData = json.loads(configSource.read()).decode("utf-8")
p = jsonData["testdata"]
print (p)

'''

#print(configSource.read())

json_info = json.loads(configSource.read())

faceCascade = json_info["Face Cascade"]
print(type(faceCascade))
x1,y1,x2,y2 = json_info["Region Of Interest"]["x1"],json_info["Region Of Interest"]["y1"],json_info["Region Of Interest"]["x2"],json_info["Region Of Interest"]["y2"]
print(f"{x1}  {y1}  {x2}  {y2}")

drawROi = json_info["Draw ROI"]["State"]
print(drawROi)
b,g,r = json_info["Draw ROI"]["Color"][0],json_info["Draw ROI"]["Color"][1],json_info["Draw ROI"]["Color"][2]
print(f"{b} {g} {r}")

faceAreaTreshold =  json_info["Face Area Threshold"]
print(faceAreaTreshold)



'''image = cv2.imread('dog.jpg')

r = 100.0 / image.shape[1]
dim = (200, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.imwrite(outputFileName, resized)
cv2.waitKey(0)'''