---
layout: post
title: 【CN】How to migrate Linux to another partition/disk
categories: [Linux, Computer Science]
description: some word here
keywords: Linux, Backup
---

这篇文章简单讲一下我怎么把系统完整地迁移到另一块硬盘上。

# 准备

1. 两块USB移动盘
2. [Manjaro Linux(或是别的发行版)的镜像](https://manjaro.org/download/)
3. [Clonezilla的镜像](https://clonezilla.org/downloads.php)
4. 原系统盘/分区(Linux系统)，目标硬盘（应比原分区大）

# 刻录镜像

## 1. 刻录Linux镜像

使用dd命令或是gnome桌面自带的工具刻录镜像。

使用dd命令如下：

```sh
dd if=boot.img(镜像名字) of=/dev/fd0(分区名字) bs=1440k 
```

## 2. 刻录Clonezilla镜像

使用dd命令或是gnome桌面自带的工具刻录镜像。使用的dd命令和上面一样。



# 为目标硬盘分区

利用系统自带的工具(KDE partition manager)或是[fdisk](http://c.biancheng.net/view/891.html)命令为硬盘分区。

注意：

1. 要为硬盘分两个区（EFI系统）。一个是efi分区，另一个是系统分区。格式和原来的硬盘保持一样，且大小应大于等于原来的分区大小。
2. efi分区应该在系统分区之前。

# 利用Clonezilla复制分区

用USB Live启动Clonezilla。首先复制EFI分区：

选项依次为 Enter clonezilla-device2device-expert mode-part to local part-origin partition-destination partition。

然后有几个高级参数要注意：

1. 选中重装grub (-g)
2. 自动修复原文件系统(-fsck-y)
3. 不要关机(-pa choose)
4. 不要产生分区的分配表(-k) <- **很重要**

用同样的选项复制主分区。

# 修复grub

如果上一步重装grub失败（因为各个发行版grub的重装都不太一样，所以clonezilla可能会失败），那么需要用Linux Live USB进入系统，为它重装一次grub。具体的步骤可以参照[这篇文章](https://wiki.manjaro.org/index.php/GRUB/Restore_the_GRUB_Bootloader)或是自己发行版的论坛。

# 解除安全模式

Linux处于安全性的考虑，在换盘以后会强制进安全模式..?再次启动时需要输入root管理员的密码。用startx进入桌面(KDE)，然后接着去修改分区表。

# 分区表

```sh
/etc/fstab
# <device>                                <dir> <type> <options> <dump> <fsck>
UUID=0a3407de-014b-458b-b5c1-848e92a327a3 /     ext4   defaults  0      1
UUID=f9fe0b69-a280-415d-a03a-a32752370dee none  swap   defaults  0      0
UUID=b411dc99-f0a0-4c87-9e05-184977be8539 /home ext4   defaults  0      2
```

修改分区表UUID为现在使用硬盘的UUID就结束了。查看方法：blkid。