#钩子方法

#inhreited 是 Class 的一个实例方法  默认情况下什么也不做
class String
    def self.inherited subclass
        puts "I am inherited now"
    end
end

class MyClass < String
end
#I am inherited now

     