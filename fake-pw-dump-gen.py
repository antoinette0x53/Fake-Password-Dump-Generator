#!/usr/bin/python
import time
import gzip
import argparse
import numpy
import random
import sys
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
parser.add_argument("--weak-pw-perc","-w", dest="weak_pw_perc", help="Specify the percentage of weak passwords to use. Default is 0.3. Must be <= 1.0", type=float,default=0.3)
args = parser.parse_args()
if args.weak_pw_perc < 1.0:
    weak_pw_perc = args.weak_pw_perc
else:
    raise ValueError('percentage must be less than or equal to 1.0')

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
    with open('rockyou.txt', 'rb') as ry:
        lines = ry.readlines()
except Exception as e:
    print(str(e))

flag = True
while(flag):
    password = gen_pw(numpy.random.choice(password_type,p=[weak_pw_perc,1.0 - weak_pw_perc]))
    ip = faker.ipv4()
    email = faker.email()
    f.write('email=%s:password=%s:ip=%s\n' % (email, password, ip))
    f.flush()

    log_lines = log_lines - 1
    flag = False if log_lines == 0 else True

