# -*- encoding:UTF-8 -*-
'''
Created on 2018. 12. 12.
'''
pageviews = 0       # 총 페이지 뷰 수 체크
visit_ip = []       # 고유 접속자 수 체크

KB = 1024
total_service = 0   # 총 서비스 용량 계산

services = {}       # 사용자별 서비스용량 계산 딕셔너리

with open('dev_access_log.20150611', 'r') as f:
    logs = f.readlines();
    print("statistic len [%d]" , len(logs))
    for log in logs :
        separated = log.split()
        try :

            status = separated[8]       # http 접속 상태
            ip = separated[0]           # 접속 ip
            serviceByte = separated[9]  # 서비스 용량

            if status == '200' :
                pageviews += 1

            if ip not in visit_ip :
                visit_ip.append(ip)

            if serviceByte.isdigit() :
                total_service += int(serviceByte)       # str 이기 때문에 int 로 형변환

            if ip not in services :
                services[ip] = serviceByte
            else :
                services[ip] += serviceByte

        except IndexError as e:
            print(logs)

print()
print("총 페이지 뷰 수 : [%d]" %pageviews)
print()
print("고유 접속자 수 : [%d]" %len(visit_ip))
print()
total_service = total_service/KB
print("총 서비스 용량 %dKB" %total_service)
print()

ret = sorted(services.items(), key = lambda x:x[1] , reverse=True)
print("=" * 8 , "사용자 IP - 서비스 용량 " , "=" * 8)
for ip , b in ret :
    print("사용자 IP [%s] , 사용량 [%d]"  %(ip , b))