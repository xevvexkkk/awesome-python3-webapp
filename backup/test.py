def inner_generator():
    i = 1
    while True:
        i = yield i
        if i > 10:
            raise StopIteration

def outer_generator():
    print("do something before yield")
    from_inner = 0
    from_outer = 1
    g = inner_generator()
    g.send(None)
    while True:
        try:
            from_inner = g.send(from_outer)
            from_outer = yield from_inner
        except StopIteration:
            break

def main():
    g = outer_generator()
    g.send(None)
    i = 0
    while True:
        try:
            i = g.send(i + 1)
            print(i)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
