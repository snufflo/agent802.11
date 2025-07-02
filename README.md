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

#### [Wireshark](https://www.wireshark.org/)

#### [nmap](https://nmap.org/)

#### [Bettercap](https://www.bettercap.org/)

#### [mitmproxy](https://mitmproxy.org/)

#### [ARP Spoofing Tool](https://github.com/davidlares/arp-spoofing)

Script to perform man in the middle attack


What is ARP Spoofing?
=====================
![Diagram for arp spoofing](/images/arp_spoof_colored.drawio.jpg)
(Diagram demonstrating ARP poisoning in local network)

ARP Spoofing is the act of pretending to be another device by broadcasting a forged ARP packet.
    - This kind of ARP broadcast reply, which is not triggered by a request, is called **Gratituous ARP Reply**.
    - Arp spoofing is essentially done through gratituous ARP replies
    - Since ARP is a trust-based protocol, receiving ends would normally have to accept such replies, thus givin adversaries an advantage
If done successfully, an adversary is able to redirect packets to its own device. 
ARP Spoofing is usually done by 
1. deceiving the target endpoint device E that adversary T is the default gateway accesspoint A.
2. deceiving A that T is E
On succession, T becomes the man in the middle

What is SSL/TLS Stripping?
==========================
![Diagram for ssl_stripping](/images/ssl_stripping.drawio.jpg)
(Diagram demonstrating SSL/TLS Stripping through ARP poisoning)

SSL/TLS Stripping, in context of HTTPS connections, is the act of removing SSL/TLS encryption of a HTTPS connection.
If done successfully, an adversary is able to view full HTTP requests in plaintext.
Combined with the ARP poisoning attack, the adversary is able to modify and take full control over HTTP responses of requested servers.

What is HSTS?
=============
- **HTTP Strict Transport Security**, HSTS in short, is a web security policy mechanism that prevents browsers to access websites through HTTP.
- Browsers have an HSTS preloaded list of domain names, which will let the browser only access urls from that domain through HTTPS.
- The term "Strict-Transport-Security" is also to be found at most of the websites that enforce HTTPS connection as a header of their HTTPS response.
- Not all browsers will be preloaded in the browsers HSTS list on default. That is why there is a dynamic way to manage the HSTS link, which might expose the device for an initial HTTP request to the server. Detailed procedure:
    1. Browser tries to connect to a website via HTTP that is not HSTS preloaded.
        - This behaviour is unusual for modern browsers, as modern browsers will try a HTTPS connection for unknown websites first. More on this behaviour below.
    2. Browser gets a HTTP 301/308 redirect from server to their HTTPS link.
    3. Browser connects to the HTTPS link and gets (as an example) following response:
    ```http
        HTTP/1.1 200 OK
        Content-Type: text/html; charset=UTF-8
        Strict-Transport-Security: max-age=31536000; includeSubDomain; preload
        Content-Length: 3456
    ```
    4. After receiving the HSTS header, browser will append their HSTS list with the domain name.
    5. Next time the browser tries to visit the website, it will only allow HTTPS connections


Browser Behaviour
=================
1. If a website is HSTS preloaded, the browser will only accept HTTPS connection and won't fall back to HTTP towards that website
2. If a website is not HSTS preloaded, most modern browsers will first try 
    - Firefox: to establish a HTTP connection then follow the redirect to HTTPS link, if provided
    - Chrome, Safari: to establish a HTTPS connection through a TLS clienthello packet
    - This clienthello will contain a SNI (Server Name Indication), which indicates the domain name the browser is trying to access in plaintext (unless the browser uses ECH (Encrypted Client Hello), which is not so widely used as of 2025)
    - agent802.11 will try to extract the unencrypted SNI and check, whether or not the indicated domain sends a Strict-Transport-Security header. If the server responds with this header, it means that the server is likely to be HSTS preloaded
3. Depending on the browser, it will fall back to HTTP, if certain conditions are met:
    - website is not HSTS preloaded
    - browser encounts website that enforces Strict-Transport-Security the first time
    - HTTPS-only mode (if available) is turned off
- On Firefox, HTTPS-only mode is turned off by default.
    - This means that unless https is specifically typed in, firefox will first try to establish a HTTP connection
