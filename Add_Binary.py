class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a,2)
        d=int(b,2)
        e=c+d
        n=f"{e:b}"
        return n
