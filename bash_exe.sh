#!/bin/bash


NUM_FILES=$1

createfiles() {
  for i in `seq 1 $NUM_FILES`; do
      mkdir mydir$i;
      touch mydir$i/myfile$i.txt;
      echo "hello $i world" > mydir$i/myfile$i.txt;
  done;
}

catfiles() {
  for i in `seq 1 $NUM_FILES`; do
      cat mydir$i/myfile$i.txt;
  done;
}


rmdirs() {
  for i in `seq 1 $NUM_FILES`; do
      rm -rf mydir*;
  done;
}



createfiles
catfiles
rmdirs
