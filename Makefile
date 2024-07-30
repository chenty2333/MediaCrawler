# 定义默认值
platform := 
type := search

# 检查传入的参数，如果有则使用传入的参数
ifneq ($(strip $(type)),)
  type := $(type)
endif

run:
	python main.py --platform $(platform) --lt qrcode --type $(type)
ifeq ($(platform),dy)
	cat data/douyin/json/search_contents_2024-07-29.json | python SCRIPT/dy_filterVedio.py | python SCRIPT/dy_save.py
else ifeq ($(platform),bili)
	cat data/bilibili/json/search_contents_2024-07-29.json | python SCRIPT/bili_filterVideo.py | python SCRIPT/bili_save.py
endif

schedule:
	python SCRIPT/scheduler.py $(platform) $(type) $(sleep) $(times)

# 传递参数
.PHONY: run schedule
