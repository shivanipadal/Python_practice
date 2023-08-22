import argparse 

parser=argparse.ArgumentParser()

# parser.add_argument("number", help="Calculate squere number", type=int)
# args = parser.parse_args()
# sqnumber = args.number ** 2
# print(args.number)
# print(sqnumber)

# parser.add_argument('--verbose', help='verbose switch', action='store_true')

# arg = parser.parse_args()

# if arg.verbose :
#     print('true')



#short options
parser= argparse.ArgumentParser(description='Verbose test')
# parser.add_argument('-v', '--verbose', help='Verbose is true', action='store_true')  #short options
parser.add_argument('-v', '--verbose', help='Verbose is true', choices=[0, 1, 2], type=int, default=1)
arg = parser.parse_args()

print(f'running {__file__}')

if arg.verbose :
    print('True')




