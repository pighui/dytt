# dytt
爬取电影天堂所有电影信息（模拟分布式）

如果对您有帮助，希望给个 Star ⭐，谢谢！😁😘🎁🎉

Github 项目地址 ：[pighui](https://github.com/pighui)/[dytt](https://github.com/pighui/dytt>)

# 克隆项目

```bash
git clone git@github.com:pighui/dytt.git
```

# 项目启动

## 1.安装Python

至少python3.5以上

## 2.安装mysql

至少mysql3.7以上

## 3.修改配置文件

修改项目根目录下的settings.py文件

## 4.安装依赖包

```bash
cd dytt
pip3 install -r requirements.txt
```

## 5.运行

```bash
scrapy crawl movie
```

## 6.添加任务

```python
python3 add_task.py
```