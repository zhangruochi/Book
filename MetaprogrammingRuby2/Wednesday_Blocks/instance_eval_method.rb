#instance_eval 在对象的上下文中执行块 此时的对象是 self  可以使用对象的私有方法和实例变量

class Myclass
    def initialize
        @v = "zhang"
    end
end

my_variable = "ruochi"
obj = Myclass.new
obj.instance_eval do 
    puts self
    puts "my name is #{@v}#{my_variable}"
end


#instance_exec  和 instance_eval 作用基本相同 但是前者可以传递参数
class C
    def initialize
        @y = 2
    end
end



class D
    def d_method
        @x = 1
        C.new.instance_exec(@x) {|x| puts "@y: #{@y}, @x: #{x}"}
        #@x 必须通过参数传递 因为实例变量依赖于当前的 self  此时的 self 是 C 的对象  故 D 的实例变量不许通过参数传递
        
    end
end

D.new.d_method
