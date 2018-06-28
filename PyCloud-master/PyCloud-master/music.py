#coding=utf-8
import os
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import json
import base64
import threading
# from Crypto import *
from Crypto.Cipher import AES

headers = {
    'Cookie': 'appver=2.0.2;',
    'Referer': 'http://music.163.com/',
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}

second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"



def get_params(p):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(p, first_key, iv)
    h_encText = AES_encrypt(h_encText.decode(), second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey
    

def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    postdata = parse.urlencode(data).encode('utf8')
    req = request.Request(url, headers=headers, data=postdata)
    try:
        rep = request.urlopen(req).read().decode('utf8')
    except:
        print("get_json error")
        return None
    json_dict=json.loads(rep)   #获取json
    return json_dict


def getcomment(id):
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+str(id)+"?csrf_token="
    pa = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
    params = get_params(pa)
    sec = get_encSecKey()
    js = get_json(url, params, sec)
    if js==None:
        return ""
    js = js["hotComments"]
    res = ""
    for i in js:
        res += i["content"]+"\n"
    return res

def getsinger(name):
    url = "http://music.163.com/api/search/get/"
    data = {
         "type": 100,
         "s": name
    }
    postdata = parse.urlencode(data).encode('utf8')
    req = request.Request(url, headers=headers, data=postdata)
    try:
        rep = request.urlopen(req).read().decode('utf8')
        singer=json.loads(rep)["result"]["artists"][0]   #获取json

    except:
        print("no such singer name "+name)
        return None, None
    id = singer["id"]
    img = singer['img1v1Url']
    return id, img

def getalbumn(id):
    url = "http://music.163.com/api/artist/albums/"+str(id)+"/"
    data = {
         "limit":200,
    }
    postdata = parse.urlencode(data).encode('utf8')
    req = request.Request(url, headers=headers, data=postdata)
    try:
        rep = request.urlopen(req).read().decode('utf8')
    except:
        print("get_albumn error")
        return None
    list = []
    albums = json.loads(rep)['hotAlbums']
    for alb in albums:
        list.append(alb['id'])
    return list


def songsong(id, songs, lock):
    url = "http://music.163.com/api/album/"+str(id)
    req = request.Request(url, headers=headers)
    try:
        rep = request.urlopen(req).read().decode('utf8')
    except:
        print("get_song error")
        return
    lock.acquire()
    for song in json.loads(rep)['album']['songs']:
        songs[song["name"]] = song["id"]
    lock.release()

def getsong(l):
    songs = {}
    threads = []
    lock = threading.Lock()
    for id in l:
        t = threading.Thread(target=songsong, args=((id, songs, lock)))
        t.daemon = True
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join(60)
    return songs

def showcomment(song_id, f, lock):
    s = getcomment(song_id)
    lock.acquire()
    f.write(s)
    lock.release()    


def singer_craw(name,usr='local'):
    f = None

    singerid,imgurl = getsinger(name)
    if singerid == None:
        return -1
    request.urlretrieve(imgurl, 'data/'+usr+'/img.jpg')
    albList = getalbumn(singerid)
    if albList == None:
        return -1
    songs = getsong(albList)
    threads = []
    f = open('data/'+usr+'/comment.txt','a+',encoding='utf-8')
    f.seek(0)
    f.truncate()
    print('delete '+'data/'+usr+'/comment.txt')
    lock = threading.Lock()
    for song_name, song_id in songs.items():
        print(song_name)
        t = threading.Thread(target=showcomment, args=((song_id,f,lock)))
        t.daemon = True
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join(60)
    
    print("finish "+name)
    f.close()
    return 0



if __name__ == '__main__':
    name = input("artist: ")
    singer_craw(name)


