def isFloat(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def isZero(element: any):
    if float(element) == 0:
        return True
    else:
        return False

def myCalc(var_a,var_b,op):
    
    if op == '+':
        return float(var_a) + float(var_b)
    elif op == '-':
        return float(var_a) - float(var_b)
    elif op == '*':
        return float(var_a) * float(var_b)
    elif op == '/':
        return float(var_a) / float(var_b)
    elif op == '%':
        return float(var_a) % float(var_b)

print('welcome to this calculator, press ctrl+C to exit')

while True:
   
    var_a = input('enter the first number ')
    var_b = input('enter the second number ')
    op = input('enter a math operator ')
    opList = ('+','-','*','/','%')


    if not isFloat(var_a) or not isFloat(var_b):
        print('variable not supported, please only use decimal numbers')
    elif op not in opList:
            print('this operator is not supported')
    elif isZero(var_b):
        print('division by zero is not supported')
    else:
        result = round(myCalc(var_a,var_b,op),3)
        print(result)
