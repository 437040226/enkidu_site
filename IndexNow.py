import json
import requests
import sys

# 配置信息
HOST = "www.enkidu.site"
KEY = "e2085757ad464a3d8e6b7ba5afd580bf"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/IndexNow"

# 完整的 URL 列表
URL_LIST = [
    "https://www.enkidu.site/",
    "https://www.enkidu.site/zh-cn/",
    "https://www.enkidu.site/zh-cn/archives",
    "https://www.enkidu.site/zh-cn/about",
    "https://www.enkidu.site/zh-cn/post/命运_奇异赝品_黎明低语/",
    "https://www.enkidu.site/zh-cn/post/恩奇都出场合集/",
    "https://www.enkidu.site/zh-cn/post/群友绘画活动/",
    "https://www.enkidu.site/zh-cn/post/官图合集/",
    "https://www.enkidu.site/zh-cn/post/科普汇总/",
    "https://www.enkidu.site/zh-cn/post/飞扬的恩鸡都/",
    "https://www.enkidu.site/zh-cn/post/合成恩奇都/",
    "https://www.enkidu.site/zh-cn/post/2048/",
    "https://www.enkidu.site/en/",
    "https://www.enkidu.site/en/archives",
    "https://www.enkidu.site/en/about",
    "https://www.enkidu.site/en/post/命运_奇异赝品_黎明低语/",
    "https://www.enkidu.site/en/post/恩奇都出场合集/",
    "https://www.enkidu.site/en/post/群友绘画活动/",
    "https://www.enkidu.site/en/post/官图合集/",
    "https://www.enkidu.site/en/post/科普汇总/",
    "https://www.enkidu.site/en/post/飞扬的恩鸡都/",
    "https://www.enkidu.site/en/post/合成恩奇都/",
    "https://www.enkidu.site/en/post/2048/"
]

def main():
    """主函数：提交URL列表到IndexNow"""
    print("=" * 50)
    print("正在提交网址到 IndexNow ...")
    print(f"主机: {HOST}")
    print(f"密钥: {KEY}")
    print(f"密钥文件位置: https://{HOST}/{KEY}.txt")
    print(f"提交 URL 数量: {len(URL_LIST)}")
    print("=" * 50)

    # 构建请求数据
    data = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": URL_LIST
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    try:
        # 打印调试信息（可选，查看实际发送的数据）
        print("正在发送请求...")
        print(f"请求端点: {INDEXNOW_ENDPOINT}")
        print("=" * 50)
        
        # 发送 POST 请求
        response = requests.post(INDEXNOW_ENDPOINT, json=data, headers=headers, timeout=30)
        http_code = response.status_code
        
        print(f"HTTP 状态码: {http_code}")
        
        # 尝试解析JSON响应
        try:
            response_json = response.json()
            print(f"API响应内容: {json.dumps(response_json, indent=2, ensure_ascii=False)}")
        except ValueError:
            print(f"响应文本: {response.text}")
        
        print("=" * 50)
        
        # 修正：将 202 也视为成功状态码
        if http_code == 200 or http_code == 202:
            print(f"✅ 成功！(状态码: {http_code})")
            if http_code == 200:
                print("   IndexNow 已确认接收并处理您的提交。")
            elif http_code == 202:
                print("   IndexNow 已接受您的请求，正在排队处理中。")
            print(f"   已成功提交 {len(URL_LIST)} 个网址。")
            print("   搜索引擎将会在接下来几小时到几天内处理这些更新。")
        elif http_code == 403:
            print("❌ 失败：密钥无效 (403 Forbidden)。")
            print("   请检查：")
            print(f"   1. 确保文件 https://{HOST}/{KEY}.txt 可以公开访问")
            print(f"   2. 文件内容必须只包含一行：{KEY}（无空格、无换行）")
        elif http_code == 422:
            print("❌ 失败：请求无法处理 (422 Unprocessable Entity)。")
            print("   可能原因：")
            print("   1. 提交的URL不属于该域名")
            print("   2. 密钥格式错误")
            print("   3. 请求参数格式不正确")
            print(f"   请检查所有URL是否都以 https://{HOST}/ 开头")
        elif http_code == 429:
            print("⚠️  警告：请求过于频繁 (429 Too Many Requests)。")
            print("   请等待几分钟后再试。")
        else:
            print(f"❌ 提交失败，HTTP 状态码: {http_code}")
            print(f"   请参考 IndexNow 文档了解此状态码的含义。")

    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求出错: {e}")
        print("   请检查网络连接或稍后重试。")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
    if sys.platform == "win32":
        input("\n按 Enter 键退出...")