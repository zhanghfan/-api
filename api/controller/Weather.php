<?php
namespace app\api\controller;
 
use think\Controller;
 
class Weather extends Controller
{
    public function read()
    {
        $weather_code = input('weather_code');
        $model = model('Weather');
        $data = $model->getWeather($weather_code);
      	$data = [
          $weather_code =>$data[0]
        ];
       
      	return json($data);
    }
  	public function getCityCode(){
        $county_name = input('county_name');
        $model = model('Weather');
        $data = $model->getCityCode($county_name);
      	$data = [
            $county_name => $data[0]
        ];
        return json($data);
    }
}