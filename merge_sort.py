

def merge_sort(A, p, r):
    """
    Args:
        A (arr): array of integers
        p (int): indice in array. Pass 0 when initializing
        r (int): length of A
    Returns:
        A (arr) sorted smallest to highest value
    """
    if p < r:
        q = int((p + r)/2)
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
    """
    Args:
        A (arr): array of integers
        p (int): indice in A; <= to q
        q (int) indice in A; >= to p, < than r
        r (int) indice in A; > than p and q
    """
    pass


merge_sort([5, 4, 3, 2, 1, 0], 0, 6)
