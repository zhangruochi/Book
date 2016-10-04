# Computer 原始代码

class Computer
    def initialize(computer_id,data_source)
        @id = computer_id
        @data_source = data_source
    end

    def mouse
        info = @data_source.get_mouse_info(@id)
        price = @data_source.get_mouse_price(@id)
        result = "Mouse: #{info} ($#{price})"
        return "* #{result}" if price >= 100
        result
    end

    def cpu
        info = @data_source.get_cpu_info(@id)
        price = @data_source.get_cpu_price(@id)
        result = "cpu: #{info} ($#{price})"
        return "* #{result}" if price >= 100
        result
    end

    def keyboard
        info = @data_source.get_keyboard_info(@id)
        price = @data_source.get_keyboard_price(@id)
        result = "keyboard: #{info} ($#{price})"
        return "* #{result}" if price >= 100
        result
    end

end


#采用动态转发技术重构
class Computer_version2
    def initialize(computer_id,data_source)
        @id = computer_id
        @data_source = data_source
    end

    def component(name)
        info = @data_source.send "get_#{name}_info",@id
        price = @data_source.send "get_#{name}_price", @id
        result = "name.capitalize: #{info} ($#{price})"
        return "* #{result}" if price >= 100
        result
    end
    
    def mouse
        component :mouse
    end

    def cpu
        component :cpu
    end

    def keyboard 
        component :keyboard
    end
end


#使用 define_method 动态创建方法
class Computer_version3
    def initialize(computer_id,data_source)
        @computer_id = computer_id
        @data_source = data_source
    end

    def self.generate_method(name)   # 注意这里是类方法
        define_method(name) do 
            info = @data_source.send "get_#{name}_info",@id
            price = @data_source.send "get_#{name}_price", @id
            result = "name.capitalize: #{info} ($#{price})"
            return "* #{result}" if price >= 100
            result
        end
    end

    generate_method :mouse
    generate_method :cpu
    generate_method :keyboard
end


#使用内省的datasource 参数
class Compuer_version4
    def initialize(computer_id,data_source)
        @id = computer_id
        @data_source = data_source
        data_source.methods.grep(/^get_{.*}_info$/)
        { Computer.generate_method $1 }   #正则表达式的匹配结果会放在全局变量$1中
    end


    def self.generate_method(name)   # 注意这里是类方法
        define_method(name) do 
            info = @data_source.send "get_#{name}_info",@id
            price = @data_source.send "get_#{name}_price", @id
            result = "name.capitalize: #{info} ($#{price})"
            return "* #{result}" if price >= 100
            result
        end
    end
end
        










