zeilen = [
   [1, 1, 1, 3, 1, 1, 7, 2],
   [3, 4, 1, 1, 2, 7, 1],
   [3, 4, 1, 2, 2, 2, 1, 2],
   [1, 2, 1, 4, 1, 1, 4, 7],
   [1, 2, 3, 2, 1, 1, 2, 6],
   [1, 1, 5, 1, 1, 11],
   [1, 2, 1, 2, 2, 1, 1, 2, 1, 7],
   [2, 4, 3, 2, 2, 1, 4, 1],
   [2, 1, 1, 4, 1, 1, 7, 2, 1],
   [2, 1, 2, 1, 2, 1, 1, 3, 2, 1, 2],
   [4, 1, 1, 2, 1, 1, 12],
   [1, 2, 1, 1, 1, 1, 1, 1],
   [6, 1, 2, 17],
   [2, 2],
   [1, 2],
   [1, 2],
   [6, 2, 2, 3, 4],
   [1, 2, 3, 1, 1],
   [3, 1, 1, 2, 3, 1, 1, 2],
   [1, 1, 1, 1, 5, 1, 1, 1, 1],
   [3, 1, 1, 6, 1, 2, 1, 2],
   [1, 1, 1, 6, 2, 1],
   [1, 4, 6, 3, 4],
   [6, 6, 3, 1],
   [1, 1, 6, 4, 1],
   [1, 1, 3, 6, 1],
   [1, 1, 7, 3],
   [4, 1, 1, 3],
   [3, 1, 3],
   [2, 3],
   [20, 2, 1, 3],
   [2, 5, 6, 2],
   [11, 6, 2, 3],
   [9, 5, 3],
   [9, 5, 3, 2],
   [13, 6, 1],
   [7, 17, 1],
   [4, 5, 3, 1, 3],
   [12, 10],
   [6, 1, 8, 1]]
spalten = [
   [2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
   [3, 4, 1, 1, 3, 1, 1, 1, 1, 2, 1],
   [1, 1, 1, 3, 1, 1, 1, 4, 3, 1, 2, 1],
   [2, 1, 2, 1, 1, 4, 1, 3, 1, 2, 1],
   [1, 2, 2, 1, 1, 1, 1, 1, 3, 1],
   [1, 2, 3, 1, 8, 1, 1, 3, 2],
   [3, 2, 3, 1, 1, 3, 1],
   [4, 2, 3, 1, 1, 2, 2],
   [1, 1, 3, 1, 2, 5, 1, 1, 2, 2],
   [8, 1, 2, 1, 1, 2, 1, 2],
   [2, 1, 1, 2, 2, 2, 1, 4, 1, 2],
   [11, 2, 2, 1, 2, 1, 4],
   [2, 4, 3, 2, 3, 2, 1, 2, 2],
   [1, 1, 1, 2, 3, 3, 2, 1, 2, 1],
   [13, 8, 2, 1, 2, 1],
   [1, 8, 1, 2, 2, 2],
   [13, 8, 1, 2, 2, 2],
   [1, 1, 1, 1, 8, 1, 3, 2, 1],
   [2, 2, 1, 3, 1, 1, 8, 3, 1, 2, 1],
   [2, 8, 1, 5, 7, 3, 1, 2, 1],
   [1, 2, 1, 3, 1, 2, 4, 2, 1, 1, 2],
   [4, 2, 1, 3, 2, 1, 1, 3, 4, 2],
   [2, 2, 4, 1, 4, 3, 2, 1, 5],
   [2, 8, 1, 6, 1, 3, 2, 1],
   [9, 3, 4, 1, 5, 2],
   [1, 5, 2, 1, 2, 1, 3, 4, 1],
   [1, 4, 1, 1, 1, 7, 3, 2, 2, 3, 1],
   [7, 1, 3, 1, 1, 4, 1, 2, 3],
   [1, 2, 3, 2, 1, 1, 3, 1, 3, 1, 3, 2],
   [1, 1, 2, 3, 1, 1, 1, 1, 4, 1, 1, 6]]

for zf in zeilen:
  print(''.join([chr(n+64) for n in zf]),end=' ')
print()  
for zf in spalten:
  print(''.join([chr(n+64) for n in zf]),end=' ')
print()         