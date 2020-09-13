# QUIZ 1
# Question 1: The Hidden Message Problem is a well-defined computational problem. - That's False.
print('QUIZ 1 ANSWERS:\nQ1 -', 'False')


# Question 2: Compute Count(ACTGTACGATGATGTGTGTCAAAG, TGT)
def occurrences(string, sub):
    counter = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            counter += 1
        else:
            return counter


print('Q2 -', occurrences('ACTGTACGATGATGTGTGTCAAAG', 'TGT'))

# Question 3: What is the most frequent 3-mer of CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT?
text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
chunks = [text[i: i + 3] for i in range(len(text) - 2)]
count = dict()
for triple in chunks:
    if triple in count.keys():
        count[triple] += 1
    else:
        count[triple] = 1
print('Q3 -', sorted(count, key=count.get, reverse=True)[0])

# Question 4: What is the reverse complement of GATTACA?
print('Q4 -', 'CTAATGT'[::-1])


# Question 5: Solve the Pattern Matching Problem with Text = ATGACTTCGCTGTTACGCGC and Pattern = CGC to find
# all starting positions of Pattern in Text. Return the starting positions in increasing order
# (make sure to use 0-based indexing!)
# Enter your answer as a collection of space-separated integers. (e.g., 4 7 14)
def z_func(string):
    """
        Z-function of string.

        Input:

        string - given string, str.

        Output:

        Numerical values of z-function for each
        element of string.
    """
    z_values = [0] * len(string)

    left, right = 0, 0
    for i in range(1, len(string)):
        if i > right:
            left = right = i
            while right < len(string) and string[right] == string[right - left]:
                right += 1
            z_values[i] = right - left
            right -= 1
        else:  # checking values from [left, right] interval
            j = i - left
            if z_values[j] < right - i + 1:  # if it's not last element
                z_values[i] = z_values[j]
            else:  # if it's last element, compare next ones
                left = i
                while right < len(string) and string[right] == string[right - left]:
                    right += 1
                z_values[i] = right - left
                right -= 1
    return z_values


def rabin_karp(target, string):
    new_string = target + '#' + string
    enterings = []

    z_list = z_func(new_string)

    for j in range(len(z_list)):
        if z_list[j] == len(target):
            enterings.append(j - len(target) - 1)

    if enterings:
        return enterings
    else:
        return [None]


print('Q5 -', *rabin_karp('CGC', 'ATGACTTCGCTGTTACGCGC'), '\n-----------------------------')


# ---------------------------------------------------------------------------------------------------------------------
# CODING CHALLENGES
# Code Challenge: Implement PatternCount.
#       Input: Strings Text and Pattern.
#       Output: Count(Text, Pattern).
def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count


with open('dataset_2_7.txt') as data:
    print(
        'CODING CHALLENGES ANSWERS:\n'
        'Pattern Count Implementation -',
        PatternCount(
            data.readline().rstrip('\n'),
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Solve the Frequent Words Problem.
#       Input: A string Text and an integer k.
#       Output: All most frequent k-mers in Text.
def FrequentWords(text, k):
    freq_patterns = set()
    count = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern not in count:
            count[pattern] = PatternCount(text, pattern)
    for pattern in count:
        if count[pattern] == max(count.values()):
            freq_patterns.add(pattern)
    return freq_patterns


with open('dataset_2_10.txt') as data:
    print(
        'Frequent Words Problem -',
        *FrequentWords(
            data.readline().rstrip('\n'),
            int(data.readline().rstrip('\n'))
        )
    )


# Reverse Complement Problem: Find the reverse complement of a DNA string.
#       Input: A DNA string Pattern.
#       Output: Pattern_rc , the reverse complement of Pattern.
def ReverseComplement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return pattern.translate(str.maketrans(complement))[::-1]


with open('dataset_3_2.txt') as data:
    print(
        'Reverse Complement Problem -',
        ReverseComplement(
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Solve the Pattern Matching Problem.
#       Input: Two strings, Pattern and Genome.
#       Output: A collection of space-separated integers specifying all starting positions where Pattern appears as
#       a substring of Genome.
with open('dataset_3_5.txt') as data:
    print(
        'Pattern Matching Problem -',
        *rabin_karp(
            data.readline().rstrip('\n'),
            data.readline().rstrip('\n')
        )
    )

with open('Vibrio_cholerae.txt') as data:
    print(
        'Vibrio Cholerae Genome -',
        *rabin_karp(
            'CTTGATCAT',
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Implement PatternToNumber.
#       Input: A DNA string Pattern.
#       Output: The integer PatternToNumber(Pattern).
def PatternToNumber(pattern):
    letter_to_digit = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}
    return int(pattern.translate(str.maketrans(letter_to_digit)), base=4) if pattern else 0


with open('dataset_3010_2.txt') as data:
    print(
        'PatternToNumber Implementation -',
        PatternToNumber(
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Implement ComputingFrequencies to generate a frequency array.
#       Input: A DNA string Text followed by an integer k.
#       Output: FrequencyArray(Text).
def ComputingFrequencies(text, k):
    freq_dict = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        index = PatternToNumber(pattern)
        if index in freq_dict:
            freq_dict[index] += 1
        else:
            freq_dict[index] = 1
    # For answer on Stepik
    # ans = [0 for _ in range(4 ** k)]
    # for ind in freq_dict:
    #     ans[ind] = freq_dict[ind]
    # return ans
    return freq_dict


with open('dataset_2994_5.txt') as data:
    print(
        'ComputingFrequencies Implementation -',
        ComputingFrequencies(
            data.readline().rstrip('\n'),
            int(data.readline().rstrip('\n'))
        )
    )


# Code Challenge: Implement NumberToPattern.
#       Input: Integers index and k.
#       Output: The string NumberToPattern(index, k).
def NumberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def NumberToPattern(n, k):
    digit_to_letter = {'0': 'A', '1': 'C', '2': 'G', '3': 'T'}
    if k == 1:
        return digit_to_letter[str(n)]
    pattern = ''.join([digit_to_letter[str(digit)] for digit in NumberToBase(n, 4)])
    if len(pattern) == k:
        return pattern
    else:
        return 'A' * (k - len(pattern)) + pattern


with open('dataset_3010_5.txt') as data:
    print(
        'NumberToPattern Implementation -',
        NumberToPattern(
            int(data.readline().rstrip('\n')),
            int(data.readline().rstrip('\n'))
        )
    )


# Code Challenge: Solve the Clump Finding Problem (Find patterns forming clumps in a string.)
#       Input: A string Genome, and integers k, L, and t.
#       Output: All distinct k-mers forming (L, t)-clumps in Genome.
def ClumpFinding(genome, k, window, t):
    freq_pat = set()
    clump = {}
    text = genome[:window]
    freq_dict = ComputingFrequencies(text, k)
    for val in freq_dict:
        if freq_dict[val] >= t:
            clump[val] = 1
    for i in range(1, len(genome) - window + 1):
        start_pattern = genome[i - 1: i - 1 + k]
        freq_dict[PatternToNumber(start_pattern)] -= 1
        end_pattern = genome[i + window - k: i + window]
        index = PatternToNumber(end_pattern)
        if index in freq_dict:
            freq_dict[index] += 1
        else:
            freq_dict[index] = 1
        if freq_dict[index] >= t:
            clump[index] = 1
    for val in clump:
        freq_pat.add(NumberToPattern(val, k))
    return freq_pat


with open('dataset_4_5.txt') as data:
    print(
        'Clump Finding Problem -',
        *ClumpFinding(
            data.readline().rstrip('\n'),
            *map(int, data.readline().rstrip('\n').split())
        )
    )
print('AND IT IS CORRECT =)))))))))))))))))')

# 24 sec =))))
with open('E_coli.txt') as data:
    print(
        'E. Coli Genome -',
        len(
            ClumpFinding(
                data.readline().rstrip('\n'),
                9, 500, 3
            )
        )
    )
