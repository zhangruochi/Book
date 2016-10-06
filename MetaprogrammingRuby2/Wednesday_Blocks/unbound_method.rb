module MyModule
    def MyModule.my_method(name)
        puts "my name is #{name}"
    end
end

puts MyModule.methods.grep /^my/ #[:my_method]


module MyModule_2
    def my_method(name)
        puts "my name is #{name}"
    end
end

puts MyModule_2.methods.grep /^my/ #[]

unbound = MyModule_2.instance_method :my_method
puts unbound.class

#unbound 方法可以重新绑定在某个对象上成为一个 Method 对象
send :define_method,:print_name,unbound  #此时的对象是 main 对象
print_name :zhangruochi
