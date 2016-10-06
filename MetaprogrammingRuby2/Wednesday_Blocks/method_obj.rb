#将方法转化为 Method 对象
class MyClass
    def initialize(value)
        @x = value
    end
    def my_method
        @x
    end
end

obj = MyClass.new(1)
m = obj.method :my_method
puts m.call
