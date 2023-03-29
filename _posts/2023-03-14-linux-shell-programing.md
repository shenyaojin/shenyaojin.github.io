---
layout: post
title: 【CN】Linux shell programming notes 1
categories: [Linux, Computer Science]
description: My Shell programming learning notes. 
keywords: Linux, Shell
---

# Shell Programming Notes 1

## 写在前面

之前上课学过现在全忘光了。所以对着书再学一遍。

I have bring all I learnt to my tutor. I need to learn it again.

## Using multiple commands 

Using ";"(or "&&") we could seperate multiple commands: 

```sh
date ; who
```

The output: 

```sh
Wed Mar 15 07:57:57 PM CST 2023
shenyao  tty1         2023-03-15 15:00 (:0)
shenyao  pts/0        2023-03-15 15:00 (:0)
shenyao  pts/1        2023-03-15 15:01 (:0)
shenyao  pts/2        2023-03-15 19:50 (:0)
shenyao  pts/3        2023-03-15 15:42 (:0)
```

## Using echo

format: echo + string

we do need to use ` ""` outside of the string, however, while the string itself has `'` we need to use `"` 

. The same as `"` situation.

```sh
echo using echo
```

Output:

```sh
using echo
```



And with `'`:

```sh
echo "Let's do it"
```

Output:

```sh
Let's do it
```



### Output in the same line:

use the -n parameter. Here is an example: 

```sh 
cat test1.sh
```

Output: 

```sh
#!/bin/bash
#

echo -n "Today's time is:"
date
echo "The users's are:"
who
```

Run the script, we have: 

```sh
Today's time is:Wed Mar 15 08:07:03 PM CST 2023
The users's are:
shenyao  tty1         2023-03-15 15:00 (:0)
shenyao  pts/0        2023-03-15 15:00 (:0)
shenyao  pts/1        2023-03-15 15:01 (:0)
shenyao  pts/2        2023-03-15 19:50 (:0)
shenyao  pts/3        2023-03-15 15:42 (:0)
```

## Using Variables

### Environment Variables

shell has a set of environment varsiables. It records the name of system, or who usr ID, home folder path, etc. Use `Set` to get the list of environment variables: 

```sh
set
```

 Since I used p9k the output is really at a mess...

### User Variables

We could also use user variables to store the data. Use "$" to quote the variable: 

```sh
a=1
$a
```

Output:

```
1
```

## Replace the command

We could use "`" or ""$()" to pass value from command output to variables: 

```sh
testing=$(date)
```

Or: 

```sh
testing=`date`
```

Then we have: 

```sh
echo "the time and date are" $testing
```

Output:

```sh
the time and date are Wed Mar 15 08:41:10 PM CST 2023
```



Let's see another example: 

```sh
today=$(date +%y%m%d)
ls /usr/bin -al > $today.log
```

It will generate another file and we'll get a new file, recording the output of `ls /usr/bin -al`.



## Redirection

### Output redirection

### Input redirection



