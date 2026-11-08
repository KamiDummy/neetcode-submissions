class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            print(score)
            if op == "C":
                score.pop()
                continue
            if op == "+":
                score.append(score[-1] + score[-2])
                continue
            if op == "D":
                score.append(2* score[-1])
                continue
            score.append(int(op))
            
        return sum(score)
            
                
            