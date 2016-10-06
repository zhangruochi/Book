setup do
    puts "Setting up sky"
    @sky_height = 100
end

setup do
    puts "Setting up mountains"
    @mountains_height = 200
end

event "The sky is failling" do
    @sky_height < 300
end

event "It's getting closer" do
    @sky_height < @mountains_height
end

event "whoops... too late" do
    @sky_height < 0 
end

