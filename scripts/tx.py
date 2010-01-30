import sys, os

total = 192
parts, part = map(int, sys.argv[1:])

tests = range(total)[part::parts]

os.system('rm -fR tx%d' % part)
os.system('mkdir tx%d' % part)
os.system('cp -R testdata tx%d' % part)
os.system('cp -R shedskin tx%d' % part)
os.system('cp unit.py tx%d' % part)
os.system('cp FLAGS tx%d/shedskin' % part)

os.system('cd tx%d; python unit.py -f -l %s' % (part, ' '.join(map(str, tests))))
