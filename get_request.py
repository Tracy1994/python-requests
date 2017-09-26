#coding:utf-8
import requests

par  = {"Keywords":"yoyoketang"}
r=requests.get("http://zzk.cnblogs.com/s/blogpost", params=par)

print r.status_code
print r.text