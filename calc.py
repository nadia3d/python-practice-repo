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


def calcAdd(a, b):
    return round(float(a) + float(b) , 3)


def calcSub(a, b):
    return round(float(a) - float(b) , 3)


def calcMult(a, b):
    return round(float(a) * float(b) , 3)


def calcDiv(a, b):
    if float(b) != 0:
        return round(float(a) / float(b) , 3)
    else:
        return errorMessage_0


def myCalc(a, op, b):
    a = input('enter the first number ')
    op = input('enter the operator ')
    # opTuple = ('+','-','*','/')
    b = input('enter the second number ')

    if isFloat(a) and isFloat(b):

        if op == '+':
            return calcAdd(a, b)            
        elif op == '-':
            return calcSub(a, b)
        elif op == '*':
            return calcMult(a, b)
        elif op == '/':
            return calcDiv(a, b)
        else:
            return errorMessage_1

    # elif op not in opTuple and not (isFloat(a) and isFloat(b)):
    #         return errorMessage_1 , errorMessage_2     

    else:
        return errorMessage_2
        
import keyboard
while True:
    print(myCalc(True, True, True)) 
    if keyboard.is_pressed("esc"):
        print('bye')
        # Key was pressed
        break
