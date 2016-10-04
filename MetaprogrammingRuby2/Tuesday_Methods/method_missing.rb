#当某个对象通过祖先链找不到某个方法时，会调用 method_missing 方法

class Test
    def method_missing(name,*args)
        puts "You called #{name}(#{args.join(", ")})"
        puts "You also passed it a block " if block_given?
    end
end


a = Test.new
a.fuck("li") do
end

=begin
output:
You called fuck(li)
You also passed it a block 
=end

