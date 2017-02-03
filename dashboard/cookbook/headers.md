# HTTP Headers

## What are HTTP Headers?
HTTP header fields are components of the header section of request and response messages in the Hypertext Transfer Protocol (HTTP). They define the operating parameters of an HTTP transaction. The header fields are transmitted after the request or response line, which is the first line of a message. Header fields are colon-separated name-value pairs in clear-text string format, terminated by a carriage return (CR) and line feed (LF) character sequence. The end of the header section is indicated by an empty field, resulting in the transmission of two consecutive CR-LF pairs. ((Wikipedia)[https://en.wikipedia.org/wiki/List_of_HTTP_header_fields])

## Headers and the proxy
The Proxy strives to be as transparent when it comes to headers as possible. Therefore, we forward the majority of headers added to any incoming request, with a few exceptions where the presence of said header could cause undesirable operation in the original server.

Additionally, The Proxy also adds a few specialized headers both to requests to the remote server and responses to the client. The presence of these headers SHOULD NOT cause erroneous behavior in the server.  
Request headers contain additional information on the client viewing the site and the language being served. This can be used to provide customized content. Some Proxy-specific request headers are:

+ `X-TranslationProxy-Translating-To: ja-JP`: This gives the language of the translated version the client is browsing.
+ `X-TranslationProxy-Translating-Host: jp.eveonline.com`: This header contains the domain under which the Proxy is serving the translated site.
+ `X-TranslationProxy-Originating-IP: 192.168.168.192`: If enabled, this header contains the IP address of the requester, which may be hidden by CDNs and other proxies.
+ Future headers of the `X-TranslationProxy` containing other metadata
+ `User-Agent`: This header is somewhat special, in the sense that it's not specific to The Proxy, rather, it is sent by almost all browsers to identify themselves. The reason it finds a place in this article is that it can be used to identify Proxy-served requests. Google AppEngine modifies this header when sending requests, in a way that ensure no further tampering before the header reaches the original server, by adding `AppEngine-Google; (+http://code.google.com/appengine; appid: u~skawa-easyling)` - this can be used to whitelist the Proxy.

## HTTP Headers and Security
Due to its nature as a proxy, and the fact that Google URLFetch uses a diverse range of addresses allocated randomly, it is easy to see that proxied requests may be caught by Web Application Firewalls, Anti-DDOS software, or even security provider companies. When a project is launched, it is often a good idea to contact the client and have them notify any contracted security providers, or make the necessary changes to firewalls and block-lists.

The easiest way to identify proxied requests is to read the `User-Agent` header, and locate the above-mentioned pattern - the application ID is added by Google at the last possible moment, thus, it can be a trusted indicator (along with the other headers, if needed) that the request was initiated by the Proxy. Security providers can be advised that the appearance of these headers is normal and should not be construed as an attack/phishing attempt.
