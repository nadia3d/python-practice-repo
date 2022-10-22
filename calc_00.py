# hi! here is my calculator homework.

errorMessage_0 = 'error: division by zero is not supported'
errorMessage_1 = 'error: operator not supported'
errorMessage_2 = 'error: value not supported, please only use decimal numbers'

def isFloat(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def calcAdd(var_a, var_b):
    return round(float(var_a) + float(var_b) , 3)


def calcSub(var_a, var_b):
    return round(float(var_a) - float(var_b) , 3)


def calcMult(var_a, var_b):
    return round(float(var_a) * float(var_b) , 3)


def calcDiv(var_a, var_b):
    if float(var_b) != 0:
        return round(float(var_a) / float(var_b) , 3)
    else:
        return errorMessage_0

def calcMod(var_a,var_b):
    return float(var_a) % float(var_b)

def myCalc(var_a, var_b, op):
    var_a = input('enter the first number ')
    # opTuple = ('+','-','*','/')
    var_b = input('enter the second number ')
    op = input('enter the math operator ')

    if isFloat(var_a) and isFloat(var_b):

        if op == '+':
            return calcAdd(var_a, var_b)            
        elif op == '-':
            return calcSub(var_a, var_b)
        elif op == '*':
            return calcMult(var_a, var_b)
        elif op == '/':
            return calcDiv(var_a, var_b)
        elif op == '%':
            return calcMod(var_a, var_b)
        else:
            return errorMessage_1

    # elif op not in opTuple and not (isFloat(a) and isFloat(b)):
    #         return errorMessage_1 , errorMessage_2     

    else:
        return errorMessage_2


        
# import keyboard
print('welcome to my calculator. precss Ctrl+C to exit.')

while True:
    print(myCalc(True,True,True)) 
    # if keyboard.is_pressed("esc"):
    #     print('bye')
    #             # Key was pressed
    #     break

