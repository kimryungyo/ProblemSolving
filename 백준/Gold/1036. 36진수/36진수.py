digit_to_char_mapping = {**{i: str(i) for i in range(10)}, **{10 + i: chr(65 + i) for i in range(26)}}
char_to_digit_mapping = {v: k for k, v in digit_to_char_mapping.items()}

class Base36():
    def __init__(self, number):
        self.number = number

    def __str__(self): return self._number
    def __repr__(self): return f"Base36(\"{self.number}\")"

    @property
    def number(self): return self._number

    @number.setter
    def number(self, number: int):
        if number == 0:
            self.decimal, self._number = 0, "0"
            return

        if type(number) == str:
            self._number = number

            index, self.decimal = 0, 0
            for character in number[::-1]:
                self.decimal += char_to_digit_mapping[character] * ( 36 ** index )
                index += 1

        elif type(number) == int:
            self.decimal = number
            
            self._number = ""
            while number > 0:
                number, remainder = divmod(number, 36)
                self._number = digit_to_char_mapping[remainder] + self._number

    @property
    def decimal(self): return self._decimal

    @decimal.setter
    def decimal(self, number: int): self._decimal = number

def main():
    count = int(input())

    numbers = []
    characters = set()
    for i in range(count):
        base36_number = input()
        numbers.append(base36_number)
        characters = characters.union(set(base36_number))

    character_distance = {}
    for character in characters:
        base36_original_sum = 0
        base36_converted_sum = 0

        for num in numbers:
            base36_original_sum += Base36(num).decimal
            base36_converted_sum += Base36(num.replace(character, "Z")).decimal

        character_distance[character] = base36_converted_sum - base36_original_sum

    important_characters = [char for char, distance in sorted(character_distance.items(), key=lambda x: x[1], reverse=True)]

    replacement_count = int(input())
    base36_sum = 0
    for num in numbers:
        for idx in range(replacement_count):
            if len(important_characters) > idx: num = num.replace(important_characters[idx], "Z")
        base36_sum += Base36(num).decimal

    print(Base36(base36_sum))
    
main()

