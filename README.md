# Fake-Password-Dump-Generator

Based on the [Fake-Apache-Log-Generate from kiritbasu](https://github.com/kiritbasu/Fake-Apache-Log-Generator) on Github, Fake Password Dump Generator will create a fake comma separated password dump of randomly generated email addresses, passwords, and IP addresses. 

## Usage

Generate 100 lines in the dump and output to temp.

`$ python3 fake-pw-dump-gen.py -n 100 -o /tmp/`

Output Filename format

`password_dump_TIMESTAMP.dump`

Password Dump Line Format

`email={$EMAIL}:password={$PASSWORD}:ip={$IP}`

If you'd like to use a different format, edit the following line in `fake-pw-dump-gen.py`:

`f.write('email=%s:password=%s:ip=%s\n' % (email, password, ip))`

Help Output

```
$ python3 fake-pw-dump-gen.py --help

usage: fake-pw-dump-gen.py [-h] [--output OUTPUT] [--num NUM_LINES]
                           [--zip [ZIP]] [--weak-pw-perc WEAK_PW_PERC]

Fake Password Dump Generator

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Specify where to output dump file
  --num NUM_LINES, -n NUM_LINES
                        The number of lines in dump
  --zip [ZIP], -z [ZIP]
                        gzip the dump file
  --weak-pw-perc WEAK_PW_PERC, -w WEAK_PW_PERC
                        Specify the percentage of weak passwords to use.
                        Default is 0.3. Must be <= 1.0
```

## Requirements

- Python 3
- `pip3 install -r requirements.txt`

## License
This script is released under the Apache version 2 license.

## Notes
- The rockyou.txt file is a subset of the rockyou password dump and is used for the source of the 'weak' passwords. I noticed that the Faker `password()` function only generated strong passwords which would be unusual to see in a password dump. Adding in weak passwords from rockyou helped to make the password dump look a bit more realistic with the addition of duplicated and uncomplicated passwords.
