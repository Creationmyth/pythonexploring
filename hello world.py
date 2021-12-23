def sorting(words, amount):
    for x in words[0:]:
        for y in words[1:]:
            if x > y:
                words.append(x)
                words.remove(x)
            else:
                words.append(y)
                words.remove(y)
    return words

assortment = []
numbermade = 0
print("If you don't want anymore words, type \"nst\" to exit")
while 1 == 1:
    choice = str(input("What word would you like to put in?"))
    if choice != "nst":
        assortment.append(choice)
        numbermade = numbermade+1
    else:
        break

print(sorting(assortment, numbermade))