class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            ans = ""
            if i%3 == 0:
                ans += "Fizz"
            if i%5 == 0:
                ans +="Buzz"
            if ans == "":
                ans += str(i)
            result.append(ans)    
    
        return result

        