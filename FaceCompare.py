import requests
import json
import os
from PIL import Image, ImageDraw, ImageFont

def FC(filepath1=r"C:\Users\meijm\Desktop\test\me2.jpg",filepath2=r"C:\Users\meijm\Desktop\test\me4.jpg"):
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"
    #你要调用API的URL

    key ="0DbxAC-3c80xCY85poqMGKDlO1knX7GX"
    secret ="-lAs5xKS-BO__ikvbTv9VD30g7mpMYjD"
    #face++提供的一对密钥

    data = {"api_key":key, "api_secret": secret}
    #必需的参数，注意均为字符串，与官网要求一致
    f1 = open(filepath1, 'rb')
    picture1=f1.read()
    f1.close()
    f2 = open(filepath2, 'rb')
    picture2=f2.read()
    f2.close()
    files = {"image_file1": picture1 , "image_file2": picture2}
    '''以二进制读入图像，这个字典中open(filepath1, "rb")返回的是二进制的图像文件，所以"image_file"是二进制文件，符合官网要求'''

    response = requests.post(http_url, data=data, files=files)
    #POTS上传
    vaule=json.loads(response.content)
    print(response.status_code)
    if response.status_code != 200:
        print("file:",filepath2,"error_message",vaule["error_message"])
        return 0
    print("file:",filepath2,"confidence:",vaule["confidence"])
    return vaule["confidence"]
#输出
# type(response.status_code)
# os.path.getsize (filepath2)
# im.size
#im.show()
# im = Image.open(filepath2)
def RS(inputpath,outputpath):
    im = Image.open(inputpath)
    im.save(outputpath)
    file_size=os.path.getsize (outputpath)
    if file_size>102400:
        im = Image.open(outputpath)
        im.save(outputpath,optimize=True,quality=50)
        file_size=os.path.getsize (outputpath)
    print("file_path",outputpath,"size:",file_size)
    return