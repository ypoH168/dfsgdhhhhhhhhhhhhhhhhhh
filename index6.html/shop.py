from product import Product

товари = []

def add(n, c, k):
    товари.append(Product(n, c, k))

def show():
    for t in товари:
        print(t.n, t.c, "грн", t.k, "шт")

def find(n):
    for t in товари:
        if t.n == n:
            return t
    return None
