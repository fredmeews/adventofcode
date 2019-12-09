require "set"

class Wire
  attr_reader :pos
  attr_reader :path
  attr_reader :total_steps
  attr_reader :pos_steps
  
  X = 0
  Y = 1
  
  def initialize
    @pos = [0,0]
    @pos_steps = Hash.new(0) # Steps to get to pos
    @total_steps = 0
    @path = Set["0,0"]  # set of coordinates making up path
  end

  def process(directions)
    for i in 0 ... directions.size
      cmd = directions[i]
      direction = cmd[0]
      steps = cmd[1,cmd.length].to_i

      method(direction).call(steps)
    end
  end

  def U(steps)
    pos2 = @pos[Y]+steps
    
    for step in @pos[Y]+1..pos2
      position = "#{@pos[X]},#{step}"
      @total_steps = @total_steps + 1
      @path.add(position)
      @pos_steps[position] = @total_steps
    end

    @pos[Y] += steps
  end

  def D(steps)
    pos2 = @pos[Y]-steps
    for step in (@pos[Y]-1).downto(pos2)
      position = "#{@pos[X]},#{step}"
      @total_steps = @total_steps + 1
      @path.add(position)
      @pos_steps[position] = @total_steps
    end

    @pos[Y] -= steps      
  end

  def R(steps)
    pos2 = @pos[X]+steps
    for step in @pos[X]+1..pos2
      position = "#{step},#{@pos[Y]}"
      @total_steps = @total_steps + 1
      @path.add(position)
      @pos_steps[position] = @total_steps
    end

    @pos[X] += steps
  end    

  def L(steps)
    pos2 = @pos[X]-steps
    for step in (@pos[X]-1).downto(pos2)
      position = "#{step},#{@pos[Y]}"
      @total_steps = @total_steps + 1
      @path.add(position)
      @pos_steps[position] = @total_steps
    end

    @pos[X] -= steps
  end

  def intersect_closest_to_origin(wire2)
    closest = -1
    
    for sloc in @path
      loc = sloc.split(",")
      if (wire2.path.include? sloc) && (sloc != "0,0")
        distance = loc[X].to_i.abs + loc[Y].to_i.abs
        closest = distance if (closest < 0) || (distance < closest)
      end
    end

    return closest
  end  

  # Return least steps that *both wires* took to get to intersection
  def intresect_least_steps(wire2)
    least_steps = -1
    
    for sloc in @path
      loc = sloc.split(",")
      if (wire2.path.include? sloc) && (sloc != "0,0")
        steps = @pos_steps[sloc] + wire2.pos_steps[sloc]
        least_steps = steps if (least_steps < 0) || (steps < least_steps)
      end
    end
    return least_steps
  end
  
end
