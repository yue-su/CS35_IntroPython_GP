

def count_sheep(n):
    # your code
    result = []
    for i in range(n):
        result.append(f"{i+1} sheep...")
    return "".join(result)

# print(count_sheep(3))


def reverseSentence(sentence):
    new = sentence.split()
    new.reverse()
    return " ".join(new)


# print(reverseSentence("Man bites dog"))

def digitSumsDifference(n):
    producttion = 1
    summation = 0
    numbers = str(n)
    number_list = [number for number in numbers]
    for i in range(len(number_list)):
       producttion = producttion * int(number_list[i])
       summation += int(number_list)
    return producttion - summation

# print(digitSumsDifference(246))