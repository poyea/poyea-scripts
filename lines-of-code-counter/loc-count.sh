#!/bin/sh

set -e
cd "$(dirname "$(pwd)")"

if [ ! -z $1 ] 
then 
    case $1 in
    "cpp")
        echo "Counting $1..."
        find . \( -name \*.cpp \
                -o -name \*.c \
                -o -name \*.h \
                -o -name \*.hpp \
                -o -name \*.cc \
                -o -name \*.CPP \
                -o -name \*.C \
                -o -name \*.cxx \
                -o -name \*.c++ \
                \) \
                -not -path ./thirdparty/\* \
                -not -path ./build/\* \
                | xargs wc -l
        ;;
    *)
        echo "Hmm... What did you type???"
        ;;
    esac
else
    echo "Counting every possible thing..."
    find . -type f | xargs wc -l
fi
