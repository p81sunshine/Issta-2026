def compute_max_photos(H, W, n, photos):
    grid = [[0] * W for _ in range(H)]
    
    def can_place_photo(h, w, i, j):
        if i + h > H or j + w > W:
            return False
        for x in range(i, i + h):
            for y in range(j, j + w):
                if grid[x][y] != 0:
                    return False
        return True
    
    def place_photo(h, w, i, j):
        for x in range(i, i + h):
            for y in range(j, j + w):
                grid[x][y] = 1

    photos_sorted = sorted(photos, key=lambda x: (x[0] * x[1]), reverse=True)
    placed_count = 0

    for h, w in photos_sorted:
        placed = False
        for i in range(H):
            if placed:
                break
            for j in range(W):
                if can_place_photo(h, w, i, j):
                    place_photo(h, w, i, j)
                    placed_count += 1
                    placed = True
                    break
                else:
                    # This is a subtle bug - it breaks the inner loop unnecessarily
                    break
    
    return placed_count


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    H = int(data[0])
    W = int(data[1])
    n = int(data[2])
    
    photos = []
    index = 3
    for _ in range(n):
        h = int(data[index])
        w = int(data[index + 1])
        photos.append((w, h))  # This is a subtle bug - swaps height and width
        index += 2

    max_photos = compute_max_photos(H, W, n, photos)
    print(max_photos)

if __name__ == "__main__":
    main()