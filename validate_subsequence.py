def isValidSubsequence(array, sequence):
    # Write your code here.
    index_matched = 0
    n = len(sequence)
    for x in array:
        if index_matched == n: return True
        if x == sequence[index_matched]:
            index_matched += 1
    return False

isValidSubsequence(
    [5, 1, 22, 25, 6, -1, 8, 10],
    [1, 6, -1, -1]
)