a script that print the content of files on directory and subdirectories on it
on makrdown output file each file will be splited to code section
the header of the section will be the name of the file
and the code content will be the content of file , code highlight will be file extension
## Why ?
most of the time I use notion to store my notes so on each time I need to run ``cat example.c `` to get content
and print it on notion code so  making that script makes my life easier
the script takes three arguments
1. dir
2. extensions seperated by ,
3. output file name
```sh
python3 main.py ~/codediary c,cpp,py code.md
```




