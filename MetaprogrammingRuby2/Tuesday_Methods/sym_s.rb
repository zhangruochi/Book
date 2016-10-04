#符号和字符串转化
puts "abc".to_sym
puts :abc.to_s

#符号不可修改 字符串可以修改

#1+2 
puts 1.send("+",2)
puts 1.send(:+,3)  #通常使用符号作为方法名