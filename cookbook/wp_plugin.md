# Easyling WordPress Plugin

## 1\. Overview

The Easyling WordPress plugin connects a WordPress site to an Easyling project and publishes translated versions of the site in **subdirectories** of the existing domain:

```
https://example.com/          → original site (served by WordPress as usual)
https://example.com/es/       → Spanish
https://example.com/fr-be/    → Belgian French
```

It is designed for hosting environments where you cannot add DNS records per language or custom reverse-proxy / CDN routing rules (e.g. managed WordPress hosting such as WP Engine). Routing happens **inside WordPress**: the plugin recognizes the language prefix, fetches the page for that language from Easyling, and returns it to the visitor.

The plugin does not duplicate content and does not write translations into the WordPress database. Its only stored data is its own settings (the `easyling` option) and a short-lived cache of the project configuration.

## 2\. Translation engines (publishing modes)

The plugin supports both Easyling engines. The **Easyling publishing mode** setting selects which one is used, and it must match the publishing method configured in the Easyling project.

|  | JavaScript (JS proxy) | Translation Proxy |
| :---- | :---- | :---- |
| Setting value | `js` (default) | `proxy` |
| Upstream host for translated pages | `{locale}-{projectCode}-j.{location}` | `{locale}-{projectCode}.{location}` (e.g. `app.easyling.co` / `eu.easyling.com`) |
| Where text is translated | In the browser, by the Easyling translation script inserted into the page | On the Easyling server; finished translated HTML is returned |
| Script added to every page | `stub.js` (language selector, hreflang, client-side logic) | `languageDropdown.js` (language selector) |
| hreflang / canonical | Added automatically | Not added; existing tags in your theme are kept unchanged |
| prerender.io support for bots | Yes (optional token) | Not used |
| Floating language selector override | Yes | No |

## 3\. How routing works

Under normal WordPress behavior, a URL like `/es/about/` is treated as a request for content at the path `es/about`. Unless you have actually created a page or rewrite rule for that path, WordPress will usually respond with a 404 Not Found. 

The plugin hooks into WordPress very early, before WordPress resolves the URL to a post or page. That way, paths such as `/es/about/` are served as translated pages instead of being treated as missing content. 

`/es/about/` is not meant to be a separate WordPress page you create in the admin. It is a translation URL handled by the plugin and Easyling. That is why visitors see the translated content instead of a “page not found” error. 

### 3.1 Language detection

On load, the plugin downloads the project configuration from

```
https://{location}/client/{projectCode}/0/stub.json?deployed=true
```

including the target language from each language's publishing path configured in Easyling, e.g. `{ "es": "es-ES", "fr-be": "fr-BE" }`. A request is treated as translated if its path starts with one of these prefixes (`/es`, `/es/…`, `/es?…`; case-insensitive).

### 3.2 Request lifecycle

Step by step:

1. **Guards.** Nothing happens if the project code is empty, the plugin status is *Disabled*, or the project configuration cannot be loaded.  
2. **Admin and system pages.**  
   - `/es/wp-admin/…` always gets a 302 redirect to `/wp-admin/…`.  
   - `/es/wp-login.php` gets a 302 redirect to `/wp-login.php` when *Redirect system pages* is on (the default).  
   - Requests inside wp-admin are never processed.  
3. **Front-end script.** On every front-end page (original and translated) the plugin enqueues the engine script. It is printed with `defer` and `data-cfasync="false"`, so Cloudflare Rocket Loader and WP Rocket do not delay or rewrite it.  
4. **Requests coming from Easyling** (identified by the `X-TranslationProxy-Translating-To` header) are served by WordPress as normal original-language pages. This is how Easyling reads your content.  
   - The WordPress admin bar is wrapped in `<div translate="no">`.  
   - The login page is wrapped the same way, unless *Translate login page* is enabled.  
5. **No language prefix.** The request is served by WordPress as usual.  
6. **Bots (JS mode with a prerender.io token).** Requests whose User-Agent matches a known crawler (Googlebot, Bingbot, social preview bots, etc.), are fetched from `service.prerender.io`. Static assets are excluded. When prerender.io renders the page, the plugin serves it the original page with the translation script, so the result is the fully translated, JavaScript-rendered HTML.  
7. **Everything else.** The request is forwarded to Easyling:  
     
   - Method: POST, PUT and DELETE are forwarded with their bodies, so forms on translated pages keep working. For GET, the plugin does not forward a request body and removes body-related headers.   
       
   - Headers: the visitor's request headers are forwarded, including cookies and User-Agent. Added headers: `Host: {upstream host}`, `Origin: {your host}`, `X-TranslationProxy-ServingDomain: {your host}`, `X-TranslationProxy-EnableDeepRoot: true`, `X-TranslationProxy-AllowRobots: true`, `X-TranslationProxy-Cache-Info: disable`.  
       
   - Redirects are not followed, so Easyling redirects reach the visitor unchanged.  
       
   - The response headers are copied to the visitor, except `Content-Encoding` (the web server re-encodes) and `Server`. The body is printed and the request ends with `exit`. No theme or other plugin code runs for that request after this point.

### 3.3 Subdirectory publishing vs. query parameter

*Subdirectory publishing* must be on for the `/es/` URLs above. When it is off, languages are selected with a query parameter on the original URLs. Translation then happens entirely in the browser, and the plugin proxies nothing.

## 4\. Caching

### 4.1 Plugin-internal cache

| Key | Content | Lifetime |
| :---- | :---- | :---- |
| `easyling_project_settings` | project configuration (languages, paths) | 10 minutes |
| `easyling_project_settings_fallback` | last successfully loaded configuration | no expiry; used if Easyling is unreachable |
| `raw_stub_json` | raw response, shown in debug info | — |

These are stored as WordPress transients. If the `ENABLE_CACHE` constant is defined, they go to the WordPress object cache instead.

Changes to languages or paths in Easyling reach the site within 10 minutes. Opening the plugin settings page refreshes the cache immediately.

### 4.2 Page caches (WP Engine, WP Rocket, Varnish, CDN)

- Page caches store responses per URL, so `/about/` and `/es/about/` are separate cache entries. Source and translated pages do not get mixed up.  
- A cached translated page is served without reaching PHP or Easyling.  
  - Translation Proxy mode: published translation changes appear after the page cache expires or is purged.  
  - JS mode: the translation is loaded by the browser, so cached HTML matters less for text changes.  
  - In both modes, purge the host cache after publishing important changes.  
- Cache headers (`Cache-Control`, etc.) returned by Easyling are passed through, and your page cache may honor them.  
- **prerender.io \+ page cache:** bot detection runs in PHP. If the page cache does not separate bots from human visitors, whichever version is cached first (prerendered or regular) can be served to both.  
- Logged-in users usually bypass page caches. The admin bar is never translated.

## 5\. Setup

### 5.1 In Easyling

1. Create the project and add the target languages.  
2. Choose **subdirectory publishing** and set the publishing path for every language (e.g. `https://example.com/es/`). The plugin shows an error for any language without a path.  
3. JS mode: **publish** each language. Unpublished languages are flagged in the plugin and not served.  
4. Translation Proxy mode: make sure the languages are published for the serving domain.  
5. Optional: configure the language selector appearance, SEO tags (hreflang/canonical), and path translation.

Note: after publishing, the language path prefixes are added to the project's crawl exclusion rules, so Easyling does not crawl its own translated pages.

### 5.2 In WordPress

1. Install and activate **Easyling** from *Plugins → Add New*. Deactivate other multilingual plugins first.  
2. Open *Easyling* in the admin menu and enter:

| Setting | Values | Notes |
| :---- | :---- | :---- |
| Status | Enabled / Disabled | Disabled \= kill switch, no scripts, no routing |
| Easyling project code | e.g. `a1b2c3` | Required |
| Languages | read-only | Flags \+ status (green \= OK, red \= missing path / not published). Click to open the translated URL |
| Easyling location | `app.easyling.com` (US), `eu.easyling.com` (EU), Other | Must match your account. "Login" opens the project settings |
| Easyling publishing mode | JavaScript / Translation Proxy | Must match the Easyling project |
| Floating language selector | Default / Hide / Show | Overrides the project setting (JS mode) |
| Redirect system pages | on (default) | `/es/wp-login.php` → `/wp-login.php` |
| Subdirectory publishing | on (default) | \- |
| Translate login page | off (default) | Allow the WordPress login page to be translated |
| prerender.io token | API key | Optional, JS mode only |

3. Click **Save Changes**, then **Test connection**.  
4. Add a language selector.

### 5.3 Hosting / DNS / CDN

- No additional DNS records, subdomains, or SSL certificates are needed. Because translations are served from subdirectories, the main domain's existing certificate (e.g., [www\.example.com](http://www.example.com)) automatically covers all translated paths (such as /es/...).  
- The host must allow outgoing HTTPS requests from PHP to `*.easyling.com`.  
- If a CDN or security layer sits in front of WordPress, it must pass `/es/…` requests through to PHP. It must not block the Easyling fetcher (requests carrying `X-TranslationProxy-*` headers).

## 6\. Language selector

All options render the same placeholder. The Easyling script turns it into the language dropdown, with links to the current page in each language:

```
<span class="el-dropdown"></span>
```

| Method | How |
| :---- | :---- |
| Floating selector | Rendered by the Easyling script; visibility set in Easyling or by the plugin's *Floating language selector* setting |
| Shortcode | `[easyling_language_selector]` |
| Block | *Easyling Language Selector* (Widgets category) in the block editor |
| Widget | *Appearance → Widgets → Easyling Language Selector* |
| Menu item | *Appearance → Menus → Easyling → EL Language Selector* (also in the Customizer) |

Custom selector: link to `/{prefix}{same path}`, e.g. `/es/about/`. If path translation is configured in Easyling, apply the same mapping.

## 7\. SEO

- **hreflang / canonical.** The plugin itself outputs none.  
  - JS mode: Easyling inserts `<link rel="alternate" hreflang="…">` for all languages plus `x-default`, and a language-specific canonical, into the translated HTML on the server side. The script on the original pages adds the same tags in the browser. This is controlled in the project's SEO tag settings.  
  - Translation Proxy mode: Easyling does not insert hreflang tags. Existing hreflang links in your HTML are preserved unchanged. Add them in your theme or SEO plugin if needed.  
- **Crawlers.** `X-TranslationProxy-AllowRobots: true` is sent, so translated pages are indexable. In JS mode, use prerender.io to serve fully rendered HTML to bots that do not execute JavaScript.  
- `<html lang>` is set to the target language on translated pages (JS mode).

## 8\. Troubleshooting

- **Test connection** requests the first configured language over HTTPS (e.g. `https://es-es-{code}-j.app.easyling.com/es/`). It shows the request URL, headers, status and body if the response is not `200`.  
- **Show debug information** (bottom of the settings page) shows the project configuration, the plugin settings, and the raw `stub.json`. Include it in support requests.

## 9\. Limitations and notes

- The plugin must load on every front-end request. Must-use plugins or security tools that block outgoing requests will prevent translation.  
- The visitor's request headers, including cookies, are forwarded to Easyling for translated pages.  
- No uninstall cleanup: the `easyling` option and transients remain after deletion.

## 10\. FAQ

**Which engine does the plugin use?** Either. You choose it with *Easyling publishing mode*, and it must match your Easyling project.

**Do we need to add hreflang ourselves?** In JS mode, no: Easyling adds them. In Translation Proxy mode, yes: add them in the theme or an SEO plugin.

**Does it work with WP Engine caching?** Yes. Pages are cached per URL, so languages do not mix. Purge the cache after publishing translation changes, and see §4.2 if you use prerender.io.

**Is any setup needed beyond the project code?** Yes. Set the language paths and publish the languages in Easyling, select the matching location and publishing mode in the plugin, add a language selector, and run Test connection.

**Is the plugin maintained?** Yes. It's in production, we actively fix any issues reported.