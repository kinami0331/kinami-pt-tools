# kinami-pt-tools

一些个人使用的 PT 小工具

## 下载器相关

### qBittorrent

#### 检查文件是否存在

用于检查当前做种中的种子对应的文件是否存在，防止删除原始种子后，辅种的种子出现做假种现象。

依赖：
```bash
pip install qbittorrent-api tqdm
```

见 [check_qbit_files.py](./check_qbit_files.py)

## 站点相关

### 天雪

#### 字幕下载辅助记录插件

用于辅助记录下载过的字幕，并可以在字幕列表中直接下载。

见 [代码文件](./websites/skyeysnow/skyey_snow_sub_helper.js) 或 
[Greasy Fork 链接](https://greasyfork.org/zh-CN/scripts/475247-%E5%A4%A9%E9%9B%AA%E4%B8%8B%E5%AD%97%E5%B9%95%E8%B5%9A%E9%87%91%E5%B8%81%E5%8A%A9%E6%89%8B)

