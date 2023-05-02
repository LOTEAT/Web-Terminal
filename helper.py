import argparse

def helper():
    parser = argparse.ArgumentParser(
                    prog='Web Ternimal',
                    description='WebTernimal')
    parser.add_argument('-p', type=int, default=8081)
    args = parser.parse_args()
    print(args)
    return args
    