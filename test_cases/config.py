import pytest
#基础域名
base_url="https://jsonplaceholder.typicode.com/posts"
#参数化测试数据
post_test_data=[
    (1,200),
    (9999,404),
    ("abc",404)
]
