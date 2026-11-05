import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # 1. Pehle arr2 ko sort kar lo taaki binary search laga sakein
        arr2.sort()
        distance_value = 0
        
        # 2. arr1 ke har ek number par loop chalayenge
        for val in arr1:
            # bisect_left se hum arr2 mein (val - d) ki sahi jagah (index) dhundte hain
            idx = bisect.bisect_left(arr2, val - d)
            
            # Agar idx array ke andar hai AUR wo element (val + d) se chota ya barabar hai,
            # toh hume invalid element mil gaya. Isko skip karenge.
            if idx < len(arr2) and arr2[idx] <= val + d:
                continue  
                
            # Agar range mein koi element nahi mila, toh yeh valid hai. Count badhao.
            distance_value += 1
                
        return distance_value
