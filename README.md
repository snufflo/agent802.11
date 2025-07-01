WARNING
=======
This project is developed for EDUCATIONAL PURPOSES ONLY.
We DO NOT condone use of this project other than educationl purposes.
We are not responsible for any consequences through your use of this project.

Internet and Network Security project
=====================================

### Project idea

Use ARP poisoning to inject malice files when the user downloads a file.
Our setup will discover if someone downlaods a file, and instead our file is downloaded

#### Road map

- [x] Manage ARP spoofing
- [x] Attempt downgrade to HTTP connection
- [x] Listening to downloads and what files
- [ ] Replace downloaded file with our file

### Procedure

1) Be in the same local network of the target device
2) Recon ip of target through `nmap`
3) Attempt ARP Poisoning through `bettercap`
4) Attempt SSL/TLS Stripping and modify HTTP requests through `mitmproxy`

### Useful Commands for troubleshooting and further procedures

```
# show arp
arp -a

# delete arp
arp -d -a
```

### Tools

#### [Wireshakr](https://www.wireshark.org/)

#### [nmap](https://nmap.org/)

#### [Bettercap](https://www.bettercap.org/)

#### [mitmproxy](https://mitmproxy.org/)

#### [ARP Spoofing Tool](https://github.com/davidlares/arp-spoofing)

Script to perform man in the middle attack
