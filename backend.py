import random

def randomQue():

    num1 = random.randint(10, 200)
    num2 = random.randint(10, 200)
    num3 = random.randint(10, 200)
    sym1 = random.choice(["+", "*", "/", "-"])
    sym2 = random.choice(["+", "*", "/", "-"])

    if sym1 == "+":
        if sym2 == "+":
            que = f"{num1} + {num2} + {num3} ="
            anw = num1+num2+num3
        elif sym2 == "*":
            que = f"{num1} + {num2} x {num3} ="
            anw = num1+num2*num3
        elif sym2 == "/":
            que = f"{num1} + {num2} / {num3} ="
            anw = num1+num2/num3
        elif sym2 == "-":
            que = f"{num1} + {num2} - {num3} ="
            anw = num1+num2-num3
    elif sym1 == "*":
        if sym2 == "+":
            que = f"{num1} x {num2} + {num3} ="
            anw = num1*num2+num3
        elif sym2 == "*":
            que = f"{num1} x {num2} * {num3} ="
            anw = num1*num2*num3
        elif sym2 == "/":
            que = f"{num1} x {num2} / {num3} ="
            anw = num1*num2/num3
        elif sym2 == "-":
            que = f"{num1} x {num2} - {num3} ="
            anw = num1*num2-num3
    elif sym1 == "/":
        if sym2 == "+":
            que = f"{num1} / {num2} + {num3} ="
            anw = num1/num2+num3
        elif sym2 == "*":
            que = f"{num1} / {num2} x {num3} ="
            anw = num1/num2*num3
        elif sym2 == "/":
            que = f"{num1} / {num2} / {num3} ="
            anw = num1/num2/num3
        elif sym2 == "-":
            que = f"{num1} / {num2} - {num3} ="
            anw = num1/num2-num3
    elif sym1 == "-":
        if sym2 == "+":
            que = f"{num1} - {num2} + {num3} ="
            anw = num1-num2+num3
        elif sym2 == "*":
            que = f"{num1} - {num2} x {num3} ="
            anw = num1-num2*num3
        elif sym2 == "/":
            que = f"{num1} - {num2} / {num3} ="
            anw = num1-num2/num3
        elif sym2 == "-":
            que = f"{num1} - {num2} - {num3} ="
            anw = num1-num2-num3
    return {"que": que,"anw": round(anw, 2)}
