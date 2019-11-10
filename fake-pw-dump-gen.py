#!/usr/bin/python
import time
import gzip
import argparse
import numpy
import random
from faker import Faker

def gen_pw(pass_type):
    password = ''
    if pass_type == 'weak':
        password = random.choice(lines).decode('utf-8').rstrip()
    if pass_type ==  'strong':
        password = faker.password()
    return password

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

password_type = ["weak","strong"]
try:
    with open('rockyou100.txt', 'rb') as ry:
        lines = ry.readlines()
except Exception as e:
    print(str(e))

flag = True
while(flag):
    password = gen_pw(numpy.random.choice(password_type,p=[0.7,0.3]))
    ip = faker.ipv4()
    email = faker.email()
    f.write('%s, %s, %s\n' % (email, password, ip))
    f.flush()

    log_lines = log_lines - 1
    flag = False if log_lines == 0 else True

