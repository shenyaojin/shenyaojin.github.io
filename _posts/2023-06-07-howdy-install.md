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
$ cat /etc/pam.d/sddm

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
$ cat /etc/pam.d/kde
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
$ cat /etc/pam.d/sudo

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
$ cat /etc/pam.d/polkit-1

#%PAM-1.0
auth sufficient pam_unix.so try_first_pass likeauth nullok
auth sufficient /lib/security/pam_howdy.so
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
```

### 2. add IR sensor

First, check whether the IR sensor works.  [linux-enable-ir-emitter ](https://github.com/EmixamPP/linux-enable-ir-emitter)will help you with this problem. I'm sorry I couldn't help with this problem for I went through it easily. If your IR sensor works, go to next step: 

Second, scan your system to determine which camera you need to use. I recommend the [v4l-utils](https://archlinux.org/packages/?name=v4l-utils) package:

```shell
# from wiki
$ v4l2-ctl --list-devices
Integrated_Webcam_HD: Integrate (usb-0000:00:14.0-11):
        /dev/video0
        /dev/video1

EyeChip: Tobii Video (usb-0000:00:14.0-3.4.3):
        /dev/video4
        /dev/video5

HD Webcam C525 (usb-0000:00:14.0-3.4.4):
        /dev/video2
        /dev/video3
```

Generally, the "/dev/video2" would be a right choice. "/dev/video0" might work, but normally it doesn't offer a IR function, only camera is remained. 

Anyway, you need to note the path and add it to `/lib/security/howdy/config.ini`. Modify on line "device_path": 

```sh
$ cat /lib/security/howdy/config.ini | grep /dev
# Video devices are usually found in /dev/v4l/by-path/
device_path = /dev/video2
```

### 3. add your face 

Use the command: 

```sh
sudo howdy add
```

### 4. check the camera

Use command: 

```sh
sudo howdy test
```

It will drop a window with a camera capturing your face, and your IR camera should work. The green circle on your face means howdy could recognize your face. 

## Notes 

If some of the functions don't work, you need to change mode to howdy folder `path: /lib/security/howdy`. If you couldn't access to it, congratulations! You could use chmod command to fix it. 

```sh
sudo chmod -R 755 /lib/security/howdy
```



