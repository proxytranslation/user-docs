# Introduction - Dashboard 3.0 Overview



## Key Features

### Content Ingestion System
Dashboard 3.0 introduces a sophisticated content ingestion system that automatically discovers and captures new website content for translation. This system operates through a lightweight JavaScript script that monitors your website for changes and new content.

### Manual Content Ingestion
For environments requiring strict editorial control, Dashboard 3.0 offers manual content ingestion through authenticated links. This feature allows you to capture content only when authorized users visit specific pages, ensuring that only reviewed and approved content enters the translation workflow.

### ContentGuard
ContentGuard is our advanced content classification and filtering system that intelligently screens incoming content to prevent irrelevant material, errors, or potential data leaks from entering your translation flow. It ensures only legitimate, high-quality content is processed.

## Getting Started

To begin using Dashboard 3.0:



## Content Ingestion Modes

### Automatic Content Ingestion
- **Best for**: High-volume, fast-moving websites
- **How it works**: Content is captured automatically whenever any visitor browses your website
- **Benefits**: Fully automated, ensures new content is captured quickly
- **Considerations**: May ingest irrelevant content from browser extensions or third-party overlays

### Manual Content Ingestion
- **Best for**: Environments requiring tight editorial control
- **How it works**: Content is only captured when pages are accessed using authenticated preview links
- **Benefits**: Secure and controlled ingestion, ensures only finalized content enters translation
- **Considerations**: Requires manual intervention for each new page

### Disabled Content Ingestion
- **Best for**: Static websites or when you want to pause content capture
- **How it works**: No new content is ingested, even if users interact with the site
- **Benefits**: Maximum control, prevents accidental ingestion
- **Considerations**: New content won't be translated automatically

## ContentGuard Features

### Language Detection
Filter content by language to ensure only approved languages are processed. This feature is particularly useful for multi-language sites or when you need to exclude unexpected languages.

### Strictness Level Adjustment
Fine-tune how ContentGuard evaluates content:
- **More Strict**: Less content is automatically accepted; more entries require human review
- **Less Strict**: More content flows through automatically; fewer manual reviews

## Best Practices

1. **Start with manual ingestion** for new projects to establish control over content quality
2. **Use automatic ingestion** for established sites with regular content updates
3. **Configure ContentGuard** with moderate strictness initially, then adjust based on your content patterns
4. **Regularly review** pending content to maintain translation quality
5. **Use descriptive names** for manual ingestion links to track their purpose

## Support and Resources

For detailed instructions on setting up specific features, refer to the following guides:
- [Content Ingestion Setup](content-ingestion.html)
- [Manual Content Ingestion](manual-content-ingestion.html)
- [ContentGuard Configuration](contentguard.html)

If you need assistance with Dashboard 3.0 features, contact our support team with your project code for personalized help. 