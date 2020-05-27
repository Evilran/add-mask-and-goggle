# 给头像添加口罩及护目镜

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/flask-v1.1.1-blue)](https://pypi.org/project/Flask/) [![License](https://img.shields.io/github/license/Evilran/add-mask-and-goggle)](https://github.com/Evilran/add-mask-and-goggle/blob/master/LICENSE)

珍爱生命，为预防2020新型冠狀病毒肺炎，请积极佩戴口罩及护目镜。

此项目使用人脸识别自动给头像添加口罩及护目镜，仅为呼吁大家积极佩戴口罩及护目镜，为武汉及奋斗在第一线的医护人员加油！

依赖🐍
------------------------------------------------------------------

- numpy==1.17.4
- Flask>=1.0.0
- requests==2.22.0
- opencv-python==4.0.0.21
- dlib==19.17.99

用法😷
---

仅需一个命令即可简单地运行Web服务器：

```
$ python3 server.py
```

然后访问: **127.0.0.1:5000** (端口 5000).

这里支持两种模式，一种是输入URL地址，另外一种是直接上传图片：

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/images/url.png)

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/images/upload.png)



目前口罩支持以下几种类型：

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/images/mask.png)

## 举个栗子🌰

***原图：***

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/test/grace_hopper.bmp)

***添加口罩及护目镜：***

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/images/grace_hopper.bmp)

***原图：***

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/test/i064qa-mn.jpg)

***添加口罩：***

![image](https://github.com/Evilran/add-mask-and-goggle/blob/master/images/i064qa-mn.jpg)

## 感谢🙏

感谢奋斗在第一线的医护人员，感谢春运中的逆行者！

口罩及护目镜素材来自：[[maskon-wuhan](https://github.com/izumiwing/maskon-wuhan)]@[izumiwing](https://github.com/izumiwing)
