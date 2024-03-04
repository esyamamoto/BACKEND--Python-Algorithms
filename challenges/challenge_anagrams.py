def merge_shot(word, start=0, end=None):
    if end is None:
        end = len(word)
    if end - start > 1:
        mid = (start + end) // 2
        merge_shot(word, start, mid)
        merge_shot(word, mid, end)
        merge(word, start, mid, end)
    return word


def merge(word, start, mid, end):
    first = word[start:mid]
    second = word[mid:end]
    first_index, second_index = 0, 0
    all_index = start

    while first_index < len(first):
        if (
            second_index < len(second)
            and second[second_index] < first[first_index]
        ):
            word[all_index] = second[second_index]
            second_index += 1
        else:
            word[all_index] = first[first_index]
            first_index += 1
        all_index += 1
    return word


def is_anagram(first_string, second_string):
    first_string_sorted = "".join(merge_shot(list(first_string.lower())))
    second_string_sorted = "".join(merge_shot(list(second_string.lower())))

    if first_string == "" or second_string == "":
        return (first_string_sorted, second_string_sorted, False)
    elif first_string_sorted == second_string_sorted:
        return (first_string_sorted, second_string_sorted, True)
    else:
        return (first_string_sorted, second_string_sorted, False)


print(is_anagram("valorant", "mewpi"))
