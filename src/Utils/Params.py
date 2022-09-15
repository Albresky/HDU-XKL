#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/5/12 14:52
# @File    : headers.py
# @Software: PyCharm


headers_skl2cas = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "cas.hdu.edu.cn",
    "Referer": "https://skl.hduhelp.com/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"
}

headers_cas1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "cas.hdu.edu.cn",
    "Origin": "https://cas.hdu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"

}

headers_cas2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "skl.hdu.edu.cn",
    "Referer": "https://cas.hdu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"

}

headers_cas2skl = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://cas.hdu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"
}

headers_check_option = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Request-Headers": "skl-ticket,x-auth-token",
    "Access-Control-Requset-Method": "GET",
    "Connection": "keep-alive",
    "Host": "skl.hdu.edu.cn",
    "Origin": "https://skl.hduhelp.com",
    "Referer": "https://skl.hduhelp.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.27"
}

headers_check_get = {
    "Accept": "application/json,text/plain,*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "skl.hdu.edu.cn",
    "Origin": "https://skl.hduhelp.com",
    "Referer": "https://skl.hduhelp.com/",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.27"
}

headers_health_check = {
    "Accept": "application/json,text/plain,*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "skl.hdu.edu.cn",
    "Origin": "https://skl.hduhelp.com",
    "Referer": "https://skl.hduhelp.com/passcord.html?type=5",
    "X-Requested-With": "com.alibaba.android.rimet",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 12; zh-CN; Pixel 3 Build/SP1A.210812.016.C2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.210 Mobile Safari/537.36 AliApp(DingTalk/6.5.40) com.alibaba.android.rimet/25925543 Channel/36180121811227 language/zh-CN abi/32 UT4Aplus/0.2.25 colorScheme/light"
}

headers_health_check_options = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Request-Method": "POST",
    "Access-Control-Request-Headers": "content-type,skl-ticket,x-auth-token",
    "Connection": "keep-alive",
    "Host": "skl.hdu.edu.cn",
    "Origin": "https://skl.hduhelp.com",
    "X-Requested-With": "com.alibaba.android.rimet",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 12; zh-CN; Pixel 3 Build/SP1A.210812.016.C2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.210 Mobile Safari/537.36 AliApp(DingTalk/6.5.40) com.alibaba.android.rimet/25925543 Channel/36180121811227 language/zh-CN abi/32 UT4Aplus/0.2.25 colorScheme/light"
}

location_params = {
    "currentLocation": "浙江省杭州市钱塘区",
    "healthCode": 0,
    "city": "杭州市",
    "districtAdcode": "330114",
    "province": "浙江省",
    "district": "钱塘区",
    "healthReport": 0,
    "currentLiving": 0,
    "last14days": 0
}
