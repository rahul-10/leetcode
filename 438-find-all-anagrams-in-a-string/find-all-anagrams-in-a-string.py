class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_freq = {}
        p_count = len(p)
        for element in p:
            p_freq[element] = p_freq.get(element, 0) + 1
        

        starting_index = 0
        current_freq = {}
        start_index = []
        for index in range(0, len(s)):
            if s[index] not in p_freq: 
                while(s[starting_index] != s[index]):
                    current_freq[s[starting_index]] = current_freq.get(s[starting_index], 0)-1
                    starting_index += 1
                starting_index += 1
            elif current_freq.get(s[index], 0) >= p_freq.get(s[index], 0):
                while( current_freq.get(s[index], 0) >= p_freq.get(s[index], 0)):
                    current_freq[s[starting_index]] = current_freq.get(s[starting_index], 0)-1
                    starting_index += 1
                current_freq[s[index]] = current_freq.get(s[index], 0)+1
            else:
                current_freq[s[index]] = current_freq.get(s[index], 0)+1
                if index-starting_index+1 == p_count:
                    start_index.append(starting_index)
                    current_freq[s[starting_index]] = current_freq.get(s[starting_index], 0)-1
                    starting_index = starting_index +1
                     
        return start_index

            
