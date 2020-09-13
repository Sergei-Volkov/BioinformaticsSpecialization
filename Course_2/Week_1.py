# CODING CHALLENGES
print('CODING CHALLENGES ANSWERS:')


# Code Challenge: Solve the String Composition Problem.
#      Input: An integer k and a string Text.
#      Output: Composition_k(Text) (the k-mers can be provided in any order).
def StringComposition(text, k):
    k_mers = []
    for i in range(len(text) - k + 1):
        k_mers.append(text[i: i + k])
    return sorted(k_mers)


with open('dataset_197_3.txt') as data:
    lines = data.readlines()
    k_mers = StringComposition(
        lines[1].rstrip('\n'),
        int(lines[0].rstrip('\n'))
    )
with open('string_composition_answer.txt', 'w') as data:
    data.writelines("%s\n" % k_mer for k_mer in k_mers)
print('String Composition Problem -', 'In file "string_composition_answer.txt"')


# Code Challenge: Solve the String Spelled by a Genome Path Problem.
# String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
#       Input: A sequence path of k-mers Pattern_1, …, Pattern_n such that the last k - 1 symbols of Pattern_i
#       are equal to the first k-1 symbols of Pattern_(i+1) for 1 ≤ i ≤ n-1.
#       Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Pattern_i (for 1 ≤ i ≤ n).
def PathToGenome(path):
    text = path[0]
    for i in range(1, len(path)):
        text += path[i][-1]
    return text


with open('dataset_198_3.txt') as data:
    print(
        'String Spelled by a Genome Path Problem -',
        PathToGenome(data.read().splitlines())
    )


# Code Challenge: Solve the Overlap Graph Problem (restated below).
# Overlap Graph Problem: Construct the overlap graph of a collection of k-mers.
#       Input: A collection Patterns of k-mers.
#       Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
#       (You may return the nodes and their edges in any order.)
def Overlap(patterns):
    graph = {pattern: set() for pattern in patterns}
    for node in graph:
        for pattern in patterns:
            if pattern[:-1] == node[1:]:
                graph[node].add(pattern)
    return graph


with open('dataset_198_10.txt') as data:
    graph = Overlap(data.read().splitlines())

with open('overlap_graph_answer.txt', 'w') as data:
    for node, patterns in graph.items():
        if patterns:
            data.writelines([node + '->' + ','.join(patterns) + '\n'])
    print('Overlap Graph Problem -', 'In file "overlap_graph_answer.txt"')


# Code Challenge: Solve the De Bruijn Graph from a String Problem.
# De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.
#       Input: An integer k and a string Text.
#       Output: DeBruijn_k(Text), in the form of an adjacency list.
def DeBruijnFromString(text, k):
    graph = {text[i: i + k - 1]: list() for i in range(len(text) - k + 2)}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern[:-1] in graph:
            graph[pattern[:-1]].append(pattern[1:])
    return graph


with open('dataset_199_6.txt') as data:
    lines = data.readlines()
    graph = DeBruijnFromString(lines[1].rstrip(), int(lines[0].rstrip()))

with open('de_bruijn_graph_from_string_answer.txt', 'w') as data:
    for node, patterns in graph.items():
        if patterns:
            data.writelines([node + '->' + ','.join(patterns) + '\n'])
    print('De Bruijn Graph from a String Problem -', 'In file "de_bruijn_graph_from_string_answer.txt"')


# Code Challenge: Solve the de Bruijn Graph from k-mers Problem.
# DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
#       Input: A collection of k-mers Patterns.
#       Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
def DeBruijnFromKmers(patterns):
    graph = {}
    for pattern in patterns:
        graph[pattern[:-1]] = []
        graph[pattern[1:]] = []
    for pattern in patterns:
        graph[pattern[:-1]].append(pattern[1:])
    return graph


with open('dataset_200_8.txt') as data:
    graph = DeBruijnFromKmers(data.read().splitlines())

with open('de_bruijn_graph_from_kmers_answer.txt', 'w') as data:
    for node, patterns in graph.items():
        if patterns:
            data.writelines([node + '->' + ','.join(patterns) + '\n'])
    print('de Bruijn Graph from k-mers Problem -', 'In file "de_bruijn_graph_from_kmers_answer.txt"')


# ---------------------------------------------------------------------------------------------------------------------
# QUIZ 1
# Question 1: True or False: The human genome is the longest genome of any organism on Earth.
print('-----------------------------\n'
      'QUIZ 1 ANSWERS:\nQ1 -', 'False')


# Question 2: What is a cycle that visits every node in a graph called?
print('Q2 -', 'Hamiltonian')


# Question 3: Below is the adjacency list of a graph. Which of the following is a Hamiltonian cycle in this graph?
# (Select all that apply.)
# 1 -> 2,3,5
# 2 -> 4,5
# 3 -> 1,2,5
# 4 -> 1,3
# 5 -> 2,4
print('Q3 -', '1 -> 3 -> 5 -> 2 -> 4 -> 1', '&', '1 -> 3 -> 2 -> 5 -> 4 -> 1')


# Question 4: Which of the following are 3-universal linear binary strings? (Select all that apply.)
print('Q4 -', '1011100010 & 0111010001 & 0011101000')


# Question 5: What is the indegree of GTA in the de Bruijn graph constructed for the following collection of 4-mers?
# (Hint: how can you answer this question without having to construct the de Bruijn graph?)
# GCGA
# CAAG
# AAGA
# GCCG
# ACAA
# AGTA
# TAGG
# AGTA
# ACGT
# AGCC
# TTCG
# AGTT
# AGTA
# CGTA
# GCGC
# GCGA
# GGTC
# GCAT
# AAGC
# TAGA
# ACAG
# TAGA
# TCCT
# CCCC
# GCGC
# ATCC
# AGTA
# AAGA
# GCGA
# CGTA
print('Q5 -', 6)
