---
layout: post
title: Check Linux system info
categories: [Computer Science]
description: Use command line to get the information of your linux distribution, including your CPU/Memory info.
keywords: keyword1, keyword2

---

# CPU Info

```sh
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
```

The output will be: 

> 12  Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz



```sh
getconf LONG_BIT
```

Output: 

> 64

That means my machine runs at 64 BIT.

# Mobo Info

```
dmidecode |grep -A16 "System Information$" 
```

You could check the maximum capacity of the memory, with this command: 

```sh
sudo dmidecode | grep -P 'Maximum\s+Capacity'
```

Output: 

```
Maximum Capacity: 64 GB
```

# Memory Info

```sh
cat /proc/meminfo 
```

The output: 
```
MemTotal:       16232108 kB
MemFree:          393568 kB
MemAvailable:    8964960 kB
Buffers:         1970112 kB
Cached:          6193428 kB
SwapCached:           28 kB
Active:          4321888 kB
Inactive:        8006376 kB
Active(anon):      60988 kB
Inactive(anon):  5644016 kB
Active(file):    4260900 kB
Inactive(file):  2362360 kB
Unevictable:      630436 kB
Mlocked:             544 kB
SwapTotal:      17855316 kB
SwapFree:       17851732 kB
Dirty:                24 kB
Writeback:             0 kB
AnonPages:       4786284 kB
Mapped:          2101992 kB
Shmem:           1540280 kB
KReclaimable:    2289608 kB
Slab:            2534456 kB
SReclaimable:    2289608 kB
SUnreclaim:       244848 kB
KernelStack:       28976 kB
PageTables:        84044 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    25971368 kB
Committed_AS:   23067276 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      126420 kB
VmallocChunk:          0 kB
Percpu:            12032 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:      806196 kB
DirectMap2M:    15820800 kB
DirectMap1G:           0 kB
```
# Distribution Info

```sh
uname -a
```

Output: 

> Linux genesis 5.15.65-1-MANJARO #1 SMP PREEMPT Mon Sep 5 10:15:47 UTC 2022 x86_64 GN
> U/Linux 



Or 

```sh
cat /etc/issue | grep Linux
```

Output: 

> Manjaro **Linux** \r  (\n) (\l)
