import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",type=int,help="increase verbosity",choices=[0,1,2],metavar="level")
group.add_argument("-q","--quiet",action="store_true")
parser.add_argument("x",type=int,help="the given base number")
parser.add_argument("y",type=int,help="the exponent number")
# parser.add_argument("-v","--verbose",type=int,choices=[0,1,2],help="increase output verbosity")
args = parser.parse_args()
answer = args.x**args.y
if args.quiet:
    print(f"{args.x}^{args.y}={answer}")
elif args.verbose == 1:
    print(f"level1:{args.x}^{args.y}={answer}")
elif args.verbose == 2:
    print(f"level2:{args.x}^{args.y}={answer}")
else:
    print(answer)
