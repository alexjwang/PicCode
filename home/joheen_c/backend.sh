#!/bin/bash
gcloud ml vision detect-document "/home/alexwang3150/img.jpg" &> "/home/joheen_c/text.txt"
python /home/joheen_c/createc.py
gcc -o /home/joheen_c/main /home/joheen_c/code.c &> /home/joheen_c/error.txt
/home/joheen_c/main &> /home/joheen_c/out.txt
