def uniquekey1():
    input1 = int(input())
    input2 = int(input())
    input3 = int(input())
    inputs = [input1, input2, input3]
    sdth = []
    result = []

    for ele in inputs:
        sdth.append(ele//1000)

    result.append(sorted(sdth)[0])
    sdth.clear()

    for ele in inputs:
        ele //= 100
        sdth.append(ele%10)

    result.append(sorted(sdth)[-1])
    sdth.clear()

    for ele in inputs:
        ele //= 10
        sdth.append(ele%10)

    result.append(sorted(sdth)[0])
    sdth.clear()

    for ele in inputs:
        sdth.append(ele%10)

    result.append(sorted(sdth)[-1])
    sdth.clear()

    for ans in result:
        print(ans, end="")
uniquekey1()