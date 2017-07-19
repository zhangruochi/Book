brl = 1/2.43
print(brl)
print(format(brl,"0.4f"))
print("1 BRL = {rate:0.2f} USD".format(rate=brl))

#内置类型的专有表示代码
print(format(42,"b"))
print(format(2/3,'.1%'))

from datetime import datetime
now = datetime.now()
print(format(now,"%H:%M:%S"))
print("It's time {: %I:%M:%p}".format(now))


