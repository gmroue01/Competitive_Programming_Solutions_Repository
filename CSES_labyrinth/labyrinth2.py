import sys
from collections import deque


def bfs(grid, n, m, start, end):
    """BFS sur grille aplatie. Renvoie came[] ou None si B est inatteignable."""
    WALL = 35                      # ord('#')
    U, D, L, R = 85, 68, 76, 82    # ord('U'), ord('D'), ord('L'), ord('R')

    visited = bytearray(n * m)
    came = bytearray(n * m)        # direction utilisee pour ENTRER dans la case
    visited[start] = 1
    q = deque([start])

    while q:
        k = q.popleft()
        if k == end:
            return came
        c = k % m

        nk = k - m                                       # haut
        if k >= m and not visited[nk] and grid[nk] != WALL:
            visited[nk] = 1; came[nk] = U; q.append(nk)
        nk = k + m                                       # bas
        if nk < n * m and not visited[nk] and grid[nk] != WALL:
            visited[nk] = 1; came[nk] = D; q.append(nk)
        nk = k - 1                                       # gauche
        if c > 0 and not visited[nk] and grid[nk] != WALL:
            visited[nk] = 1; came[nk] = L; q.append(nk)
        nk = k + 1                                       # droite
        if c + 1 < m and not visited[nk] and grid[nk] != WALL:
            visited[nk] = 1; came[nk] = R; q.append(nk)

    return came if visited[end] else None


def path_direction(came, m, start, end):
    """Remonte de B vers A en inversant chaque direction, puis renvoie A -> B."""
    back = {85: m, 68: -m, 76: 1, 82: -1}   # arrive par 'U' => le parent est en dessous
    res = bytearray()
    k = end
    while k != start:
        ch = came[k]
        res.append(ch)
        k += back[ch]
    res.reverse()
    return res.decode()


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    grid = b''.join(data[2:2 + n])

    start = grid.find(b'A')
    end = grid.find(b'B')

    came = bfs(grid, n, m, start, end)
    if came is None:
        sys.stdout.write("NO\n")
        return

    path = path_direction(came, m, start, end)
    sys.stdout.write("YES\n%d\n%s\n" % (len(path), path))


main()