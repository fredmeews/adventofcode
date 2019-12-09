require "minitest/autorun"
require_relative "password"


class PasswordTest < MiniTest::Test
  def setup
    @password = Password.new()
  end

  def test_check_v1
    assert @password.check_v1("111111")    
    refute @password.check_v1("223450")
    refute @password.check_v1("123789")
  end

  def test_check_v2
    assert @password.check_v2("112233")    
    refute @password.check_v2("123444")
    assert @password.check_v2("111122")
  end
  

  def test_check_range
    assert_equal ["111111"], @password.check_range("111110", "111111", "check_v1")
  end

  def test_puzzle_part_one
    num_passwords = @password.check_range("235741", "706948", "check_v1").size
    assert_equal 1178, num_passwords
  end

  def test_puzzle_part_two
    num_passwords = @password.check_range("235741", "706948", "check_v2").size
    assert_equal 763, num_passwords
  end
  
end

