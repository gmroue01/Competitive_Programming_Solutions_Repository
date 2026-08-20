n = int(input())
init_name = input()
name = input()


alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count = 0

for i in range(n):
    index_letter_previous = alpha.index(init_name[i])
    index_letter_next = alpha.index(name[i])

    d1 = abs(index_letter_previous-index_letter_next)
    d2 = len(alpha) - d1

    d = min(d1, d2)

    count += d

print(count)
