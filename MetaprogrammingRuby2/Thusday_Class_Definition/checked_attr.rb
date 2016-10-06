def add_checked_attribute(kclass,attribute)
    eval "
        class #{kclass}
            def #{attribute}= (value)
                rasie 'Invalid attribute' unless value
                @#{attribute} = value
            end

            def #{attribute}
                @#{attribute}
            end
        end
    "
end


add_checked_attribute(String, :my_attr)
a = String.new "zhangruochi"
puts a
a.my_attr = "name"
puts a.my_attr

#重构 add_checked_attribute方法  去掉 eval
def add_checked_attribute_2(kclass,attribute)
    
        kclass.class_eval do 
            define_method "#{attribute}=" do |value|
                rasie 'Invalid attribute' unless value
                instance_variable_set("@#{attribute}", value)
            end

            define_method "#{attribute}" do
                instance_variable_get "@#{attribute}"
            end
        end
end


add_checked_attribute_2(String,:my_attr_2)
b = String.new "hongchabiao"
b.my_attr_2 = "her name"
puts b.my_attr_2



# 重构  通过代码块来效验属性
def add_checked_attribute_3(kclass,attribute,&block)
    
        kclass.class_eval do 
            define_method "#{attribute}=" do |value|
                rasie 'Invalid attribute' unless block.call(value)
                instance_variable_set("@#{attribute}", value)
            end

            define_method "#{attribute}" do
                instance_variable_get "@#{attribute}"
            end
        end
end

add_checked_attribute_3(String,:age) {|value| value > 18}
c = String.new "zhang"
c.age = 22
puts c.age


#将内核方法改造成为一个类宏
class Class
    def attr_checked(attribute,&block)
        define_method "#{attribute}=" do |value|
                rasie 'Invalid attribute' unless block.call(value)
                instance_variable_set("@#{attribute}", value)
            end
        define_method "#{attribute}" do
            instance_variable_get "@#{attribute}"
            end
    end
end



class Person
    attr_checked(:virtual_age) {|value| value > 18}
end

obj = Person.new
obj.virtual_age = 22
puts obj.virtual_age 


#限制类宏 十七只对哪些包含 CheckedAttributes 模块的类可用
module CheckedAttributes
    def self.included(base)
        base.enxtend ClassMethods
    end

    module ClassMethods
        def attr_checked(attribute,&block)
            define_method "#{attribute}=" do |value|
                    rasie 'Invalid attribute' unless block.call(value)
                    instance_variable_set("@#{attribute}", value)
                end
            define_method "#{attribute}" do
                instance_variable_get "@#{attribute}"
                end
        end
    end
end

class MyModuleClass
    included CheckedAttributes
    attr_checked(:virtual_age) {|value| value > 18}
end

obj_2 = MyModuleClass.new
obj.virtual_age = 22
puts obj.virtual_age 







