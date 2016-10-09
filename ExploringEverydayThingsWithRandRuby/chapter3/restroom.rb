class Restroom
    attr_reader :queue
    attr_reader :facilities
    
    def initialize(facilities_per_room)
        @queue = []
        @facilities = []
        facilities_per_room.times do 
            facilities << Facility.new
        end
    end

    def enter(person)
        unoccupied_facility = facilities.find { |facility| not facility.occupied? }

        if unoccupied_facility
            unoccupied_facility.occupy person
        else
            @queue << person
        end
    end

    def tick
        @facilities.each {|facility| facility.tick}
    end
end



class Facility
    def initialize
        @occupier = nil
        @duration = 0
    end

    def occupy(person)
        unless occupied?
            @occupier = person
            @duration = 1
            Person.population.delete person
            true
        else
            false    
        end
    end

    def occupied?
        not @occupier.nil?
    end

    def vacate
        Person.population << @occupier
        @occupier = nil
    end

    def tick
        if occupied? and @duration > @occupier.use_duration 
            vacate
            @duration = 0
        elsif occupied?
            @duration += 1
        end
    end
end


class Person
    @@population = []
    attr_reader :use_duration
    attr_reader :frequency

    def initialize(frequency,use_duration)
        @frequency = frequency
        @use_duration = use_duration
    end

    def self.population
        @@population
    end

    def need_to_go?
        rand(540) + 1 < @frequency
    end
end






