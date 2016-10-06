#当一个类包含一个模块时，它获得的是该模块的实例方法 而不是类方法
#下面的代码把模块的普通方法编程类的类方法

#类扩展
module MyModule
    def print_name
        puts "My name is zhangruochi"
    end
end

class MyClass
    class << self
        include MyModule
    end
end

MyClass.print_name # My name is zhangruochi



#对象扩展
module MyModule_2
    def print_my_firstname
        puts "My firstname is zhang"
    end
end

obj = MyClass.new
class << obj
    include MyModule_2
end

obj.print_my_firstname



#利用 extend 方法进行扩展
module MyModule_3
    def print_my_lastname
        puts "My lastname is ruochi"
    end
end

obj.extend MyModule_3
obj.print_my_lastname




