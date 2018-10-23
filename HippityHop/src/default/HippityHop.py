def hippityHop(a_list):
  jump = a_list[0]
  i = 1
  jump_distance = 0
  while jump > 0:
    jump_distance = a_list[jump]
    jump = jump_distance + jump
    jump = jump % len(a_list)
    i += 1
  return i
list_a = [2,2,-1,1]
print(hippityHop(list_a))
list_a = [2,1,-2,1,4,-4]
print(hippityHop(list_a))
    