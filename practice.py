def make_bricks(small, big, goal):
  if (small + big*5) < goal :
    return False
  else :
    if goal%5 > small :
      return False
    else :
      return True

def lone_sum(a, b, c):
  if a!=b and b!=c and c!=a :
    return a+b+c
  elif a==b :
    if b==c :
      return 0
    return c
  elif b==c :
    return a
  elif c==a :
    return b

  def lucky_sum(a, b, c):
  if a != 13 and b != 13 and c != 13 :
    return a+b+c
  elif a == 13 :
    return 0
  elif b == 13 :
    return a
  elif c == 13:
    return a+b

def no_teen_sum(a, b, c):
  def fix_teen(n) :
    if n>=13 and n<=19 :
      if n==15 or n==16 :
        return n
      else :
        return 0

  if (a<13 or a>19) and (b<13 or b>19) and (c<13 or c>19) :
    return a+b+c
  elif (a>=13 and a<=19) and (b<13 or b>19) and (c<13 or c>19) :
    return fix_teen(a)+b+c
  elif (a<13 or a>19) and (b>=13 and b<=19) and (c<13 or c>19) :
    return a+fix_teen(b)+c
  elif (a<13 or a>19) and (b<13 or b>19) and (c>=13 and c<=19) :
    return a+b+fix_teen(c)
  elif (a>=13 and a<=19) and (b>=13 and b<=19) and (c<13 or c>19) :
    return fix_teen(a)+fix_teen(b)+c
  elif (a<13 or a>19) and (b>=13 and b<=19) and (c>=13 and c<=19) :
    return a+fix_teen(b)+fix_teen(c)
  elif (a>=13 and a<=19) and (b<13 or b>19) and (c>=13 and c<=19) :
    return fix_teen(a)+b+fix_teen(c)
  else :
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num) :
    if num%10 >= 5 :
      num += (10-num%10)
      return num
    else :
      num -= num%10
      return num

def make_chocolate(small, big, goal):
  if (small + big*5) < goal :
    return -1
  else :
    if goal%5 > small :
      return -1
    elif goal-big*5 <= small and goal-big*5 > 0 :
      return goal-big*5
    else :
        return goal%5

def double_char(str):
  new_char=[]
  for char in str :
    new_char += char*2
  str1 = ''.join(new_char)
  return str1

def count_hi(str):
  count = 0
  for i in range(len(str)) :
    if str[i:i+2] == 'hi' :
      count += 1
  return count

def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range(len(str)-2) :
    if str[i:i+3] == 'cat' :
      cat_count += 1
    elif str[i:i+3] == 'dog' :
      dog_count += 1
  return dog_count == cat_count

def count_code(str):
  count = 0
  for i in range(len(str)-3) :
    if str[i:i+2] == 'co' and str[i+3] == 'e' :
      count += 1
  return count

def end_other(a, b):
  if len(a) >= len(b) :
    if a[len(a)-len(b):len(a)].lower() == b.lower() :
      return True
    else :
      return False
  else :
    if b[len(b)-len(a):len(b)].lower() == a.lower() :
      return True
    else :
      return False

def xyz_there(str):
  for i in range(len(str)-2) :
    if str[i:i+3] == 'xyz' :
      if str[i-1] != '.' :
        return True
  else :
    return False

def count_evens(nums):
  count = 0
  for i in nums :
    if i%2 == 0 :
      count += 1
  return count

def big_diff(nums):
  maxx = 0
  minn = 100
  if len(nums) <= 1 :
    return 0
  for i in range(len(nums)-1) :
    if maxx < max(nums[i], nums[i+1]) :
      maxx = max(nums[i], nums[i+1])
    if minn > min(nums[i], nums[i+1]) :
      minn = min(nums[i], nums[i+1])
  return maxx-minn

def centered_average(nums):
  nums.sort()
  sum = 0
  for i in nums[1:len(nums)-1] :
    sum += i
  return sum/(len(nums)-2)

def sum13(nums):
  count = 0
  if nums is [] :
    return 0
  for i in range(len(nums)) :
    if nums[i] == 13 :
      continue
    elif nums[i-1] == 13 and i > 0 :
        continue
    else :
      count += nums[i]
  return count

  def sum67(nums):
  sum = 0
  i = 0
  six = 0
  seven = 0
  first_six = True
  if nums.count(6) == 0 :
    for i in nums :
      sum += i
    return sum
  
  while i < len(nums) :
    if nums[i] == 6 and first_six :
      six = i
      first_six = False
    elif nums[i] == 7 and not first_six:
      seven = i
      first_six = True
    else :
      if (i>=six and not first_six) or i<=seven :
        continue
      else :
        sum += nums[i]
    i = i+1
  return sum
