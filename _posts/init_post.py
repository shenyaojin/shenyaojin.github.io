import sys 
title = str(sys.argv[2])
filename = str(sys.argv[1])
with open(filename, 'w') as file: 
    file.writelines('---\n')
    file.writelines('layout: post\n')
    file.write('title: ')
    file.write(title)
    file.write('\n')
    file.write('categories: [Linux]\ndescription: \nkeywords: \nmathjax: true\n---\n')