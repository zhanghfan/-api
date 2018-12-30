# coding = utf-8
import requests
import time
import pymysql
def connect_db():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='sql123_206_68_1',
                           passwd='kwtJSZcWKh',
                           db='sql123_206_68_1',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor,conn

def get_info(citycode='101010100'):
    url="http://t.weather.sojson.com/api/weather/city+"+citycode
    r=requests.get(url)
    return r.text

def update_info():
    cursor,conn=connect_db()
    cursor.execute('select city_code from ins_county')
    listcodes=cursor.fetchall()
    conn.commit()
    for citycode in listcodes:
        time.sleep(0.3)
        info=get_info(citycode['county_name'])
        sql="UPDATE ins_county SET weather_info='%s' WHERE county_name=%s"%(info,citycode['county_name'])
        try:
            cursor.execute(sql)
            conn.commit()
            print("{}写入成功".format(citycode['county_name']))
        except:
            conn.rollback()

if __name__ == "__main__":
    update_info()