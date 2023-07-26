# -*- coding:UTF-8 -*-
services = {}  # (key:ip, value:서비스용량)이 저장될 딕셔너리 자료구조

with open('dev_access_log.20150611', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        servicebyte = log[9]

        if servicebyte.isdigit():
            servicebyte = int(servicebyte)
        else:  # 제공한 콘텐츠의 크기가 0일 경우 '-'다음과 같은 문자로 정해지기에...
            servicebyte = 0

        if ip not in services:
            services[ip] = servicebyte
        else:
            services[ip] += servicebyte

ret = sorted(services.items(), key=lambda x: x[1], reverse=True)  # 서비스 용량을 기준으로 내림차순 정리

print('=' * 8 , '사용자IP - 서비스 용량' , '=' * 8)

for ip, b in ret:
    print('[IP ADDRESS: %s] - [%d byte]' % (ip, b))