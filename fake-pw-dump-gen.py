#!/usr/bin/python
import time
import gzip
import argparse
from faker import Faker

parser = argparse.ArgumentParser(__file__, description="Fake Password Dump Generator")
parser.add_argument("--output", "-o", dest="output",help="Specify where to output dump file",type=str)
parser.add_argument("--num","-n",dest="num_lines",help="The number of lines in dump",type=int, default=1)
parser.add_argument("--zip","-z",dest="zip",help="gzip the dump file", type=bool, default=False, const=True, nargs='?')

args = parser.parse_args()

log_lines = args.num_lines
output_path = '' if not args.output else args.output
timestr = time.strftime("%Y%m%d-%H%M%S")
outputFileName = 'password_dump_'+timestr+'.dump'
if args.zip:
    f = gzip.open(output_path+outputFileName+'.gz','wt')
else:
    f = open(output_path+outputFileName, 'w')

faker = Faker()

flag = True
while(flag):
    password = faker.password()
    ip = faker.ipv4()
    email = faker.email()
    f.write('%s, %s, %s\n' % (email, password, ip))
    f.flush()

    log_lines = log_lines - 1
    flag = False if log_lines == 0 else True

