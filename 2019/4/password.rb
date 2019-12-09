require "set"

class Password
  def initialize
  end

  def check_v1(passwd)
    is_duplicate = false
    is_increasing = true
    repeat = 0

    # Duplicate digit check
    digit = passwd.each_char.map(&:to_i)
    for i in 1..(digit.length-1)
      is_increasing = false if (digit[i] < digit[i-1])
      is_duplicate = true if (digit[i] == digit[i-1])
    end

    return (is_increasing && is_duplicate)
  end

  def check_v2(passwd)
    is_duplicate = false
    is_increasing = true
    repeat = 0

    # Duplicate digit check
    digit = passwd.each_char.map(&:to_i)
    for i in 1..(digit.length-1)
      is_increasing = false if (digit[i] < digit[i-1])

      if (digit[i] == digit[i-1])
        repeat = repeat + 1
      elsif (repeat == 1)  # only repeats once
        is_duplicate = true
      else
        repeat = 0
      end
    end

    is_duplicate = true if (repeat == 1)

    return (is_increasing && is_duplicate)
  end
  

  def check_range(from, to, check_method)
    solution = Array.new(0)
    for passwd in from..to
      if method(check_method).call(passwd)
        solution.push(passwd)
      end
    end

    return solution
  end
  
end
