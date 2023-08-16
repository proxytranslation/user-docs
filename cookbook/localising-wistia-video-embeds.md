# Localising Wistia video embeds

## What is Wistia
Wistia is a leading business video hosting platform. It specializes in creating and hosting marketing-oriented videos, with a particular focus on embedded videos playing on the website directly.

## Why you should localise videos
Basically for the same reason you're localising your website: increased reach by speaking to people in their native tongues.

Just like how you already use the Translation Proxy to translate your website, if your marketing team creates a localised version of your marketing videos, it would be prudent to replace the existing video on your translated website, so any foreign visitors are greeted with tailored materials speaking their language.

## How to localise embedded Wistia videos

Note that this guide assumes you have access to the proxy project so that you can configure the platform to make the necessary changes.

1. Open the website and go to the page where the original video is found.
1. Press **Ctrl-U** to open the source code (use **Line wrap** in Chrome).
1. Press **Ctrl-F** and find `wisita_async`. Here you’ll find an ID for the given video. It’ll look like `wistia_async_s0urcec1de0`. You’ll need this later.
1. Go to **SETTINGS -> Path prefix overrides** on the Dashboard. Click on the relevant path. This video is in the root in our case so you need to click on `/`.
1. If the video is on a page where nothing has been replaced yet, it is not added to the paths yet either. In such case click on the **ADD NEW** button, enter the URL and click on the **ADD NEW PATH** button. and then click on the now listed path.
1. Select **CONTENT SEARCH & REPLACE** and click on the **ADD NEW** button.
1. Enter `text/html.*` in the Content-types field. It is worth adding the `.*` to the end as the server might send other info as well.
1. Paste the code selected from the source code (`wistia_async_S0urceC0de`) to the **Search** field.
1. Paste the code of the new video (`wistia_async_C0deT0Repl4ce`) to the **Replace** field.
1. Leave the **Regexp** checkbox disabled.
1. The **Target languages** field is optional so you can leave it empty.
1. Click on the **ADD** button.
1. Click on the **SAVE ALL** button.
1. Go back to the website and enter `/?test=0` to the end of the URL. The URL is now changed by the query with something that probably does not change content served and if the translated page had been cached somewhere, it cannot be used to serve the content for us so the translated video should be displayed on the site (otherwise you would have to wait until all caches are cleared). You should see the replaced video now on the website.