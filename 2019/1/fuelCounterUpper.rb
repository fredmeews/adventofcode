totalFuel = 0

File.foreach("inputs.txt") {
  |mass| mass.chomp
  iMass = Integer(mass)
  moduleFuel = (iMass / 3).round(half: :down) - 2
  totalFuel += moduleFuel
  puts "mas = #{iMass}, module = #{moduleFuel}"
}

puts "Total fuel = ", totalFuel
