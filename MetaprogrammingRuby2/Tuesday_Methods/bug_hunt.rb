class Roulette
    def method_missing(name,*args)
        person = name.to_s.capitalize
        super unless %w[Ruochi Chenxi Sui Wangtao].include? person
        number = 0
        3.times do
            number = rand(10) + 1
        end
    "#{person}'s number is : #{number}"
    end
end

machine = Roulette.new
puts machine.Sui
puts machine.Ruochi
puts machine.Chenxi
puts machine.Wangtao
