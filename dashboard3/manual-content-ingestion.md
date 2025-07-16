# Manual Content Ingestion Setup

## Overview

**Manual Content Ingestion** allows you to capture new content in a **controlled and secure way** by using **authenticated links**. When a user visits your site through one of these special links, the translation script will be temporarily enabled to ingest new content during that session.

This method gives you full control over what content gets picked up for translation and is especially useful when:

- You want to avoid unwanted ingestion from anonymous users or bots.
- You're working in a staging or QA environment.
- You're manually reviewing and publishing new content for translation.

## Best Practices

- **Use descriptive names** for your links (e.g., "Blog QA – Feb 2025").
- **Always prefer source language ingestion** for dynamic or regularly updated content.
- **Set short expiration periods** for one-time QA tasks or staging environments.

## Accessing Manual Ingestion Links

![Manual ingestion settings location](/img/dashboard3/manual_content_ingestion.png)

To manage your authenticated ingestion links:

1. Go to your **Dashboard**.
2. Navigate to your project.
3. Open **Settings > Content Ingestion > Manual Content Ingestion via Authenticated Links**.

You'll find a table listing all existing links.

### Table Fields:

![Manual ingestion table](/img/dashboard3/manual_ingestion_table.png)

- **Description** – A custom description for your link
- **Link** – The generated authenticated URL
- **Valid Until** – Expiration date of the link
- **Actions** – Options to **Edit** or **Delete** the link

## Creating a New Authenticated Link

![Create new authenticated link](/img/dashboard3/content_manual_link.png)

To generate a new link:

1. Click the **Generate New Link** button.
2. A modal will open where you can configure the link options.

### Modal Fields:

#### **Description** *(required)*
- A name to help you identify what the link is used for.

#### **Add New Content (Source)**
Choose how content will be captured during the session:

- **From source language pages** *(Recommended)*  
  Ingests content from the **untranslated** version of your site.  
  Best for **dynamic websites** where new content appears in the original language first.

- **From translated pages**  
  Ingests content from the **already translated** version of your site.  
  Useful for **static websites**, but may accidentally capture **translated content** on dynamic sites.

#### **Expires On**
- Select the date the link should expire.
- After this date, visiting the link will no longer trigger ingestion.

## Editing or Deleting Links

Under the **Actions** column of the table:

- Click **Edit** to reopen the modal and change the link's description, content source, or expiry.
- Click **Delete** to permanently remove the link.

## Usage Workflow

1. **Create a link** with appropriate settings for your use case
2. **Share the link** with your content team or QA personnel
3. **Visit pages** using the authenticated link to capture content
4. **Monitor captured content** in your translation workflow
5. **Delete or expire links** when no longer needed

## Security Considerations

- **Link expiration**: Always set appropriate expiration dates for your links
- **Access control**: Only share authenticated links with authorized personnel
- **Monitoring**: Regularly review and clean up unused or expired links
- **Content review**: Use manual ingestion to ensure only approved content enters translation

## Troubleshooting

**Link not working:**
- Check if the link has expired
- Verify you're using the complete URL including the authentication token
- Ensure the link was created for the correct project

**Content not being captured:**
- Confirm you're visiting pages through the authenticated link
- Check that the ingestion script is properly loaded on your site
- Verify the link settings match your content source requirements

**Need to extend a link:**
- Edit the existing link to update the expiration date
- Or create a new link with the same settings and a new expiration