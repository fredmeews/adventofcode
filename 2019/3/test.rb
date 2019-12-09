require "minitest/autorun"
require_relative "wire"


class WiresTest < MiniTest::Test
  def setup
    @wire = Wire.new()
  end

  def test_init
    assert_equal [0,0], @wire.pos
  end
  
  def test_up
    @wire.method('U').call(3)
    assert_equal [0,3], @wire.pos
    assert_equal Set["0,0", "0,1", "0,2", "0,3"], @wire.path
  end

  def test_down
    @wire.method('D').call(3)
    assert_equal [0,-3], @wire.pos
    assert_equal Set["0,0", "0,-1", "0,-2", "0,-3"], @wire.path    
  end

  def test_right
    @wire.method('R').call(3)
    assert_equal [3,0], @wire.pos
    assert_equal Set["0,0", "1,0", "2,0", "3,0"], @wire.path
  end

  def test_left
    @wire.method('L').call(3)
    assert_equal [-3,0], @wire.pos
    assert_equal Set["0,0", "-1,0", "-2,0", "-3,0"], @wire.path
  end

  def test_process
    @wire.process(["U5","R5","D5","L5"])
    assert_equal [0,0], @wire.pos
  end

  def test_closest_intersect
    @wire2 = Wire.new()
    
    @wire.process(["R75","D30","R83","U83","L12","D49","R71","U7","L72"])
    @wire2.process(["U62","R66","U55","R34","D71","R55","D58","R83"])
    
    assert_equal 159, @wire.intersect_closest_to_origin(@wire2)
  end

  def test_intresect_least_steps
    @wire2 = Wire.new()
    
    @wire.process(["R75","D30","R83","U83","L12","D49","R71","U7","L72"])
    @wire2.process(["U62","R66","U55","R34","D71","R55","D58","R83"])
    
    assert_equal 610, @wire.intresect_least_steps(@wire2)
  end
  
  
  def test_puzzle_part_one
    @wire2 = Wire.new()    

    file = File.open("inputs.txt")    
    wire1 = file.readline.split(",").map(&:chomp)
    wire2 = file.readline.split(",").map(&:chomp)

    @wire.process(wire1)
    @wire2.process(wire2)

    assert_equal 806, @wire.intersect_closest_to_origin(@wire2)    
  end  

  def test_puzzle_part_two
    @wire2 = Wire.new()    

    file = File.open("inputs.txt")    
    wire1 = file.readline.split(",").map(&:chomp)
    wire2 = file.readline.split(",").map(&:chomp)

    @wire.process(wire1)
    @wire2.process(wire2)

    assert_equal 66076, @wire.intresect_least_steps(@wire2)    
  end  
  
end
