# crawler_videos
A crawler for videos

## 一、运行环境
Python3.5+requests

## 二、用途
爬取网页视频

## 三、参考文献
[如何抓取视频资源-以头条视频为例](https://zhuanlan.zhihu.com/p/27234910) 作者：邓旭东HIT

## 四、相关评价
这个抓取过程很简单，局限性也很大，若目标网页源码中没有mp4、rmvb、mov等视频格式，则无法抓取视频。

不过思路还可以：

1. 分析网页源码，查找解析出视频资源url
2. 对该url发起请求，返回二进制数据
3. 将二进制数据保存为视频格式

有时间可以完善一下
