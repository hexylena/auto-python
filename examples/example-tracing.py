# Initialise our accumulator
x = 1 + 1
# Loop over our input data
for i in range(10): # 0..9
    # In-loop temporary variable
    tmp = x * 2 + i
    # Update our accumulator
    x = tmp + 1
# Output our result
print(f'The final value is {x}')
