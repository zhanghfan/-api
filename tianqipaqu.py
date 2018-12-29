# coding=utf-8
import sys
import requests
import pymysql
from bs4 import BeautifulSoup as bs

reload(sys)
sys.setdefaultencoding('utf-8')
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='数据库用户名',
                       passwd='你的密码',
                       db='数据库名',
                       charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select weather_code from ins_county')
result = cursor.fetchall()
conn.commit()
for i in range(len(result)):
    citycode = result[i]['weather_code']
    url = "http://wthrcdn.etouch.cn/WeatherApi?citykey=" + citycode
    r = requests.get(url, verify=False)
    soup = bs(r.text, 'html.parser')

    wendu = soup.find('wendu').text
    fengli = soup.find('fengli').text
    shidu = soup.find('shidu').text
    fengxiang = soup.find('fengxiang').text
    if soup.find('pm25'):
        pm25 = soup.find('pm25').text
    else:
        pm25 = 'Null'
    if soup.find('quality'):
        quality = soup.find('quality').text
    else:
        quality = 'Null'
    if soup.find('high_1'):
        high = soup.find('high').text
    else:
        high = 'Null'
    if soup.find('low_1'):
        low = soup.find('low').text
    else:
        low = 'Null'
    weather_content = '温度:' + wendu + '℃' + '\n风力:' + fengli + '\n适度:' + shidu + '\n风向:' + fengxiang + '\nPM2.5:' + pm25 + '\n空气质量:' + quality + '\n温度范围:' + low + '-' + high + '℃'
    sql_exe = 'UPDATE ins_county SET weather_info = \''\
              + weather_content + '\' WHERE weather_code = ' + citycode +' '
    print(sql_exe)
    cursor.execute(sql_exe)
    conn.commit()
cursor.close()
conn.close()