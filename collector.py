import requests
import base64
import random
import re

# منابع جمع‌آوری کانفیگ
SOURCES = [
    "https://raw.githubusercontent.com/Iranian-V2Ray/V2Ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyMaster/master/Text_Sub.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/vfarid/v2ray-share/main/all.txt",
    "https://github.com/barry-far/V2ray-Config/blob/main/All_Configs_Sub.txt",
    "https://https://github.com/Epodonios/v2ray-configs/blob/main/All_Configs_Sub.txt"
  
]

def get_configs():
    all_configs = set()
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                content = response.text
                if "vmess://" not in content and "vless://" not in content:
                    try:
                        content = base64.b64decode(content).decode('utf-8')
                    except:
                        pass
                found = re.findall(r'(vless|vmess|trojan|ss|ssr)://[^\s]+', content)
                for c in found:
                    config_link = re.search(rf'{c}://[^\s]+', content)
                    if config_link:
                        all_configs.add(config_link.group(0))
        except:
            continue
    return list(all_configs)

def main():
    configs = get_configs()
    valid_configs = [c for c in configs if len(c) > 10]
    
    # انتخاب ۱۰۰ عدد رندوم
    if len(valid_configs) > 100:
        selected_configs = random.sample(valid_configs, 100)
    else:
        selected_configs = valid_configs
        
    with open("assets/data/content.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(selected_configs))

if __name__ == "__main__":
    main()
