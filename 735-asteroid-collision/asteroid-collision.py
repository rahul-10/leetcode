class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res: List[int] = [asteroids[0]]
        for i in range(1, len(asteroids)):
            to_be_uopdated = True
            while res and asteroids[i] < 0 and res[len(res) -1] > 0:
                if -1*asteroids[i] > res[len(res) -1]:
                    res.pop()
                elif -1*asteroids[i] == res[len(res) -1]:
                    res.pop()
                    to_be_uopdated = False
                    break
                else:
                    to_be_uopdated = False
                    break
            
            if to_be_uopdated:   
                res.append(asteroids[i])
        return res
            
