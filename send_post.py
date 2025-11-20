import requests

def send_post():
    # 要请求的 URL
    url = "http://localhost:5678/webhook-test/test-code-review"  # 替换成你的目标地址

    # 要发送的 POST 数据（字典会自动转为表单）
    data = {
        "name": "Tom",
        "age": 18
    }

    # 如果需要发送 JSON，可以用 json= 参数
    # response = requests.post(url, json=data)

    # 这里用 form 表单方式发送
    try:
        response = requests.post(url, data=data, timeout=10)
        print("状态码:", response.status_code)
        print("返回内容:", response.text)
    except requests.RequestException as e:
        print("请求出错:", e)

if __name__ == "__main__":
    send_post()
