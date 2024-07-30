#!/usr/bin/env python3

import sys  # 导入sys模块，用于读取标准输入
import json  # 导入json模块，用于处理JSON数据

# 从标准输入读取JSON数据
data = json.load(sys.stdin)

# 定义筛选条件：点赞数大于10000
liked_threshold = 10000
share_threshold = 100  # 分享数量
comment_threshold = 100  # 评论数量

# 根据筛选条件过滤数据
filtered_data = [
    {
        "Nickname": item["nickname"],  # 用户昵称
        "Title": item["title"],        # 视频标题
        "URL": item["aweme_url"],      # 视频URL
        "Likes": item["liked_count"],  # 点赞数
        "Shares": item["share_count"], # 分享数
        "Comments": item["comment_count"]  # 评论数
    }
    for item in data
    if int(item["liked_count"]) > liked_threshold and int(item["share_count"]) > share_threshold and int(item["comment_count"]) > comment_threshold
]

# 以人类可读的格式打印过滤后的数据
for video in filtered_data:
    print(f"Nickname: {video['Nickname']}")  # 打印用户昵称
    print(f"Title: {video['Title']}")        # 打印视频标题
    print(f"URL: {video['URL']}")            # 打印视频URL
    print(f"Likes: {video['Likes']}")        # 打印点赞数
    print(f"Shares: {video['Shares']}")      # 打印分享数
    print(f"Comments: {video['Comments']}")  # 打印评论数
    print("-" * 40)                          # 打印分隔线
