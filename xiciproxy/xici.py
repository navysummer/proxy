# --*-- coding:utf-8 --*--
try:
    import urlparse
except Exception as e:
    from urllib import parse as urlparse
import requests
from bs4 import BeautifulSoup

class XCproxy(object):
    def __init__(self,url='https://www.xicidaili.com'):
        self.url = url
        self.parsed_tuple = urlparse.urlparse(self.url)
        self.headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': self.parsed_tuple.netloc,
            'If-None-Match': 'W/"0da2948c0760aff77c34cd2b39e915e9"',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }

    def gaoni(self,page=1):
        url = '%s/nn/%s'%(self.url,page)
        r = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(r.text,'lxml')
        trs = soup.find('table',id='ip_list').find_all('tr')[1:]
        # ips = [{tr.find_all():} for tr in trs]
        proxy = []
        for tr in trs:
            tds = tr.find_all('td')
            protocol = tds[5].text.strip().lower()
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            proxy.append({protocol:'%s://%s:%s'%(protocol,ip,port)})
        return proxy

    def putong(self,page=1):
        url = '%s/nt/%s'%(self.url,page)
        r = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(r.text,'lxml')
        trs = soup.find('table',id='ip_list').find_all('tr')[1:]
        # ips = [{tr.find_all():} for tr in trs]
        proxy = []
        for tr in trs:
            tds = tr.find_all('td')
            protocol = tds[5].text.strip().lower()
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            proxy.append({protocol:'%s://%s:%s'%(protocol,ip,port)})
        return proxy

    def https(self,page=1):
        url = '%s/wn/%s'%(self.url,page)
        r = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(r.text,'lxml')
        trs = soup.find('table',id='ip_list').find_all('tr')[1:]
        # ips = [{tr.find_all():} for tr in trs]
        proxy = []
        for tr in trs:
            tds = tr.find_all('td')
            protocol = tds[5].text.strip().lower()
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            proxy.append({protocol:'%s://%s:%s'%(protocol,ip,port)})
        return proxy

    def http(self,page=1):
        url = '%s/wt/%s'%(self.url,page)
        r = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(r.text,'lxml')
        trs = soup.find('table',id='ip_list').find_all('tr')[1:]
        # ips = [{tr.find_all():} for tr in trs]
        proxy = []
        for tr in trs:
            tds = tr.find_all('td')
            protocol = tds[5].text.strip().lower()
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            proxy.append({protocol:'%s://%s:%s'%(protocol,ip,port)})
        return proxy
