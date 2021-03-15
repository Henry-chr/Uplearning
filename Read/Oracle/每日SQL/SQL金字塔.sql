select lpad(' ', 9 - level , ' ') || lpad(level, 2 * level - 1, level) 
  from dual 
connect by level <= 9
