def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Can not divided by zero."
    except TypeError:
        return "Unsupported Type. Check your input please.."

print(div("10",2))
print(div(3,0))
print(div(9,3))