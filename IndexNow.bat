@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM ========== 配置区 ==========
set HOST=www.enkidu.site
set KEY=e2085757ad464a3d8e6b7ba5afd580bf
set INDEXNOW_ENDPOINT=https://api.indexnow.org/IndexNow
REM ===========================

REM 定义 URL 列表 (因为批处理数组处理复杂，这里构造一个 JSON 数组字符串)
set "URL_LIST=["
for %%u in (
    "https://www.enkidu.site/zh-cn/"
    "https://www.enkidu.site/zh-cn/archives"
    "https://www.enkidu.site/zh-cn/about"
    "https://www.enkidu.site/zh-cn/post/命运_奇异赝品_黎明低语/"
    "https://www.enkidu.site/zh-cn/post/恩奇都出场合集/"
    "https://www.enkidu.site/zh-cn/post/群友绘画活动/"
    "https://www.enkidu.site/zh-cn/post/官图合集/"
    "https://www.enkidu.site/zh-cn/post/科普汇总/"
    "https://www.enkidu.site/zh-cn/post/飞扬的恩鸡都/"
    "https://www.enkidu.site/zh-cn/post/合成恩奇都/"
    "https://www.enkidu.site/zh-cn/post/2048/"
    "https://www.enkidu.site/en/"
    "https://www.enkidu.site/en/archives"
    "https://www.enkidu.site/en/about"
    "https://www.enkidu.site/en/post/命运_奇异赝品_黎明低语/"
    "https://www.enkidu.site/en/post/恩奇都出场合集/"
    "https://www.enkidu.site/en/post/群友绘画活动/"
    "https://www.enkidu.site/en/post/官图合集/"
    "https://www.enkidu.site/en/post/科普汇总/"
    "https://www.enkidu.site/en/post/飞扬的恩鸡都/"
    "https://www.enkidu.site/en/post/合成恩奇都/"
    "https://www.enkidu.site/en/post/2048/"
) do set "URL_LIST=!URL_LIST!%%~u,"

REM 移除最后一个逗号并闭合数组
set "URL_LIST=%URL_LIST:~0,-1%]"

REM 构造完整的 JSON 请求体
set "JSON={\"host\":\"%HOST%\",\"key\":\"%KEY%\",\"keyLocation\":\"https://%HOST%/%KEY%.txt\",\"urlList\":%URL_LIST%}"

echo 正在提交 Sitemap 到 IndexNow ...
echo 主机: %HOST%
echo 密钥位置: https://%HOST%/%KEY%.txt
echo 提交 URL 数量: 22
echo =====================================

REM 发送 POST 请求
curl -X POST "%INDEXNOW_ENDPOINT%" ^
     -H "Content-Type: application/json; charset=utf-8" ^
     -d "!JSON!"

echo.
echo =====================================
echo 执行完毕，请检查上方返回的 HTTP 状态码。
echo 200 表示成功，其他代码请参考文档。
pause