<?php
require_once('../php/logger.php');
Logger::$mod_name = 'test-module2';

function a(){
    $data['msg'] = 'cccc';
    $data['aaa'] = '333333333';
    $data['sdfadsf'] = '4444';
    $data['ip'] = '1278121';
    $data['func'] = 'func_a';
    $data['_rid_'] = 'func_a';
    Logger::info($data);

    $data['msg'] = 'bbbbbb';
    $data['aaa'] = 'lllllllll';
    $data['sdfadsf'] = 'xxxxxx';
    $data['ip'] = 'zzzzzzzz';
    $data['func'] = 'func_a';
    $data['_rid_'] = 'func_b';
    Logger::debug($data);
}

function b(){
    a();
}

b();
?>
