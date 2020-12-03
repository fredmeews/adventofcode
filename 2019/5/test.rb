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

  def test_opcode_store
    @opcode = Opcode.new([3,3,0,0,99])
    @opcode.argv = [47]  # input to store
    
    @opcode.process_next()
    assert_equal [3,3,0,47,99], @opcode.outputArr
  end
  

end
