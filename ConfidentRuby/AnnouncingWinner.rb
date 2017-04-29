winners = ["zhang","li","wang","liu"]

Place = Struct.new(:index,:name,:prize) do 
    def to_int
        index
    end
end

first = Place.new(0,"first","100 RMB")
second = Place.new(1,"second","50 RMB")
third = Place.new(2,"third","100 RMB")

[first,second,third].each do |place|
    print "In #{place.name} place, #{winners[place]}, "
    puts "you win: #{place.prize}"
end
