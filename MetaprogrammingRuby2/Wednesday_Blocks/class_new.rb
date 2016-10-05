# 扁平化作用域 
#将 变量 穿越作用域门

my_variables = "zhangruochi"

MyClass = Class.new do     #将 class 改为 Class.new 方法

    puts "my variable in MyClass is: #{my_variables}"

    define_method :func do   #define_method 是 kernel 的 private_method
        puts "my variable in func is: #{my_variables}"
    end
end


MyClass.new.func
=begin
output:
    my variable in MyClass is: zhangruochi
    my variable in func is: zhangruochi
=end


