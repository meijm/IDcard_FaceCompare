#基于二代身份证的人脸识别身份验证系统研究
import os
from FaceCompare import FC,RS

#resize image file
#basepath = r'C:\Users\meijm\Desktop\test\data90'
#outbase=r'C:\Users\meijm\Desktop\test\Rtestdata'
#for entry in os.listdir(basepath):
 #   if os.path.isfile(os.path.join(basepath, entry)):
 #       inputpath=basepath+"\\"+entry
 #       outputpath=outbase+"\\"+entry
 #       RS(inputpath,outputpath)

# List all files in a directory using os.listdir
maxconfig=0
maxfile=""
basepath = r'C:\Users\meijm\Desktop\test\Rdata90'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        entry=basepath+"\\"+entry
        confidence=FC(filepath1=r"C:\Users\meijm\Desktop\test\meme.jpg",filepath2=entry)
        #confidence=FC(filepath1=r"C:\Users\meijm\Desktop\test\me2.jpg",filepath2=r"C:\Users\meijm\Desktop\test\Rtestdata\丁加旺2024年江苏.jpg")
        if maxconfig < confidence:
            maxconfig=confidence
            maxfile=entry
print("maxconfidence:",maxconfig,"filename:",maxfile)