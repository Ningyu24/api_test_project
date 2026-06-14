import pytest
import requests
@pytest.fixture
def base_url():
    url = "https://jsonplaceholder.typicode.com/posts"
    return url
def test_get_posts(base_url):
    response=requests.get(base_url)
    assert response.status_code==200
    #断言返回数据是列表且至少有一条
    data=response.json()
    assert isinstance(data,list)
    assert len(data)>0
    #打印前两条记录
    print("前两条帖子",data[:2])

def test_create_posts(base_url):
    json_data={
        "userID":11,
        "title":"A wonderful day",
        "body":"The learning has begun"
    }
    response=requests.post(base_url,json=json_data)
    assert response.status_code==201
    #断言返回的数据包含发送的内容
    response_data=response.json()
    assert response_data["title"]==json_data["title"]
    assert response_data["userID"]==json_data["userID"]
    assert response_data["body"]==json_data["body"]
    #断言服务器返回了一个“id”
    assert "id" in response_data
    #由于jsonplaceholder不会让我通过GET查到这条数据（因为是mock API）
    #可以再调用一次GET/posts/返回的id来验证
    new_id=response_data["id"]
    get_response=requests.get(f"{base_url}/{new_id}")
    #因为jsonplaceholder不会真正保留数据，所以预期返回404
    assert get_response.status_code==404



