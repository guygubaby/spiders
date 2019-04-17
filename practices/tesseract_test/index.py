from PIL import Image
from pytesseract import image_to_string
import requests
import datetime


class TesseractTest:
    base_url='http://47.107.92.76:8080/api/auth.do'
    login_url='login'
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    data={
        'username':'',
        'digest':'',
        'code':''
    }
    session=requests.session()
    session.headers=headers

    def __init__(self):
        pass

    def get_verifycode_img(self):
        img_res=self.session.get(self.base_url,params={
            'action':'loadCode',
            'date':datetime.datetime.now()
        })
        self.img_path=f'./imgs_code/{datetime.datetime.now()}.png'
        with open(self.img_path,'wb') as f:
            f.write(img_res.content)

    def get_code(self):
        img=Image.open(self.img_path)

        imgry = img.convert("L")
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        # out.show()

        code=image_to_string(out)
        print(f'code : {code}')
        return code


if __name__ == '__main__':
    # img=Image.open('./vm3.png')
    # code=image_to_string(img)
    # print(code)

    tesseract_test=TesseractTest()
    tesseract_test.get_verifycode_img()
    tesseract_test.get_code()
