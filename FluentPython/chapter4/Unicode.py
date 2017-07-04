#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


"""
总结： 1， python3 中字符串对象中是一个个 Unicode 字符（人类可识别的文本），每一个 Unicode 字符都有一个位码，如 A 的位码是 U+0041。
      2，字符的具体表述取决于所用的编码，编码是在位码和字节序列中转化的算法。
      3，位码->字节序列（编码）  字节序列->位码（解码）
      4，虽然字节序列实际上是整数序列，但其在显示的时候用了三种不同的显示方式
        a，可打印的ASCII范围内的字节 直接显示 ASCII 字符本身
        b，换行符等使用转义序列   \n
        c，其他字节的值，使用十六进制转义序列 (如 b'caf\xc3\xa9'）
"""

print("abc".encode("utf-8"))
b = "abcö".encode("utf-8")
print(b)

"""
b'abc'
b'abc\xc3\xb6'
"""

print(b.decode("utf8"))


        
