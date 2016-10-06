# 代码块在函数中的传递
def math(a,b)
    yield a,b 
end

def do_math(a,b,&operation)
    math(a,b,&operation)
end

do_math(5,5){|x,y| puts x+y}

#代码块转化为 Proc 对象 这个技巧成为延迟执行
inc = Proc.new {|x| puts x+1}
inc.call 2

inc_2 = proc {|x| puts x+1}
inc_2.call 2

inc_3 = lambda {|x| puts x+1}
inc_3.call 2

# &operation  操作符& 表示的意思是 operation 是一个 Proc 对象 把它当做代码块执行
def my_method(&operation)
    operation
end

p = my_method {|name| puts "My name is #{name}"}
p.call :zhangruochi


def my_method(greeting)
    puts "#{greeting},#{yield}"
end

my_proc = proc {:zhangrucohi}
#my_method("Hey!") {:zhangrucohi}
my_method("Hey!",&my_proc)






