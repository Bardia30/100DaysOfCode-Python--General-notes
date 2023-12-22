#put a pointer on sequence
#loop over array




def isValidSubsequence(array, sequence):
    pointer = 0
    for num in array:
        if pointer > len(sequence) - 1:
            break
        if num == sequence[pointer]:
            pointer += 1

    return pointer == len(sequence)


print(isValidSubsequence([5,1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))