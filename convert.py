import os
import base64

def convert(path):
    for person in os.listdir(path):
        person = os.path.join(f"{path}/{person}")
        # print(person)
        for filename in os.listdir(person):
            filename = os.path.join(f"{person}/{filename}")
            # print(filename)
            with open(filename, encoding="utf8") as file:
                text = str(file.readlines())
                img_data = text[24:-1]
                with open(f"{filename}.png", "wb") as fh:
                    print(img_data)
                    fh.write(base64.b64decode(img_data))
        
        
if __name__ == "__main__":
    path = os.path.join("./img")

    convert(path)