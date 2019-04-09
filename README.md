# CodeforcesRound-550-DIV3
Codes of round#550 div 3


here, I have solved all the problems which came in codeforces round 550

1.Diverse String-:
    A string is called diverse if it contains consecutive (adjacent) letters of the Latin alphabet and each letter occurs exactly once.       For example, the following strings are diverse: "fced", "xyz", "r" and "dabcef". The following string are not diverse: "az", "aa",         "bad" and "babc". Note that the letters 'a' and 'z' are not adjacent.
    Formally, consider positions of all letters in the string in the alphabet. These positions should form contiguous segment, i.e. they       should come one by one without any gaps. And all letters in the string should be distinct (duplicates are not allowed).
    You are given a sequence of strings. For each string, if it is diverse, print "Yes". Otherwise, print "No".
   
   
2.Parity Alternated Deletion-:
    Polycarp has an array a consisting of n integers.
    He wants to play a game with this array. The game consists of several moves. On the first move he chooses any element and deletes it      (after the first move the array contains n−1 elements). For each of the next moves he chooses any element with the only restriction:      its parity should differ from the parity of the element deleted on the previous move. In other words, he alternates parities (even-odd-     even-odd-... or odd-even-odd-even-...) of the removed elements. Polycarp stops if he can't make a move.

    Formally:

    If it is the first move, he chooses any element and deletes it;
    If it is the second or any next move:
    if the last deleted element was odd, Polycarp chooses any even element and deletes it;
     if the last deleted element was even, Polycarp chooses any odd element and deletes it.
      If after some move Polycarp cannot make a move, the game ends.
    Polycarp's goal is to minimize the sum of non-deleted elements of the array after end of the game. If Polycarp can delete the whole       array, then the sum of non-deleted elements is zero.
    Help Polycarp find this value.
  
 3. Two Merged Sequence-:
     Two integer sequences existed initially, one of them was strictly increasing, and another one — strictly decreasing.
      Strictly increasing sequence is a sequence of integers [x1<x2<⋯<xk]. And strictly decreasing sequence is a sequence of integers         [y1>y2>⋯>yl]. Note that the empty sequence and the sequence consisting of one element can be considered as increasing or              decreasing.

      Elements of increasing sequence were inserted between elements of the decreasing one (and, possibly, before its first element and       after its last element) without changing the order. For example, sequences [1,3,4] and [10,4,2] can produce the following               resulting sequences: [10,1,3,4,2,4], [1,3,4,10,4,2]. The following sequence cannot be the result of these insertions:                   [1,10,4,4,3,2] because the order of elements in the increasing sequence was changed.

      Let the obtained sequence be a. This sequence a is given in the input. Your task is to find any two suitable initial sequences.         One of them should be strictly increasing, and another one — strictly decreasing. Note that the empty sequence and the sequence         consisting of one element can be considered as increasing or decreasing.

      If there is a contradiction in the input and it is impossible to split the given sequence a into one increasing sequence and one          decreasing sequence, print "NO".
   
   
 4.Two Shuffled Sequence-:
      Two integer sequences existed initially — one of them was strictly increasing, and the other one — strictly decreasing.
        Strictly increasing sequence is a sequence of integers [x1<x2<⋯<xk]. And strictly decreasing sequence is a sequence of integers         [y1>y2>⋯>yl]. Note that the empty sequence and the sequence consisting of one element can be considered as increasing or              decreasing.

        They were merged into one sequence a. After that sequence a got shuffled. For example, some of the possible resulting sequences         a for an increasing sequence [1,3,4] and a decreasing sequence [10,4,2] are sequences [1,2,3,4,4,10] or [4,2,1,10,4,3].

        This shuffled sequence a is given in the input.

          Your task is to find any two suitable initial sequences. One of them should be strictly increasing and the other one —                  strictly decreasing. Note that the empty sequence and the sequence consisting of one element can be considered as increasing or           decreasing.

            If there is a contradiction in the input and it is impossible to split the given sequence a to increasing and decreasing                sequences, print "NO".
