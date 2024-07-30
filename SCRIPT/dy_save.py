import json
import sys
import os

def save_data(data, sort_by_likes=True):  # 默认值为True
    file_path = "json_data/dy_data.json"
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    combined_data = existing_data + data

    # 去重
    unique_data = {entry['url']: entry for entry in combined_data}.values()
    
    if sort_by_likes:
        unique_data = sorted(unique_data, key=lambda x: x['likes'], reverse=True)
    
    with open(file_path, 'w') as file:
        json.dump(list(unique_data), file, ensure_ascii=False, indent=4)

def parse_input(input_data):
    entries = input_data.strip().split('----------------------------------------')
    data = []

    for entry in entries:
        if entry.strip():
            lines = entry.strip().split('\n')
            nickname = lines[0].split(': ')[1]
            title = lines[1].split(': ')[1]
            url = lines[2].split(': ')[1]
            likes = int(lines[3].split(': ')[1])
            plays = int(lines[4].split(': ')[1])
            data.append({"nickname": nickname, "title": title, "url": url, "likes": likes, "plays": plays})

    return data

if __name__ == "__main__":
    input_data = sys.stdin.read()
    parsed_data = parse_input(input_data)
    save_data(parsed_data, sort_by_likes=True)  # 默认开启排序
