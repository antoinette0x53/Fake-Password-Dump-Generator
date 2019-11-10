# Fake-Password-Dump-Generator

Based on the [Fake-Apache-Log-Generate from kiritbasu](https://github.com/kiritbasu/Fake-Apache-Log-Generator) on Github, Fake Password Dump Generator will create a fake comma separated password dump of randomly generated email addresses, passwords, and IP addresses. 

## Usage

Generate 100 lines in the dump and output to temp.

`$ python3 fake-pw-dump-gen.py -n 100 -o /tmp/`

Output Filename format

`password_dump_TIMESTAMP.dump`


Help Output

```
$ python3 fake-pw-dump-gen.py --help
usage: fake-pw-dump-gen.py [-h] [--output OUTPUT] [--num NUM_LINES]
                           [--zip ZIP]

Fake Password Dump Generator

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Specify where to output dump file
  --num NUM_LINES, -n NUM_LINES
                        The number of lines in dump
  --zip ZIP, -z ZIP     gzip the dump file

```

## Requirements

- Python 3
- `pip3 install -r requirements.txt`

## License
This script is released under the Apache version 2 license.

