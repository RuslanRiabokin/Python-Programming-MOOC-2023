# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list):
        if not my_list:
            return None

        frequency_dict = {}
        for item in my_list:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1

        most_common_item = max(frequency_dict, key=frequency_dict.get)
        return most_common_item

    @classmethod
    def doubles(cls, my_list):
        if not my_list:
            return 0

        frequency_dict = {}
        for item in my_list:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1

        count = 0
        for key, value in frequency_dict.items():
            if value >= 2:
                count += 1

        return count
