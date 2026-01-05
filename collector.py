import requests
import re

# سورس‌های مستقیم و تست شده
SOURCES = [
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub1.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt",
"https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/master/servers.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt",
"https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/Sub1.txt",
"https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/all_extracted_configs.txt",
"https://raw.githubusercontent.com/Joker-funland/V2ray-configs/main/vmess.txt",
"https://raw.githubusercontent.com/Net-Account/Config/main/All.txt",
"https://raw.githubusercontent.com/M-Mashreghi/Free-V2ray-Collector/main/shuffle/Sub1_shuffled.conf",
"https://raw.githubusercontent.com/mrvcoder/V2rayCollector/main/vmess_iran.txt",
"https://raw.githubusercontent.com/hamed1124/port-based-v2ray-configs/main/sub.txt",
"https://raw.githubusercontent.com/ShatakVPN/ConfigForge-V2Ray/main/configs.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/super-sub.txt",
"https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/Sub20.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_base64_Sub.txt",
"https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/vless_configs.txt",
"https://raw.githubusercontent.com/Joker-funland/V2ray-configs/main/warp.txt",
"https://raw.githubusercontent.com/Joker-funland/V2ray-configs/main/hy2.txt"

]

def main():
    all_configs = []
    for url in SOURCES:
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                # استخراج هر چیزی که شبیه لینک کانفیگ باشد
                configs = re.findall(r'(?:vless|vmess|trojan|ss|ssr)://[^\s<>"]+', res.text)
                all_configs.extend(configs)
        except Exception as e:
            print(f"Error reading {url}: {e}")
            continue
    
    # حذف تکراری‌ها و انتخاب ۱۰۰ مورد اول
    unique_configs = list(dict.fromkeys(all_configs))
    final_configs = unique_configs[:100]
    
    if final_configs:
        with open("assets/data/content.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(final_configs))
        print(f"✅ Success! {len(final_configs)} configs saved.")
    else:
        print("❌ No configs found at all!")

if __name__ == "__main__":
    main()
