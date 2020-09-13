# CODING CHALLENGES
print('CODING CHALLENGES ANSWERS:')


# Code Challenge: Solve the Minimum Skew Problem.
# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
#       Input: A DNA string Genome.
#       Output: All integer(s) i minimizing Skew_i (Genome) among all values of i (from 0 to |Genome|).
def MinimumSkew(genome):
    min_skew = 0
    skew = 0
    positions = set()
    for pos, symbol in enumerate(genome):
        if symbol == 'G':
            skew += 1
        elif symbol == 'C':
            skew -= 1
        if skew < min_skew:
            positions = {pos + 1}
            min_skew = skew
        elif skew == min_skew:
            positions.add(pos + 1)
    return positions


with open('dataset_7_6.txt') as data:
    print(
        'Minimum Skew Problem -',
        *MinimumSkew(
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Solve the Hamming Distance Problem.
# Hamming Distance Problem: Compute the Hamming distance between two strings.
#       Input: Two strings of equal length.
#       Output: The Hamming distance between these strings.
def HammingDistance(string_1, string_2):
    res = 0
    for val_1, val_2 in zip(string_1, string_2):
        if val_1 != val_2:
            res += 1
    return res


with open('dataset_9_3.txt') as data:
    print(
        'Hamming Distance Problem -',
        HammingDistance(
            data.readline().rstrip('\n'),
            data.readline().rstrip('\n')
        )
    )


# Code Challenge: Solve the Approximate Pattern Matching Problem.
# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#       Input: Strings Pattern and Text along with an integer d.
#       Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
def ApproximatePatternMatching(pattern, text, d):
    positions = set()
    for i in range(len(text) - len(pattern) + 1):
        if HammingDistance(pattern, text[i:i + len(pattern)]) <= d:
            positions.add(i)
    return positions


with open('dataset_9_4.txt') as data:
    print(
        'Approximate Pattern Matching Problem -',
        *ApproximatePatternMatching(
            data.readline().rstrip('\n'),
            data.readline().rstrip('\n'),
            int(data.readline().rstrip('\n'))
        )
    )


# Code Challenge: Implement ApproximatePatternCount.
#       Input: Strings Pattern and Text as well as an integer d.
#       Output: Count_d(Text, Pattern).
def ApproximatePatternCount(pattern, text, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if HammingDistance(pattern, text[i:i + len(pattern)]) <= d:
            count += 1
    return count


with open('dataset_9_6.txt') as data:
    print(
        'ApproximatePatternCount Implementation -',
        ApproximatePatternCount(
            data.readline().rstrip('\n'),
            data.readline().rstrip('\n'),
            int(data.readline().rstrip('\n'))
        )
    )


# Code Challenge: Implement Neighbors to find the d-neighborhood of a string.
#       Input: A string Pattern and an integer d.
#       Output: The collection of strings Neighbors(Pattern, d).
#       (You may return the strings in any order, but each line should contain only one string.)
def Neighbors(pattern, d):
    nucleotides = {'A', 'C', 'G', 'T'}
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return nucleotides
    neighborhood = set()
    suffix_neighbors = Neighbors(pattern[1:], d)
    for string in suffix_neighbors:
        if HammingDistance(string, pattern[1:]) < d:
            neighborhood.update([x + string for x in nucleotides])
        else:
            neighborhood.add(pattern[0] + string)
    return neighborhood


with open('dataset_3014_4.txt') as data:
    print(
        'Neighbors Implementation -',
        *Neighbors(
            data.readline().rstrip('\n'),
            int(data.readline().rstrip('\n'))
        )
    )


# Code Challenge: Solve the Frequent Words with Mismatches Problem.
# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#       Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
#       Output: All most frequent k-mers with up to d mismatches in Text.
def PatternToNumber(pattern):
    letter_to_digit = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}
    return int(pattern.translate(str.maketrans(letter_to_digit)), base=4) if pattern else 0


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


def ComputingFrequenciesWithMismatches(text, k, d):
    freq_dict = {}
    for i in range(len(text) - k + 1):
        patterns = Neighbors(text[i:i + k], d)
        for pattern in patterns:
            index = PatternToNumber(pattern)
            if index in freq_dict:
                freq_dict[index] += 1
            else:
                freq_dict[index] = 1
    return freq_dict


def FrequentWordsWithMismatches(text, k, d):
    freq_dict = ComputingFrequenciesWithMismatches(text, k, d)
    keys = set()
    for key, value in freq_dict.items():
        if value == max(freq_dict.values()):
            keys.add(NumberToPattern(key, k))
    return keys


with open('dataset_9_7.txt') as data:
    print(
        'Frequent Words with Mismatches Problem -',
        *FrequentWordsWithMismatches(
            data.readline().rstrip('\n'),
            *map(int, data.readline().rstrip('\n').split())
        )
    )


# Code Challenge: Solve the Frequent Words with Mismatches and Reverse Complements Problem.
# Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers
# (with mismatches and reverse complements) in a string.
#       Input: A DNA string Text as well as integers k and d.
#       Output: All k-mers Pattern maximizing the sum Count_d(Text, Pattern) + Count_d(Text, Pattern_rc)
#       over all possible k-mers.
def ReverseComplement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return pattern.translate(str.maketrans(complement))[::-1]


def ComputingFrequenciesWithMismatchesAndReverseComplements(text, k, d):
    freq_dict = {}
    for i in range(len(text) - k + 1):
        patterns = Neighbors(text[i:i + k], d)
        patterns.update(Neighbors(ReverseComplement(text[i:i + k]), d))
        for pattern in patterns:
            index = PatternToNumber(pattern)
            if index in freq_dict:
                freq_dict[index] += 1
            else:
                freq_dict[index] = 1
    return freq_dict


def FrequentWordsWithMismatchesAndReverseComplements(text, k, d):
    freq_dict = ComputingFrequenciesWithMismatchesAndReverseComplements(text, k, d)
    keys = set()
    for key, value in freq_dict.items():
        if value == max(freq_dict.values()):
            keys.add(NumberToPattern(key, k))
    return keys


with open('dataset_9_8.txt') as data:
    print(
        'Frequent Words with Mismatches and Reverse Complements Problem -',
        *FrequentWordsWithMismatchesAndReverseComplements(
            data.readline().rstrip('\n'),
            *map(int, data.readline().rstrip('\n').split())
        )
    )

with open('Salmonella_enterica.txt') as data:
    genome = ''
    for line in data.readlines()[1:]:
        genome += line.rstrip('\n')
    print('/Salmonella Enterica Genome/')
    print(
        'Position of minimum skew -',
        *MinimumSkew(genome)
    )
    print(
        'In 250 nucleotides to both sides window (500 total) most frequent 9-mers with 1 mismatch max -',
        *FrequentWordsWithMismatchesAndReverseComplements(genome[3764856 - 250: 3764856 + 250], 9, 1)
    )
print('Answer - AGCTTCCGG')


# ---------------------------------------------------------------------------------------------------------------------
# QUIZ 2
# Question 1: The position of the E. coli genome at which the skew attains a minimum value is most likely near which
# of the following?
print('-----------------------------\n'
      'QUIZ 2 ANSWERS:\nQ1 -', 'The origin of replication')


# Question 2: Compute the Hamming distance between CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG and
# ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT.
print(
    'Q2 -',
    HammingDistance(
        'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG',
        'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
    )
)


# Question 3: Identify the value of i for which Skew_i (GCATACACTTCCCAGTAGGTACTG) attains a maximum value.
def MaximumSkew(genome):
    max_skew = 0
    skew = 0
    positions = set()
    for pos, symbol in enumerate(genome):
        if symbol == 'G':
            skew += 1
        elif symbol == 'C':
            skew -= 1
        if skew > max_skew:
            positions = {pos + 1}
            max_skew = skew
        elif skew == max_skew:
            positions.add(pos + 1)
    return positions


print('Q3 -', *MaximumSkew('GCATACACTTCCCAGTAGGTACTG'))


# Question 4: Compute Count2(CATGCCATTCGCATTGTCCCAGTGA, CCC).
print('Q4 -', ApproximatePatternCount('CCC', 'CATGCCATTCGCATTGTCCCAGTGA', 2))


# Question 5: The d-neighborhood of the k-mer Pattern is the collection of all k-mers that are at most Hamming distance
# d from Pattern.
# How many 10-mers are in the 1-neighborhood of Pattern = CCAGTCAATG?
# Note that the d-neighborhood of Pattern includes Pattern.
print('Q5 -', len([x for x in Neighbors('CCAGTCAATG', 1) if len(x) == 10]))
