# Python-Modular
# 
# 存放一些常用的代码模块和常用工具：
  ## Transformation
    繁体转为简体，收集了8000多个繁简字符对存放在transformation文件夹下的data.json文件中可自行添加
    fantiTojianti.py  读取出data.json里面的字典数据，进行匹配，输入字符或者语句输出转化后的内容，其中的正则是自己需要添加的
  
  ## DownloadBaiduPictures.py  
    指定关键词下载百度图库相关关键词的图片，可指定下载页数
    getManyPages('qq头像', 50)  传入关键词和下载页数采集图片连接
    getImg(dataList, r'D:\1\zhnegchang\\')  传入图片连接列表和保存路径进行下载
