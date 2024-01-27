# Create a method called testPrim() in the Calculation class to test the primality of a given integer.
# Test this method.

class Calculation():

    def __init__(self) -> None:
        pass

    def testPrim(self, num1, num2):
        nums_inBetween = []

        if num1 > num2:
            while num1 > num2:
                num1 -= 1
                nums_inBetween.append(num1)
                
            nums_inBetween.sort()
            nums_inBetween.remove(0)
        elif num2 > num1:
            while num2 > num1:
                num2 -= 1
                nums_inBetween.append(num2)
                
            nums_inBetween.sort()
            nums_inBetween.remove(0)
        else:
            return "Please enter two different numbers"
        
        prime_nums = []
        not_prime_nums = []

        for num in nums_inBetween:
            if num == 1:
                not_prime_nums.append(num)
            elif num == 2:
                prime_nums.append(num)
            elif num > 1:
                for i in range (2, num):
                    if (num % i) == 0:
                        if num in not_prime_nums:
                            continue
                        else:
                            not_prime_nums.append(num)
                    else:
                        if num in prime_nums:
                            continue
                        else:
                            prime_nums.append(num)
        
        for not_prime_num in not_prime_nums:
            if not_prime_num in prime_nums:
                prime_nums.remove(not_prime_num)

        return f"Prime numbers: {prime_nums}\nNot prime numbers: {not_prime_nums}"
        


calculation_instance = Calculation()

print(calculation_instance.testPrim(100, 0))