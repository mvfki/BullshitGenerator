import argparse
import sys
from .core import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--theme', metavar = 'STR', type = str, 
                        required = True, 
                        help = 'The theme you want to talk about.')
    parser.add_argument('-j', '--jsonDataBase', metavar = 'JSON', type = str, 
                        help = 'Optional. By default we load the original data.')
    parser.add_argument('-d', '--bsDataBase', metavar = 'NAME', type = str, 
                        help = 'The name of an existing BSDB. Optional, By default we load the original data')
    parser.add_argument('-p', '--bsDataBasePath', metavar = 'PATH', type = str, 
                        help = 'The path of the existing BSDB, can be included into NAME.')
    parser.add_argument('-w', '--wordLimit', metavar = 'INT', type = int, 
                        default = 1000, 
                        help = 'Around how many characters you want to get.')
    parser.add_argument('-r', '--repeatLevel', metavar = 'INT', type = int, 
                        default = 2)
    args = parser.parse_args()
    bs = bullShit(args.theme, jsonFile = args.jsonDataBase, BSDB = args.bsDataBase, 
                  BSDBPath = args.bsDataBasePath, wordLimit = args.wordLimit, 
                  repeatLevel = args.repeatLevel)
    sys.stderr.write('## THEME: %s\n' % args.theme)
    sys.stderr.write('## WORD #: %d\n' % args.wordLimit)
    sys.stderr.write('#### START ####\n')
    sys.stdout.write(str(bs))
    sys.stderr.write('\n#### END ####\n')

if __name__ == '__main__':
    main()
