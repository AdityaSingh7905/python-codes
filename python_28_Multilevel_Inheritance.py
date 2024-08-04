class Dad:
    basketball=1

class Son(Dad):
    dance=1
    basketball=6
    def isdance(self):
        return f"I am a good dancer as i danced {self.dance} times."
class Grandson(Son):
    dance=6
    guitar=1
    # def isdance(self):
    #     return f"I am a better dancer {self.dance} times and I am trying to learn more moves.."
# Here O refers to overwriting and after overwriting value of the variable or method changes...
darry=Dad()
larry=Son()
harry=Grandson()
print(Grandson.basketball)
print(harry.isdance())
print(larry.basketball)