class Opcode
  attr_reader :inputArr
  attr_reader :outputArr

  
  def initialize(inputArr)
    @location = 0
    @inputArr = inputArr
    @op
    @outputArr = Array.new(inputArr)
  end

  def process_next
    @op = outputArr[@location]
    arg1 = outputArr[@location+1]
    arg2 = outputArr[@location+2]
    resultLoc = outputArr[@location+3]

    if @op == 1
      outputArr[resultLoc] = outputArr[arg1] + outputArr[arg2]
    elsif @op == 2
      outputArr[resultLoc] = outputArr[arg1] * outputArr[arg2]
    elsif @op == 99
      nil
    else
      puts "unknown operation #{@op} - skipping"
    end
  end

  def process
    while @op != 99 do
#      puts "op = #{@op}"
      process_next()
      @location += 4          
    end
  end

end


