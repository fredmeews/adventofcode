require "minitest/autorun"
require_relative "opcode"

class OpcodeTest < MiniTest::Test
  def setup
  end

  def test_initialize
    @opcode = Opcode.new([1,1,2,3])
    
    assert @opcode.inputArr.length > 0
    assert_equal 1, @opcode.inputArr[0]
  end

  def test_opcode_add
    @opcode = Opcode.new([1,0,0,0,99])
    @opcode.process_next()
    
    assert_equal [2,0,0,0,99], @opcode.outputArr
  end

  def test_opcode_mult
    @opcode = Opcode.new([2,3,0,3,99])
    @opcode.process_next()
    
    assert_equal [2,3,0,6,99], @opcode.outputArr
  end

  def test_process
    @opcode = Opcode.new([1,1,1,4,99,5,6,0,99])
    @opcode.process()
    
    assert_equal [30,1,1,4,2,5,6,0,99], @opcode.outputArr
  end

  def test_puzzle_part_one
    file = File.open("inputs.txt")
    @input = file.readlines(",").map(&:chop).map{ |string| string.to_i }
    @input[1] = 12
    @input[2] = 2
    
    @opcode = Opcode.new(@input)
    @opcode.process()
    
    assert_equal 4138687, @opcode.outputArr[0]
  end

  def test_puzzle_part_two

    file = File.open("inputs.txt")
    @input = file.readlines(",").map(&:chop).map{ |string| string.to_i }
    
    for noun in (99).downto(0) do
      for verb in 0..99 do

#        puts "1: #{@input.inspect}"
        
        @input[1] = noun
        @input[2] = verb
        @opcode = Opcode.new(@input)        
#        puts "2: #{@input.inspect}"

        @opcode.process()
        puts @opcode.outputArr[0]        
        if @opcode.outputArr[0] == 19690720
          solution = 100 * noun + verb
          puts "solution = #{solution}"
          exit(0)
        end
      end #verb 
    end # noun
    
  end
end
