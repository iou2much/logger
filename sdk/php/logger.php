<?php
/*
 * ../config.json中配置有服务器IP,端口,以及接入系统名
 * 
 * 默认提供info,warn,error,debug四种级别方法 
 * 传入参数$data,可为字符串，或数组
 * 调用前须设定模块名----Logger::mod_name = 'module_name';
   固定字段: sys,mod_name,level,time,func,_rid_,ip
 */
class Logger{
    private static $HOST = null;
    private static $PORT = null;
    private static $SYS  = null;
    public static $mod_name = null;

    private static function init(&$data){
        $config = json_decode(trim(file_get_contents('../config.json')),true);
        Logger::$HOST = $config['HOST'];
        Logger::$PORT = $config['PORT'];
        Logger::$SYS  = $config['SYS'];
    }

    private static function send(&$data){
        #echo "send\n";

        $fp = fsockopen(Logger::$HOST, Logger::$PORT, $errno, $errstr, 30);
        if (!$fp) {
            echo "Logger Server's down!! $errstr ($errno)<br />\n";
        } else {
            $out = "POST /log/add/ HTTP/1.1\r\nHost: ".Logger::$HOST."\r\n";
            $post = array();
            while (list($k,$v) = each($data)) {
                $post[] = rawurlencode($k)."=".rawurlencode($v);
            }
            $post = implode('&',$post);
            $len = strlen($post);

            $out .= "Content-type: application/x-www-form-urlencoded\r\nConnection: Close\r\nContent-Length: $len\r\n\r\n";
            $out .= $post."\r\n";
         
            fwrite($fp, $out);
            /*忽略执行结果*/
            while (!feof($fp)) {echo fgets($fp, 128);}
            fclose($fp);
        }
    }

    public static function format_data(&$data){
        if(!Logger::$HOST) Logger::init($data);
        if(is_string($data)){
            $data = array('msg'=>$data);
        }
        $data['time'] = date('Y-m-d H:i:s');
        $data['mod'] = Logger::$mod_name !=null ? Logger::$mod_name:'';
        $data['sys'] = Logger::$SYS;
    }

    public static function info($data){
        Logger::format_data($data);
        $data['level'] = 'INFO';
        Logger::send($data);
    }

    public static function error($data){
        Logger::format_data($data);
        $data['level'] = 'ERROR';
        $trc = debug_backtrace();
        $data['trace'] = $trc;
        Logger::send($data);
    }

    public static function debug($data,$mode=false){
        Logger::format_data($data);
        $data['level'] = 'DEBUG';

        $trc = debug_backtrace();
        if(!$mode){
            $trc = $trc[0];
            $data['file'] = $trc['file'];
            $data['line'] = $trc['line'];
        }else{
            $data['trace'] = $trc;
        }
        Logger::send($data);
    }

    public static function warn($data){
        Logger::format_data($data);
        $data['level'] = 'WARNING';
        Logger::send($data);
    }
}

#Logger::info(array('info'=>'什么adfadf','author'=>'author'));
#Logger::info('中文什么adfadf');
?>
