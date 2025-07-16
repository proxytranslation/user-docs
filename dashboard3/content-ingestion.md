# Content Ingestion Setup

## Overview

**Content Ingestion** is the process through which new website content is discovered and forwarded to our translation service. This is managed by a lightweight **JavaScript script** injected into your website. The script observes changes and interactions with your site to detect new content that might require translation.

You have full control over **how** content is ingested. This guide will walk you through the available options and help you choose the method that best suits your workflow and translation needs.

## Best Practices & Recommendations

- **For tight editorial control:** Use **Manual Ingestion** with authenticated links.
- **For high-volume, fast-moving websites:** Use **Automatic Ingestion** and enable content review queues.

## Accessing the Content Ingestion Settings

![Content ingestion settings location](/img/dashboard3/content_opts_position.png)

To adjust your content ingestion settings:

1. Log in to your Dashboard.
2. Navigate to your project.
3. Go to **Settings > Content Ingestion**.
4. Choose your preferred ingestion mode from the available options.

## Ingestion Modes

![Content ingestion options](/img/dashboard3/content_options.png)

### Option 1: Disable Automatic Content Ingestion

**What it does:**  
Disables all automatic and manual content capturing. No new content will be ingested, even if users interact with the site.

**Use Cases:**
- You want to switch off ingestion of any new content, either via automatic, or manual ingestion through authenticated links.
- Your site is static or updated infrequently.

**Pros:**
- Maximum control
- Prevents accidental ingestion of irrelevant content

**Cons:**
- New content won't be ingested and translated.

> ⚠️ **Important:**  
> Keep in mind that updates to your website won't be detected in this mode, which may cause your translations to become outdated.

### Option 2: Manual Content Ingestion

**What it does:**  
New content is only captured when pages are accessed using **authenticated preview links** by authorized users. These links include a secure token that activates the ingestion script in **manual mode**.

**Use Cases:**
- You have a QA or content team responsible for validating new pages.
- You want to limit ingestion to tested and verified pages.

**Pros:**
- Secure and controlled ingestion
- Ensures only finalized content enters the translation queue

**Cons:**
- Requires someone to manually visit all new, or modified pages
- Not suitable for fast-changing or dynamic websites

### Option 3: Automatic Content Ingestion

**What it does:**  
New content is captured automatically whenever **any visitor** browses your website, including search engines, external users, or bots.

**Use Cases:**
- You want to automatically track and translate new or updated content
- Your site changes frequently
- You want a hands-off, high-coverage approach

**Pros:**
- Fully automated
- Ensures new content is captured quickly

**Cons:**
- May ingest **irrelevant or unwanted content**, such as:
  - Content from browser extensions (e.g., Grammarly, Google Translate)
  - 3rd-party translation overlays
  - Personalized user data shown to individuals

## Automatic Content Ingestion Source Options

![Automatic content ingestion options](/img/dashboard3/content_opts_automatic.png)

When enabling **Automatic Content Ingestion**, you can choose how content is captured:

- **From source language pages** *(Recommended)*  
  Ingests content from the **untranslated** version of your site.  
  Best for **dynamic websites** where new content appears in the original language first.

- **From translated pages**  
  Ingests content from the **already translated** version of your site.  
  Useful for **static websites**, but may accidentally capture **translated content** on dynamic sites.

## FAQ

**Can I switch ingestion modes later?**  
Yes, you can change ingestion settings at any time.

**Will disabling ingestion delete already captured content?**  
No, it only prevents new content from being captured. Existing content remains in the system.

**How can I avoid irrelevant content from browser extensions?**  
We recommend enabling **manual mode** to limit the amount of irrelevant content ingested.

## Troubleshooting

**Content is not being captured:**
- Make sure the ingestion script is properly injected on your live site.
- If using manual ingestion, confirm you're using a valid authenticated preview link.

**Unexpected content appears in translations:**
- Review your ingestion mode.
- Consider switching to manual ingestion for more control.