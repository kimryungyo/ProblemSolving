def calculate_cuts_needed(total_sausage_count: int, critic_count: int) -> int:
    total_sausage_length = total_sausage_count * 1
    cutted_sausage_length = total_sausage_length / (critic_count)
    number_of_cuts = critic_count - 1
    cut_positions = {cutted_sausage_length * number_of_cut for number_of_cut in range(1, number_of_cuts+1)}
    for cut_pos in cut_positions:
        if cut_pos % 1 == 0:
            number_of_cuts -= 1
    return number_of_cuts

def main():
    sausage_count, critic_count = map(int, input().split())
    print(calculate_cuts_needed(sausage_count, critic_count))

if __name__ == "__main__":
    main()

