#-*- coding: utf-8 -*-
import pycurl,StringIO
import urllib,multiprocessing,json,datetime
class Logger():
    @staticmethod
    def _load(self,data = []):
        config = json.loads(open('../config.json','r').read())
        url = 'http://%s:%s/log/add/'%(config['HOST'],config['PORT'])
        crl = pycurl.Curl()
        crl.fp = StringIO.StringIO()
        crl.setopt(pycurl.URL, url)
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
        crl.setopt(pycurl.VERBOSE, 0)
        crl.setopt(crl.POST, 1)
        crl.setopt(crl.POSTFIELDS, urllib.urlencode(data))
        crl.perform()
        crl.close()
        return crl.fp.getvalue()

    @staticmethod
    def _format_data(data):
        data['time'] = datetime.datetime.now().strftime('%Y-%m-%d %x')

    @staticmethod
    def _log(data):
        p = multiprocessing.Process(target=Logger._load, args=data)
        p.start()

    @staticmethod
    def info(data):
        data['level'] = 'INFO'
        Logger._log(data)
