# ContentGuard Configuration

## Overview

**ContentGuard is our advanced content classification and filtering system**, designed to keep your translation project efficient, accurate, and safe. By smartly screening incoming content, ContentGuard prevents irrelevant material, errors, or even potential data leaks from entering your translation flow—**ensuring only legitimate, high-quality content is processed.**

ContentGuard is both powerful and flexible, giving you dynamic control over what gets ingested and reviewed. It operates behind the scenes, but you're always in control of its key settings right from your Dashboard.

## Why Use ContentGuard?

ContentGuard helps you:

- **Prevent unwanted content** from being translated
- **Reduce the risk of data leaks** or accidental ingestion of private or irrelevant material
- **Save time** by ensuring only authentic, worthwhile content is processed
- **Maintain high translation quality** through content review and filtering

## How ContentGuard Works

When new content is detected, ContentGuard evaluates it in real time. Using smart algorithms and statistical analysis, it checks if the content is legitimate and appropriate for translation. Based on your chosen settings, content that doesn't meet quality standards can be:

- **Automatically Approved** (if entirely trustworthy)
- **Marked as Pending for Review** (if unsure)
- **Excluded** from translation (if considered irrelevant or spurious)

All of this helps protect your project from accidental ingestion of bogus or sensitive content, especially useful if you're working in an environment with dynamic or user-generated content.

## Customizing ContentGuard Settings

> **Important:** Before you can enable ContentGuard settings, please contact our support team. Send them your project code by including the URL of your dashboard link. Our support team will need to adjust a few settings in your project before you can proceed.

![ContentGuard getting started](/img/dashboard3/getting_started.png)

To enable ContentGuard settings after support has made the necessary adjustments:

1. Go to your **Dashboard**.
2. Navigate to your project.
3. Open **Settings > ContentGuard Configuration > Enable ContentGuard**

You can tailor ContentGuard's behavior according to your needs in the project Dashboard. Two main settings are available:

### 1. Language Detection

![Language detection settings](/img/dashboard3/language_detection.png)

- **Enable Language Detection:** This option filters content by language, ensuring only those in your approved list are processed.
  - Useful for multi-language sites or when you need to exclude unexpected languages.
  - Note: Selecting this option may lead to additional costs.
  - This feature requires a machine translator integrated with your project. If not available, the setting will be inactive.

### 2. Strictness Level Adjustment

![Strictness level settings](/img/dashboard3/strictness_level.png)

- **Strictness Slider:** Adjust how rigidly ContentGuard decides whether content is approved, flagged for review, or excluded.
  - **More Strict:** Less content is automatically accepted; more entries require a human review.
  - **Less Strict:** More content flows through automatically; fewer manual reviews.
  - **Fine-tune the slider** as needed to match your workflow and risk appetite.

## Best Practices

- Start with a moderately strict setting and fine-tune from there, based on the volume and type of content typically ingested.
- If you support global audiences, carefully select which languages to allow.
- Regularly check for **Pending Review** entries to maintain high translation quality and catch any edge cases.

## Troubleshooting & FAQ

**Q: Why is some content now "Pending Review" or "Excluded"?**  
A: ContentGuard detected that these items might not match your rules (due to language, content type, or statistical analysis). Review them to approve or permanently exclude as needed.

**Q: Can I change settings later?**  
A: Yes, you can adjust ContentGuard's language detection and strictness at any time—these updates take effect immediately.

**Q: What if ContentGuard is too strict (or too lenient)?**  
A: Return to the slider and adjust to increase or decrease the strictness level to best fit your content flow.

**Q: Does enabling language detection add costs?**  
A: Possibly. If enabled, machine translation or detection services may generate additional charges. Check with your account manager or billing contact for specifics.

## Content Review Process

When ContentGuard flags content for review:

1. **Navigate to Workbench**
2. **Select the Show pending entries** option to view all items
4. **Review flagged content** to determine if it should be:
   - Approved for translation
   - Excluded permanently
5. **Take action** to approve or exclude content
6. **Monitor patterns** to adjust ContentGuard settings if needed

If you would like to review excluded content:

1. **Navigate to Workbench**
2. **Choose a specific page** you wish to review, **or select the All entries** option to view all items
3. **Open the Workflow filter menu,** and enable the **Show excluded entries** option to include excluded items in your view
4. **Review the content** to determine if it should be:
   - Approved for translation
   - Marked as Pending
   - Excluded permanently
5. **Take action** to approve, mark as Pending, or keep it excluded
6. **Monitor patterns** to adjust ContentGuard settings if needed

## Integration with Content Ingestion

ContentGuard works seamlessly with both automatic and manual content ingestion:

- **Automatic ingestion:** ContentGuard filters all automatically captured content
- **Manual ingestion:** ContentGuard still applies its rules to manually ingested content
- **Combined approach:** Use manual ingestion for initial content capture, then let ContentGuard filter and review