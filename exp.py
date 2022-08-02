def check(code):
    if code[0] == "T" and code[1] == "H" and len(code) == 5:
        return code
    else:
        return "no"

while 1 == 1:
    code = input()
    correct = check(code)
    if correct != "no":
        print(correct)