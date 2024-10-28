from typing import List
input_numbers = {1, 2, 3, 4, 5, 6}

class Cube():
    def __init__(self, shape_str: str):
        numbers_list = list(map(int, shape_str.split()))
        self.faces: List[set] = [{numbers_list[0], numbers_list[5]}, {numbers_list[1], numbers_list[3]}, {numbers_list[2], numbers_list[4]}]

    def get_other(self, num): return [ face - {num} for face in self.faces if num in face ][0].pop()

def main():
    cube_count = int(input())
    cube_list: List[Cube] = []
    for i in range(cube_count): cube_list.append(Cube(input()))

    total_faces = {}

    for base_num in range(1, 7):
        total_faces[base_num], bottom_face = 0, base_num

        for cube_obj in cube_list:
            top_face = cube_obj.get_other(bottom_face)
            total_faces[base_num] += max(input_numbers - {bottom_face, top_face})
            bottom_face = top_face

    return max(total_faces.values())

print(main())

