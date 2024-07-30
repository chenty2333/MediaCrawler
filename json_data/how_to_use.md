## 如何通过make run命令使用：
- 进入根目录下，使用make run并传递参数可以直接使用
- make run接受两个参数platform和type，platform的值可以是bili或者dy，type默认等于search
- 可以使用make run platform=bili或者是make run platform=bili type=search进行使用
- 如需读取指定的帖子ID列表(详见MediaCrawler源项目),可使用type=detail

## 使用make schedule定时运行
- make run接受四个参数platform，type，sleep，times.前两个参数同上
- sleep为两次爬取中间的时间间隔，单位为分钟
- times为执行次数
- 可以使用make schedule platform=bili sleep=10 times=5，执行5次，间隔十分钟

## 保存
- 使用make run或make schedule执行，数据会保存在MediaCrawler/json_data下
- 数据通过bili_save.py和dy_save.py脚本进行保存
- 脚本中已包含排序去重功能，默认按照Likes（点赞数）排序
- 排序功能可以通过进入bili_save.py和dy_save.py中，将True修改为False关闭