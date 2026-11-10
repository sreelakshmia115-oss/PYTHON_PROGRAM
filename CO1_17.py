d = {'a': 3, 'b': 1, 'c': 2}

2 ascending = dict(sorted(d.items()))

3 descending = dict(sorted (d.items(), reverse=True ))

4 print("Ascending", ascending)

5 print("Descending", descending)