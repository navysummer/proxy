from xiciproxy import XCproxy

xc = XCproxy()
gn = xc.gaoni()
print(gn)
pt = xc.putong()
print(pt)
http = xc.http()
print(http)
https = xc.https()
print(https)