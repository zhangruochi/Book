class Book
    def initialize(title,subtitle)
        @title = title
        @subtitle = subtitle
    end

    def title
        @title
    end

    def subtitle
        @subtitle
    end

    def lend_to(user)
        puts "Lending book to #{user}"
    end

    def self.change_method_name(old_name,new_name)
        define_method old_name do |*args,&block|
            warn "Warning: #{old_name}() is changed, the new name is #{new_name}()"
            send new_name,*args,&block
        end
    end

    change_method_name :GetTitle, :title
    change_method_name :LEND_TO_USER, :lend_to
    change_method_name :title2, :subtitle
end


a = Book.new("zhang","ruochi")
puts a.GetTitle
puts a.title


