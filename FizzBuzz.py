def fizz_buzz(num):
    res = []
    for nums in range(1, num + 1):
        if nums % 15 == 0:
            res.append("FizzBuzz")
        elif nums % 3 == 0:
            res.append("Fizz")
        elif nums % 5 == 0:
            res.append("Buzz")
        else:
            res.append(nums)
        print(res)

fizz_buzz(15)
fizz_buzz(5)