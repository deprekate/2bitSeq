# 2bitSeq

Although A, C, G & T can be mapped arbitrarily onto 00, 01, 10, 11 -- or any other arrangment -- there's at least one mapping that falls out for practically free from ASCII codes, A, C, G & T -> 00, 01, 11, 10:

```
A 65 01000|00|1  0
C 67 01000|01|1  1
G 71 01000|11|1  3
T 84 01010|10|0  2
```
Conveniently, the arrangement can also work for RNA as the U nucleotide doesn't disturb the bit pattern when it replaces the DNA T nucleotide:
```
U 85 01010|10|1  2
```
To get from ASCII letter to bits, simply shift and mask: (N >> 1) & 3

