<?php
namespace app\api\model;

use think\Model;
use think\Db;

class Weather extends Model
{
    public function getCityCode($county_name = '北京')
    {
        $res = Db::name('ins_county')->where('county_name', $county_name)->column('weather_code');
        return $res;
    }

    public function getWeather($weather_code = '101010100')
    {
        $res = Db::name('ins_county')->where('weather_code', $weather_code)->column('weather_info');
        return $res;
    }
}