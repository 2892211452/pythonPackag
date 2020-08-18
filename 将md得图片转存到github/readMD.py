import  re
import os

os.makedirs('./image/', exist_ok=True)
os.makedirs('./copyMD/', exist_ok=True)

img_dir = './image/'


def request_download(path,IMAGE_URL):
    import requests
    r = requests.get(IMAGE_URL)
    with open(path, 'wb') as f:
        f.write(r.content)


img_dict ={}

with open('test.md', 'r', encoding= 'utf-8', errors='ignore') as  f:
    lines = f.readlines()


mdFile = open('./copyMD/test.md','w',encoding= 'utf-8',)

for i in lines:
    ans = re.findall(r'!.?((.*?))', i)
    if ans !=[]:
        # print(ans)
        tmp = i.split('(')[1]
        tmp = tmp.replace(')', '')
        tmp = tmp.replace('\n', '')
        name = tmp .replace('https://', '')
        name = name .replace('http://', '')
        name = name .replace('/', '')
        name = name .replace('\n', '')
        path = img_dir + name
        img_dict[tmp] = path
        request_download(path,tmp)
        print(tmp , '已经保存到本地')
        i = i.replace(tmp, path)
        print(i)
    mdFile.write(i)



for i in img_dict:
    print(i, img_dict[i])