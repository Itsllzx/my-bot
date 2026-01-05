import requests
import re

# سورس‌های معتبر و تازه
SOURCES = [
    "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/protocols/vless",
    "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/protocols/vmess",
    "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/protocols/trojan",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/All_Configs_Sub.txt"
]

def main():
    all_configs = []
    for url in SOURCES:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                # استخراج لینک‌ها با استفاده از Regex
                configs = re.findall(r'(vless|vmess|trojan|ss)://[^\s]+', res.text)
                all_configs.extend(configs)
        except:
            continue
    
    # فقط ۵۰ تا از بهترین‌ها را نگه دار
    final_configs = list(set(all_configs))[:50]
    
    # ذخیره در فایل
    with open("assets/data/content.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(final_configs))
    print(f"Successfully saved {len(final_configs)} configs.")

if __name__ == "__main__":
    main()
