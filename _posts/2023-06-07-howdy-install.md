---
layout: post
title: How to configure Howdy on your machine?
categories: [Linux]
description: Give the method to configure your howdy, which is a program based on face recognition.
keywords: howdy, configure
mathjax: true
---

## Introduction to Howdy

[Howdy](https://github.com/boltgolt/howdy) is a program that imitates Windows Hello on Linux. It uses a computer's IR sensors and camera to verify a user's face. It could be used to replace enter password to get super user privilege or perform screen unlock.

I'll show the configuration on my PC(ROG Zephyrus G14, 2022). 

## Installation

[Install](https://wiki.archlinux.org/title/Install) the [howdy](https://aur.archlinux.org/packages/howdy/)$$^{AUR}$$ package. (From Arch wiki)



## Configuration

Normally, you need to add two lines to activate howdy.

The first line is: 

```sh
auth sufficient pam_unix.so try_first_pass likeauth nullok # <-- add lines here
```

After this line is added, you could either use face or your password to login. Remember to tap the enter if you need to use face recognition. 

The second line is: 

```shell
auth sufficient /lib/security/pam_howdy.so # <-- add lines here
```

This line adds the method to use face recognition. If your howdy version is too old, you should try another line: 

```sh
auth sufficient pam_python.so /lib/security/howdy/pam.py
```

If you don't have pam_howdy.so in /lib/security/, then use the alternative version. Otherwise, keep your configuration same as mine.

### 1. set up PAM files

I'll give a few examples to set up PAM files.

* unlock SDDM:

```shell
: /etc/pam.d/sddm

# Add face recognition
auth sufficient pam_unix.so try_first_pass likeauth nullok # <-- add lines here
auth sufficient /lib/security/pam_howdy.so # <-- add lines here

auth            include         system-login
auth            optional        pam_kwallet5.so
account         include         system-login
password        include         system-login
session         include         system-login
session         optional        pam_kwallet5.so auto_start

```

* unlock KDE locker & other locker related to your DE: 

```sh
: /etc/pam.d/kde
#%PAM-1.0
auth sufficient pam_unix.so try_first_pass likeauth nullok
auth sufficient /lib/security/pam_howdy.so
auth            include         system-login

account         include         system-login

password        include         system-login

session         include         system-login
```

* unlock super user privilege

``` sh
: /etc/pam.d/sudo

#%PAM-1.0
# Add face recognization
auth sufficient pam_unix.so try_first_pass likeauth nullok
auth sufficient /lib/security/pam_howdy.so
auth            include         system-auth
account         include         system-auth
session         include         system-auth
```

* unlock PAMAC or other GUI you need to enter password: 

```sh
: /etc/pam.d/polkit-1

#%PAM-1.0
auth sufficient pam_unix.so try_first_pass likeauth nullok
auth sufficient /lib/security/pam_howdy.so
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
```

### 2. add IR sensor

