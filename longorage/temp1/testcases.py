import requests



data = {
    "id": 1,
    "name": "upload image",
    "cyclename":"BVT-1011",
    "executionresult":"pass",
    "attachment":"just do it",
    "description":"yes,just do it when it's right",
    "steps":"1.click button;2.select image;3.upload image"
}
url = "http://127.0.0.1:5007/testcase_orm"
r = requests.post(url=url,json=data)
print(r.text)