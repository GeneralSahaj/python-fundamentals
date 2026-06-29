# format specifier = {value:flags} format a value based on the flags provided
# flags = < (left align), > (right align), ^ (center align),
#         + (show sign), - (show minus sign only), 0 (zero padding)
#         , (thousands separator), . (precision)

# example

num1 = 1234.56789
num2 = -1234.56789
num3 = 1234567890

print(f"num1: {num1:+,.2f}")  # 1,234.57
print(f"num2: {num2:+,.2f}")  # -1,234.57
print(f"num3: {num3:+,}")      # 1,234,567,890

# above code's section {num1:+,.2f} means:
# + : show sign (positive or negative)
# , : use thousands separator  (thousands separator is useful for large numbers to improve readability by separating groups of three digits)
# .2f : format as fixed-point number with 2 decimal places