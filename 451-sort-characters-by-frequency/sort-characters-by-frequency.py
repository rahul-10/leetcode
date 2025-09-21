from functools import cmp_to_key


class Solution:

    def custom_cmp(self, obj_1: dict, obj_2: dict) -> int:
        return -1 * (obj_1['frequency'] - obj_2['frequency'])

    def frequencySort(self, s: str) -> str:
        # if len(s) <=2:
        #     return s

        map = {}
        for char in s:
            map[char] = map.get(char, 0) + 1
        # print("map: ", map)
        char_list = []
        for key, value in map.items():
            char_list.append({ "key" : key, "frequency": value})
        # print("B char_list: ", char_list)
        char_list.sort(key = cmp_to_key(self.custom_cmp))
        # print("A char_list: ", char_list)

        sorted_string = ""
        for char_obj in char_list:
            for index in range(0, char_obj["frequency"]):
                sorted_string = sorted_string + char_obj["key"]
        
        return sorted_string

