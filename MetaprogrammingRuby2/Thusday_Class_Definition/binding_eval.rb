#binding  对象绑定当前作用域  可以把 binding 对象看成比块更加纯净的闭包

class MyClass
    def my_method
        @x = 1
        binding
    end
end

puts eval "@x",MyClass.new.my_method
# 1


#Here Dcoument

eval <<end_eval
    def print_my_name
        puts "my name is zhangruochi"
    end
    print_my_name
end_eval


