How to set up mitmproxy
=======================
#### Step 1: make sure desired port is unused (8080)

#### Step 2: make sure iptables is configured with following code: (STILL A BIT UNSURE)
```bash
sudo iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner root --dport 80 -j REDIRECT --to-port 8080
```
    * redirects all traffic in port 80 to 8080 (where mitmproxy will listen)
    * is necessary, as mitmproxys transparent mode requires redirection of traffic and no direct traffic
    * apparently, doing this will only be useful if traffic is meant from local clients
    * ! --uid-owner root is to block infinite traffic from the same user. (I think only useful if testing locally)
    * might need to use PREROUTING option instead of OUTPUT for external clients

ChatpGPT says that this is needed for external source:
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```
    * apparently redirects incoming traffic
    * apparently used when your machine acts as a gateway or receives traffic from other devices

#### Step 3: run following code:
```bash
sudo mitmproxy --mode transparent -p 8080 -s mad_server.py
```
    * mitmproxy has to run in transparent mode because browser is unaware of the proxy
        * normally, the browser knows if mitmproxy is listening and this requires manual setup on the browser side
        * transparent mode goes under the assumption that the browser isn't aware of it listening (necessary for intercepting)
    * -s [script] tells mitmproxy which python script to use

Clean up (IMPORTANT!)
=====================
#### To see if the iptables rule still exists, run following code:
    ```bash
    sudo iptables -t nat -L -n -v --line-numbers
    ```
    * if any rules with the numbers 80 and 8080 are listed, you probably still have the mitmproxy setup
    * delete this if done with mitmproxy work

#### To delete the iptables rule (redirect from 80 to 8080), run following code:
    ```bash
    sudo iptables -t nat -D OUTPUT <line number of rule>
    ```

