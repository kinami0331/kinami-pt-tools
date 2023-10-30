# kinami-pt-tools

一些个人使用的 PT 小工具

## 列表及说明

### 检查文件是否存在

用于检查当前做种中的种子对应的文件是否存在，防止删除原始种子后，辅种的种子出现做假种现象。

依赖：
```bash
pip install qbittorrent-api tqdm
```

见 [check_qbit_files.py](./check_qbit_files.py)