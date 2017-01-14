#!/bin/bash

# This script works for macOS, but should work for *nix systems as well.
# Make sure to run it from the directory you're packaging.
# Lastly, it assumes you use virtual environments and have a environment var
# called VIRTUAL_ENV pointing to the location of the active virtual env.
# (This should be the case if using virtualenvwrapper)

PACKAGE_NAME="btvpython"
PROJECT_DIR=$(pwd)
BUILD_DIR="build"

# clear out existing package
mkdir -p ${BUILD_DIR}
rm -f "$BUILD_DIR/$PACKAGE_NAME.zip"

# package out python module and any dependencies installed in the virtual env
zip -r9 "$BUILD_DIR/$PACKAGE_NAME.zip" ${PACKAGE_NAME}
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" .
cd ${PROJECT_DIR}

