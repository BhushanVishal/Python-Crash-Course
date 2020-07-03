##check if a list is order serially
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
if all(i < j for i, j in zip(input_list, input_list[1:])):
    print("yes")
else:
    print("no")
	
##sum integers in a number	
n=int(input())
if sum(map(int, str(n))) % 2:
    print("odd")
else:
    print("even")
	
##polling result for the list of values
##value that occur most than 50 percent win else NOTA
import ast,sys
input_str = sys.stdin.read()
votes = ast.literal_eval(input_str)
def dinner(votes):
    for i in set(votes):
        if votes.count(i)>len(votes)//2:
          return i
    return "NOTA"
print(dinner(votes))	