def all_unique(test_list):
    return len(test_list) > len(set(test_list))

    if __name__ == "__main__":
        import sys
        test_cases = [list(map(int, line.strip().split())) for line in sys.stdin]
        for case in test_cases:
            print(all_unique(case))