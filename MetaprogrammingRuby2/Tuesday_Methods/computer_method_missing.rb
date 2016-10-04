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

#采用 method_missing 方法再次重构 Computer 代码
class Computer
    def initialize(computer_id,data_source)
        @id = computer_id
        @data_source = data_source
    end

    def method_missing(name)
        #检测name 是否是 datasource 封装的对象方法 如果不是 则转发给上层的BasicObject#method_missing方法 抛出异常
        super if @data_source.respond_to? "get_#{name}_info"
        info = @data_source.get_mouse_info(@id)
        price = @data_source.get_mouse_price(@id)
        result = "Mouse: #{info} ($#{price})"
        return "* #{result}" if price >= 100
        result
    end

    #为了让 object.respond? method 显示正常  每次覆写 method_missing 方法时都需要覆写  respond_to_missing方法
    def respond_to_missing? (method,include_private = false)
        @data_source.respond_to? "get_#{method}_info" || super
end







