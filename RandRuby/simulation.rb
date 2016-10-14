require 'market'
$producers = []
NUM_OF_PRODUCERS.times do
    producer = Producer.new
    producer.price = COST + rand(MAX_STARTING_PROFIT)
    producer.supply = rand(MAX_STARTING_SUPPLY)
    $producers << producer
end

$consumers = []
NUM_OF_CONSUMERS.times do
    $consumers << Consumer.new
end

$generate_demands = []
SIMILATION_DURATION.times {|n| $generate_demand << ((Math.sin(n)+2)*20).round}

