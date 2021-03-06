#!/usr/bin/env python2.7

import os
import sys
import subprocess


def green( s ):
    return '\033[92m' + s + '\033[0m'


if __name__ == "__main__":
    errors = 0
    fail_fast = True
    args = sys.argv[ 1 ]
    if args and args[ 0 ] == '@':
        args = args[ 1: ]
        fail_fast = False
    projects = sys.argv[ 2: ]
    root_path = os.path.dirname( __file__ )
    for project in projects:
        dir_path = os.path.join( root_path, project )
        print green( "Attempting to run 'setup.py %s' in %s" % (args, dir_path) )
        assert os.path.isdir( dir_path )
        assert os.path.exists( os.path.join( dir_path, 'setup.py' ) )
        if 0 != subprocess.call( sys.executable + " setup.py " + args,
                                 cwd=dir_path, shell=True ):
            errors += 1
            assert errors < 128
            if fail_fast: break

    sys.exit( errors )
