# coding:utf-8
import requests
r=requests.get("https://www.baidu.com/")

print r.url
print r.encoding
# decompress the gizp deflate
print r.content
print r.headers
print r.cookies
# print the failed request
print r.raise_for_status()
print r.text
# print the json date of the response
#print r.json()
