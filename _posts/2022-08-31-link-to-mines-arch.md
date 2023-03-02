---
layout: post
title: Connect to Midland server in Linux Client (Archlinux)
categories: [Programming Skills]
description: Introduce how to connect to RCP server on newest Linux system like arch.
keywords: fix bug
---

# This time is arch linux

I deleted my ubuntu by ... some kind of ... accident. Then I turned back to arch. I must say archlinux is masterpiece, and when I tried to connect to midland server, I met another problem, the pacman is different from apt, I could add a private repo. But thanks to aur, we could also install the vpn client on archlinux.

# Commands
I've tested several alternatives from the Internet and choose the best one. 

Here are the commands(arch&zsh): 

> Update the package: 

```bash
sudo pacman -Syyu
```

> install from git, so if you have not installed git, go through these commands: 
* Install git
```bash
sudo pacman -S git
```

* clone globalprotect from AUR 
```bash
git clone https://aur.archlinux.org/globalprotect-openconnect-git.git
```

* build the package
```bash
build -rsi
```

If you have yay, then it will be much easier:
```bash
yay globalprotect-openconnect-git
```

Then you could enjoy the network.