class Producer
    attr_accessor :supply,:price
    def initialize
        @supply = 0
        @price = 0
    end

    def generate_goods
        @supply += SUPPLY_INCREMENT if @price > COST
    end

    def produce
        if @supply > 0
            @price *= PRICE_DECREMENT unless @price < COST
        else
            @price *= PRICE_INCREMENT 
            generate_goods
        end
    end
end

class Consumer
    attr_accessor :demands
    def initial
        @demands = 0 
    end

    def buy
        until @demands <=0 or Market.supply <= 0
            cheapest_producer = Market.cheapest_producer
            if cheapest_producer
                @demands *= 0.5 if @demands > cheapest_producer.price

                if demands > cheapest_producer.supply
                    @demands -= cheapest_producer.supply
                    cheapest_producer.supply = 0 
                else
                    cheapest_producer.supply -= @demands 
                    @demands = 0
                end
            end
        end
    end
end


class Market
    def self.average_price
        ($producers.inject(0.0) {|memo,produce| memo += produce.price} / producers.size).round 2
    end

    def self.supply
        $producers.inject(o.o) {|memo,produce| memo += produce.supply}
    end

    def self.demands
        $consumers.inject(0.0) {|memo,consumer| memo += consumer.demands}
    end

    def self.cheapest_producer
        producers = $producers.find_all {|produce| produce.supply > 0}
        producers.min_by {|produce| produce.price}
    end
end







