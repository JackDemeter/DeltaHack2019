from PIL import Image
import cv2
import main1
import os
import tensorflow as tf

#from db import session, Credentials, Users

#print(vars(session.query(Credentials).first()))

# data = open('QRtext.txt').split(' ').strip()
data = [1,0]
data[0] = 1
dict1={}
if (data[0] == 1):
    dict1 ={
        'DATE':[50,150,150,170],
        'AGE':[470,140,510,170],
        'PATIENT NAME':[230,145,420,165],
        'DOB':[595,135,690,170],
        'Issue1':[30,235,230,270],
        'Issue2':[340,235,570,265],
        'LAST EXAM':[165,305,280,335],
        'LAST EYE':[365,305,475,335],
        'DENTAL':[575,315,690,335],
        'COLY':[245,360,255,370],
        'COLN':[290,360,300,370],
        'FINDINGS':[425,355,610,370]
    }
elif (data[0] == 2):
    dict1 = {
        'FIRST':[30,100,60,110],
        'REPEAT':[240,100,250,110],
        'WHOLEBLOOD':[40,160,50,110],
        'APHERESIS':[140,160,150,170]
    }

i = 0
img = Image.open("3doc.png")
list = []
for key in dict1:
    print(i)
    data = dict1.get(key)
    crop = img.crop((int(data[0]),int(data[1]),int(data[2]),int(data[3])))
    crop.save("C:/Users/JackD/Desktop/DeltaHacks/DeltaHack2019/SimpleHTR/data/temp"+str(i)+".png")
    main1.act("C:/Users/JackD/Desktop/DeltaHacks/DeltaHack2019/SimpleHTR/data/temp"+str(i)+".png")
    i += 1
    tf.reset_default_graph()