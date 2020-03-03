import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        newnama = namafile.split('.')
        # print(newnama[0])
        # lennama = len(newnama)
        # print(newnama[:(lennama-1)])
        ekstensi = tipe[content_type]
        logging.warning(f"writing {newnama[0]}.{ekstensi}")
        fp = open(f"{newnama[0]}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    arr=[]
    arr.append('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
    arr.append('https://upload.wikimedia.org/wikipedia/id/c/c4/Badge_ITS.png')
    arr.append('https://gatra.website/foldershared/images/2019/fuad/06-Jun/ITS.jpg')

    threads = []
    for i in arr:
        # print(i)
        t = threading.Thread(target=download_gambar, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()