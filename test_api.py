import json
import requests
import base64
import time, cv2, os
import numpy as np
if __name__ == '__main__':
    read_CT_auto_url = 'http://10.0.9.28:2080/read_CT'  # read_CT_cuto_url
    read_CT_manual_url = 'http://10.0.9.28:2080/read_CT_manual'  # read_CT_manual_url
    read_logo_url = 'http://10.0.9.28:2080/read_logo'
    # 不需要裁剪
    dir_path = './images/autoTC_erro_2/autoTC_erro_2/'
    for image_name in os.listdir(dir_path):
        image_path = os.path.join(dir_path, image_name)
        with open(image_path, 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        data_obj = {'img_base64': image_base64, "mode":"A", "type":"LH"}

        # test
        t0 = time.time()
        r = requests.post(read_CT_auto_url, json.dumps(data_obj))
        t1 = time.time()
        print('time',t1-t0)
        print(r)
        content = r.json()
        print(len(content['data']))
        img_b64decode = base64.b64decode(image_base64)  # base64解码
        img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        height, width, _ = image.shape
        cpos = content["data"][0]["cpos"]
        tpos = content["data"][0]["tpos"]
        cv2.line(image, (int(cpos), 0), (int(cpos), height - 1), (255, 0, 0), 2)
        cv2.line(image, (int(tpos), 0), (int(tpos), height - 1), (0, 0, 255), 2)
        cv2.imwrite("test_draw.jpg", image)
        cv2.imwrite("result1114/"+image_name, image)
        
