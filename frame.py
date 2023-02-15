import random
class Frame:

    def __init__(self, round):
        self.first = random.randint(0,10)
        if self.first == 10:
            self.next = "strike"
            self.score = self.first
            self.desc = "X"
        else:
            self.second = random.randint(self.first+1,10)
            if self.second == 10:
                self.next = "spare"
                self.score = self.second
                self.desc = f"{self.first} /"
            else:
                self.score = self.second
                self.next = "none"
                self.desc = f"{self.first} {self.second - self.first}"
        self.round = round
        if int(round) == 10:
            if self.next != "none":
                self.third = random.randint(0,10)
                self.score += self.third
                if self.third == 10 and self.next == 'strike':
                    self.fourth = random.randint(0,10)
                    self.score += self.fourth
                    self.desc += f" X {self.fourth}" if self.fourth != 10 else f" X X"
                else:
                    self.desc += f" {self.third}"


    def __str__(self):
        return self.desc
        

