def lowest_consecutive(list: list[int]) -> list[int]:
    return [
        item
        for i, item in enumerate(sorted(list))
        if i != len(list) - 1 and item + 1 != list[i + 1]
    ]

def rotate(list, offset):
    return list[offset:] + list[:offset]
