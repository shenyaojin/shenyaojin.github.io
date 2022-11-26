---
layout: wiki
title: Timeshift
cate1: Linux
cate2: Backup
description: Timeshift is an application to make snaps of Linux.
keywords: Linux
type: 
link:
---

Timeshift is one of the best sync package for all Linux distributions. It is developed by **Tony George**, here is the [repo page](https://github.com/teejee2008/timeshift).

# Timeshift - Features

- Minimal setup
- Support for CLI and GUI modes
- Support for btrfs
- Support for rsync snapshots
- Multiple backup level options (hourly, daily, weekly, monthly, and boot)
- Cross-distro restore

# Timeshift - How to install

## Ubuntu & Debian

```sh
sudo add-apt-repository -y ppa:teejee2008/timeshift
sudo apt-get update
sudo apt-get install timeshift
```

## Fedora, CentOS, and RHEL

```shell
sudo dnf install timeshift
```

## Arch Linux

```sh
sudo pacman -S timeshift
```

# Timeshift - Usage

## Initial timeshift

1. open timeshift. Enter your user password for authentication. Enter it and hit **Authenticate**.
2. Choose the mode: **Rsync** or **Btrfs**. Here's an introduction about the difference between the two different modes.

> For the uninitiated, the Rsync option creates snapshots using rsync and hard links. Basically, Rsync snapshots contain only those files and directories that have been changed or modified—the rest of the (unchanged) files aren't backed up in the snapshot. Hence, it takes up less disk space. On the other hand, the Btrfs mode is ideal for users using one of the Linux distros that use the btrfs file system. Article from [here](https://www.makeuseof.com/use-timeshift-backup-and-restore-linux-snapshots/).

3. Choose the **Snapshot level**. Select whether to sync the file. 

## Usage from command line

Here I will only introduce command line to activate the timeshift. In most cases, we will only use timeshift from command line to recover the broken system. And another reason is using GUI is quite easy and there's no need to discuss it.

