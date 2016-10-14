class Restroom
    attr_accessor :queue
    attr_accessor :facilities

    def initialize(facilities_per_restrooom = 3)
        @queue = []
        @facilities = []
        facilities_per_restrooom.times { facilities << Facility.new }
    end
        
    def enter(person)
        unoccupied_facility = @facilities.find( |facility| not facility.occupied? )
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
    def initial
        @occupier = nil
        @duration = 1
    end

    def occupy(person)
        unless occupied?
            @occupied = person
            @duration = 1  #存储当前使用者使用了多长的时间
            Person.population.delete person
            true
        else
            false
        end
    end

    def occupied?
        not @occupied.nil?
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

def Person
    @@population = []
    attr_reader :use_duration 
    attr_accessor : frequency

    def initialize(frequency = 4, use_duration = 1)
        @use_duration = use_duration
        @frequency = frequency
    end
    
    def self.population
        @@population
    end
    
    def need_to_go?
        rand(DURATION) + 1 > @frequency 
    end            
end    



