=begin  #模块的使用

module MyModule
    PI = 3.14
    
    def MyModule.print_name
        puts "zhangruochi!"
    end

end

puts MyModule::PI
MyModule.print_name
=end


#在一组方法中共享一个变量


class DefineMethods
    shared = 0

    define_method :counter do
        shared
    end

    send :define_method, :inc do |increment|
        shared += increment
    end
end


a = DefineMethods.new
puts a.counter
puts a.inc 10
puts a.counter





def define_methods
    shared = 0
    Kernel.send :define_method, :counter do  #利用 send 方法调用 kernel 的私有方法 define_methods   为 kernel 生成新的函数
        shared
    end

    Kernel.send :define_method, :inc do |increment|
        shared += increment
    end
 end

define_methods

puts counter
puts inc 10
puts counter





