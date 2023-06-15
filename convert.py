import os
import base64
from PIL import Image
import numpy as np

im_size =(200,100)

def convert(path):
    for person in os.listdir(path):
        person = os.path.join(f"{path}/{person}")
        # print(person)
        for filename in os.listdir(person):
            if filename.endswith(".txt"):
                filename = os.path.join(f"{person}/{filename}")
                # print(filename)
                with open(filename, 'rb') as file:
                    text = str(file.read())
                    img_data = text[24:-1]
                    file_path=f"{filename}.png"
                    if  not os.path.exists(file_path):
                        with open(file_path, "wb") as fh:
                            img_data=str(img_data).encode("UTF-8")
                            de =base64.decodebytes(bytes(img_data))
                            fh.write(de)
                            
                            

def getPixels(filename):    
    im = Image.open(filename, 'r').convert('L')
    im = im.resize(im_size)
    # pix_val = list(im.getdata())
    pix_val = np.asarray(im)
    return pix_val
    
def gen_pattern(path):
    for person in os.listdir(path):
        pp = os.path.join(f"{path}/{person}")
        # print(person)
        all_px=np.empty([im_size[1],im_size[0]])
        for filename in os.listdir(pp):
            if filename.endswith(".png"):
                filename = os.path.join(f"{path}/{person}/{filename}")
                px = getPixels(filename)
                for i in range(im_size[1]):
                    for j in range(im_size[0]):
                        all_px[i,j]+=px[i,j]

                # print(px)
        PIL_image = Image.fromarray(np.uint8(all_px)).convert('L')
        PIL_image.save(os.path.join(f"{path}/{person}/pattern.bmp"))
        # print(all_px)

def get_pattern(filename):
    save_filename = os.path.join(f"{filename}.bmp")
    img_data = ""
    with open(filename, 'rb') as file:
        img_data = str(file.read())
        img_data = img_data[24:-1]
    with open(save_filename, "wb") as fh:
        img_data=str(img_data).encode("UTF-8")
        de =base64.decodebytes(bytes(img_data))
        fh.write(de)
    px = getPixels(save_filename)
    PIL_image = Image.fromarray(np.uint8(px)).convert('L')
    PIL_image.save(save_filename)
    im = Image.open(save_filename, 'r').convert('L')
    im = im.resize(im_size)
    pix_val = np.asarray(im)
    return pix_val
        
def check_img(path, img_path):
    pt = get_pattern(img_path)
    print(get_pattern(img_path))
    print("Checking img")
    
        
if __name__ == "__main__":
    path = os.path.join("./img")
    convert(path)
    gen_pattern(path)
    get_pattern("x.txt")
    # check_img(path, "x.txt")