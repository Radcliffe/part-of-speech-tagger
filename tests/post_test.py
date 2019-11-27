import http.client

conn = http.client.HTTPConnection("localhost", 8000)

payload = "text=The%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog."

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "localhost:8000",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "65",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("POST", "tag", payload, headers)

res = conn.getresponse()
data = res.read()
actual = data.decode('utf-8')
expected = '["DT", "JJ", "NN", "NN", "VBZ", "IN", "DT", "JJ", "NN"]'
assert actual == expected
print('Test passed.')