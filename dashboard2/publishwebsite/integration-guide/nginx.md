# Subdirectory publishing via nginx

As described on [their website](https://nginx.org/en/),

> nginx [engine x] is an HTTP and **reverse proxy** server, a mail proxy server, and a generic TCP/UDP proxy server

This makes it perfect for our purposes. We'll use a small subset of the features it provides to set up subdirectory publishing.

To get started, it's recommended to copy the settings provided in the Publishing wizard. These are partially project-specific. We'll use a project with the following details:

- Source domain: example.com
- Project code: `redacted`
- Translations exist for German
- We wish to publish them to example.com/de/
- Your white label is app.translationproxy.com

With these options set in the Publish wizard, we get the following configuration:

```
location ~* ^/(de) {
        resolver 8.8.8.8;

        set $xhost de-de-redacted.app.translationproxy.com;

        proxy_set_header X-TranslationProxy-Cache-Info   disable;
        proxy_set_header Server $xhost;
        proxy_ssl_name $xhost;
        proxy_set_header X-TranslationProxy-EnableDeepRoot true;
        proxy_set_header X-TranslationProxy-AllowRobots true;
        proxy_set_header X-TranslationProxy-ServingDomain $host;
        proxy_set_header Host $xhost;

        #old nginx
        #  proxy_pass $scheme://$xhost;
        #new nginx:
        proxy_pass $scheme://ghs.googlehosted.com;
    }
```

With these details on hand, we can get started. Note that this guide assumes that nginx is already installed on your Debian-based server and that you are familiar with its command line. Canonical has a well-written guide for Ubuntu servers available [here](https://ubuntu.com/tutorials/install-and-configure-nginx#2-installing-nginx).

Log into your server either as `root` or a user who can use `sudo`. If you aren't `root`, switch to that user via 

```
$ sudo su
```

**WARNING:** At this point, you have complete, *unrestricted* access to the server. It's very easy to break it. Don't run commands that you aren't certain will do what you need to.

If you have no reason not to do so, it's probably a good idea to update your server.

```
# apt update && apt upgrade -y
```

By default, the configuration file can be found at `/etc/nginx/nginx.conf`. We'll need to edit this file with our text editor of choice:

```
# nano /etc/nginx/nginx.conf
```

By default, the file looks something like this:

```
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}


#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
# 
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```

If you use this server to host websites too, not just as a reverse proxy then it will probably contain considerably more settings. In any case, scroll to the bottom and paste the configuration snippet that we provided. Save and exit.

**NOTE:** You can add further target languages by putting their code right below.

The configuration is in place, but nginx doesn't automatically switch them over. This ensures that you don't bring down your entire site by accidentally saving a syntax error. Verify that the file is correct.

```
# nginx -t
```

If no errors are printed, you can reload without dropping connections via 

```
# systemctl reload nginx
```

This ensures no downtime. With that, the nginx configuration is complete.

These instructions are up-to-date as of 24/02/2022.