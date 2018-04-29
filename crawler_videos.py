import requests
import re

main_url = 'http://video.eastday.com/a/170602114054589846059.html?indexlbt'

resp = requests.get(main_url)
"""没有下面这行，打印的结果中文是乱码"""
resp.encoding='utf-8'

html = resp.text

link = re.findall(r'var mp4 = "(.*?)";', html)[0]

link = 'http:'+link

dest_resp = requests.get(link)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#保存数据的路径及文件名
path = '/media/zzy/DAA07DDCA07DC015/video/刘涛.mp4'
f = open(path, 'wb')
f.write(data)
f.close()
print('下载完成')