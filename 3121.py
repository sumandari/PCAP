blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
height = 0
need_stack = 0
used_block = 0
while blocks:
    need_stack = height + 1
    if blocks < need_stack:
        break
    height += 1
    used_block += need_stack
    blocks -= need_stack

print("The height of the pyramid:", height)
