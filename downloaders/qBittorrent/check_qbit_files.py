import qbittorrentapi
from tqdm import tqdm
from pathlib import Path

def print_tqdm(*args, **kwargs):
    tqdm.write(' '.join(map(str, args)), **kwargs)

# 修改为你的配置
conn_info = dict(
    host="localhost",
    port=9000,
    username="USERNAME",
    password="PASSWORD",
)

qb_client = qbittorrentapi.Client(**conn_info)

try:
    qb_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

print(f"qBittorrent: {qb_client.app.version}")
print(f"qBittorrent Web API: {qb_client.app.web_api_version}")
for k, v in qb_client.app.build_info.items():
    print(f"{k}: {v}")


for torrent in tqdm(qb_client.torrents_info(), position=0, desc="torrents", leave=True):
    if torrent.state in ["downloading", "stalled_downloading"]:
        continue
    category = torrent["category"]
    torrent_name = torrent["name"]
    save_path = torrent["save_path"]
    save_path_obj = Path(save_path)

    for f in tqdm(torrent.files, position=1, desc="files", leave=False):
        full_path_obj = save_path_obj / Path(f["name"])
        if not full_path_obj.exists():
            print_tqdm("[NOT FOUND!]", category, torrent_name, full_path_obj.resolve())

qb_client.auth_log_out()