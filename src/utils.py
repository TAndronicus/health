def print_table(table):
    n = len(table[0])
    br = [0 for _ in range(n)]
    for row in table:
        for i in range(n):
            br[i] = max(br[i], len(str(row[i])))
    for row in table:
        print(f' | '.join(map(lambda i: str(row[i]).ljust(br[i]), range(n))))
