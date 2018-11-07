from time import sleep

from bs4 import BeautifulSoup
import requests
import csv

def map():
    url = "http://cd.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

# 已完成的页数序号，初时为0
    page = 0

    csv_file = open("./static/rent.csv", "w")

# 创建writer对象，指定文件与分隔符
    csv_writer = csv.writer(csv_file, delimiter=',')

    while True:
        page += 1
        print("fetch: ", url.format(page=page))
        sleep(0.2)
    # 抓取目标页面
        response = requests.get(url.format(page=page))
    # 创建一个Beautiful对象
        html = BeautifulSoup(response.text)
    # 获取class = list的元素下的所有li元素
        house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
        if not house_list:
            break

        for house in house_list:
                            #　得到标签包裹着的文本
            house_title = house.select("h2")[0].string
                                                # 得到标签内的属性值
            house_url = "http://cd.58.com/%s" % (house.select("a")[0]["href"])
            house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
            if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
                house_location = house_info_list[0]
            else:
                house_location = house_info_list[1]

            house_money = house.select(".money")[0].select("b")[0].string

        # 写一行数据
            csv_writer.writerow(
                [house_title, house_location, house_money, house_url])

    csv_file.close()
