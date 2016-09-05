import urllib2

char = repr(u'\u91cd'.encode('utf-8'))
char = u'\u91cd'.encode('utf-8')

print char

url1 = 'http://starling.rinet.ru/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cchina%5Cdoc&first=1&off=&text_character=&method_character=substring&ic_character=on&text_mcinfo=&method_mcinfo=substring&ic_mcinfo=on&text_zihui=&method_zihui=substring&ic_zihui=on&text_beijing=&method_beijing=substring&ic_beijing=on&text_jinan=&method_jinan=substring&ic_jinan=on&text_xian=&method_xian=substring&ic_xian=on&text_taiyuan=&method_taiyuan=substring&ic_taiyuan=on&text_hankou=&method_hankou=substring&ic_hankou=on&text_chengdu=&method_chengdu=substring&ic_chengdu=on&text_yangzhou=&method_yangzhou=substring&ic_yangzhou=on&text_suzhou=&method_suzhou=substring&ic_suzhou=on&text_wenzhou=&method_wenzhou=substring&ic_wenzhou=on&text_changsha=&method_changsha=substring&ic_changsha=on&text_shuangfeng=&method_shuangfeng=substring&ic_shuangfeng=on&text_nanchang=&method_nanchang=substring&ic_nanchang=on&text_meixian=&method_meixian=substring&ic_meixian=on&text_guangzhou=&method_guangzhou=substring&ic_guangzhou=on&text_xiamen=&method_xiamen=substring&ic_xiamen=on&text_chaozhou=&method_chaozhou=substring&ic_chaozhou=on&text_fuzhou=&method_fuzhou=substring&ic_fuzhou=on&text_shanghai=&method_shanghai=substring&ic_shanghai=on&text_zhongyuan=&method_zhongyuan=substring&ic_zhongyuan=on&text_any='
url2 = '&method_any=substring&sort=number&ic_any=on'

print url1+char+url2

response = urllib2.urlopen(url1+char+url2)
print response.read()

#f = open('nanchangresultpage.txt', 'w')
#for line in response.read():
#    f.write(line)

#f.close()
