def sum_invalid_keys(ranges, is_valid_proc):
    total_invalid = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        for key in range(start, end + 1):
            if not is_valid_proc(key):
                print(f"Invalid key found: {key}")
                total_invalid += key
    return total_invalid

def is_valid_key(key):
    if (len(str(key)) % 2) != 0:
        return True
    size = len(str(key)) // 2
    return str(key)[:size] != str(key)[-size:]

def is_valid_key_alternate(key):
    for i in range(1, len(str(key))//2 + 1):
        key_to_check = str(key)[0:i]*(len(str(key))//len(str(key)[0:i]))
        if key_to_check==str(key):
            return False
    return True

if __name__ == "__main__":
    with open("2025/inputs/day2_input.txt") as f:
        ranges = f.read().strip().split(",")
    print(sum_invalid_keys(ranges, is_valid_proc=is_valid_key))
    print(sum_invalid_keys(ranges, is_valid_proc=is_valid_key_alternate))