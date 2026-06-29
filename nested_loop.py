#nested loops =  a loop within another loop. The "inner loop" will be executed one time for each iteration of the "outer loop"

#                outer loop:
#                    inner loop:

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print() #print a new line after each row is printed

#Note: 
# normally print() adds a new line after the statement is printed, but we can change that with the "end" parameter

#So:
#end="\n" → next line (default)
#end="" → stay on same line
#end=" " → add space
#end="-" → add dash

#So yes, learning it as:

#outer = rows
#inner = columns

#is good initially.

#But the real understanding is:

#outer loop controls the big repetition
#inner loop controls the detailed repetition inside it.