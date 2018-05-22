Unicode and UTF-8

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode0.jpg)

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode1.jpg)

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode2.jpg)

查看系统编码方式：  
\>>> import sys  
\>>> sys.getfilesystemencoding()  
\>>> 'utf-8'

编码测试：  
\>>> test1 = '亁颐堂'  
\>>> test1.encode()  
b'\xe4\xba\x81\xe9\xa2\x90\xe5\xa0\x82'  
\>>> test1.encode('gbk')  
b'\x81x\xd2\xc3\xcc\xc3'  
\>>> test1.encode('gb18030')  
b'\x81x\xd2\xc3\xcc\xc3'

解码测试(尾部添加了\x01)：  
\>>> octets1 = b'\xe4\xba\x81\xe9\xa2\x90\xe5\xa0\x82\x01'  
\>>> octets1.decode()  
'亁颐堂\x01'  
\>>> octets1.decode('gbk')  
解码错误  
\>>> octets1.decode('gb18030')  
解码错误

ASCII字符会自动转码:  
\>>> print(b'\x73\x70\x01\x61\x6d')  
b'sp\x01am'  
\>>> b'sp\x01am' == b'\x73\x70\x01\x61\x6d'  
True
