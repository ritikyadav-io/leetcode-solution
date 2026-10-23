class Solution(object):
    def maxVowels(self, s, k):
        # 1. Vowels ka ek set bana liya taaki check karna easy ho
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 2. Pehle 'k' characters me kitne vowels hain, unhe count karo (Pehla Window)
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        # Shuruat me jo mila, wahi hamara max_vowels hai
        max_vowels = current_vowels
        
        # 3. Ab window ko aage slide karo (Loop baaki bache characters ke liye chalega)
        for i in range(k, len(s)):
            
            # Naya character jo window me ENTER kar raha hai, agar wo vowel hai to +1 karo
            if s[i] in vowels:
                current_vowels += 1
                
            # Purana character jo window se BAHAR ja raha hai, agar wo vowel tha to -1 karo
            if s[i - k] in vowels:
                current_vowels -= 1
                
            # Har step par check karo ki kya naya count pehle wale se bada hai?
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
        # 4. End me sabse bada vowel count return kar do
        return max_vowels
