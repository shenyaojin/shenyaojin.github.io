---
layout: post
title: Connect to Midland server in Linux Client (Ubuntu)
categories: [Computer Science]
description: Introduce how to connect to RCP server on newest Linux system like ubuntu.
keywords: fix bug
---

# Why need this article?
I was told to connect the RCP server off campus using the application called global protection. But I faced problem called "SSL shakehand failed" on my machine. I checked the error log and could assure that it's caused by the version of SSL. Before I upgrade my system to Ubuntu 22.04 LTS, the libqt5network uses **SSL 1.0**. But after that they developers update SSL to **SSL 3.0** which is not supported by Mines.

> That means the package provided by *Mines* doesn't work in Ubuntu 22.04 LTS or newer version.

# Machine information
Note that my machine is based on ubuntu 22.04 LTS and I modified some of the libs on it. 

# When it works?
Anyway, this article works while your machine is Ubuntu 22.04 LTS or newer. Only fit for Debian family, won't work in Redhat or Arch.

# Commands
I've tested several alternatives from the Internet and choose the best one. 

Here are the commands: 

```bash
sudo add-apt-repository ppa:yuezk/globalprotect-openconnect
```

then update the package: 
```bash
sudo apt update
sudo apt upgrade
```

finally install the package:
```bash
sudo apt install globalprotect-openconnect 
```

This version works. Tested.