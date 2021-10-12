from arrayStackty import ArrayStack

#using a stack to reverse a string
def stack_reverse_string(str):
    stack = ArrayStack()

    for i in range(len(str)):
        stack.push(str[i])
    result = ""
    for i in range(len(str)):
        result += stack.pop()

    return result

def main():
    str1 = "ABCDE" #output EDCBA 
    print(stack_reverse_string(str1))

main()


