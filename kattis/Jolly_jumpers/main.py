while True:
    try:
        n, *nums = map(int, input().split())
        found = [0 for _ in range(n - 1)]
        f, *nums = nums
        for i in nums:
            if n - 1 > abs(f - i) - 1:
                found[abs(f - i) - 1] = 1
                f = i

        if sum(found) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")

    except EOFError:
        break
