# Resources

Resources are binary content found on the sites, suchg as images, PDFs, CSS and JS files, etc.  Please note that the content of these resources is not extracted for translation, so you have to translate / edit them separately.

### How to replace am image with its localised version?

You have the option to replace images, downloadable files and other resources with their localized version.

1) Please make sure that you see the appropriate target language selected on the left side menu.  
2) Navigate to the original image in the Resources view of the Content (or the Discovery) section.  
3) Hover over the thumbnail image. A green '+' icon should appear.  
4) Click this icon. It marks the image as 'localizable', i.e. a candidate for replacement.  
5) Select the replacement image and upload it. It will immediately replace the original image, and the new image will show up on te translated site.  
6) Check the Preview to see if the image was replaced properly.  
7) Repeat these steps for all images and all target languages that need localized versions.  
**Please note that you can replace only 1 resource, for 1 target language at one time.**  


### I can't extract an image from the website. Why is it?

The image might be inside a "data-image" attribute in the source code. In such cases you have to set the "data-image" attribute up to be translated as a link in the Advanced Settings screen.
The <img src> attributes are recognized by default as URLs, while data-* attributes are not, as they can contain any sort of data, and must be configured manually to tailor the behavior to the current project's needs.

The image might also be drawn from a subdomain. In this case you have to create a second project for the subdomain, mutually link the two projects together, and add the resource in the subdomain's project. In this case you have to publish the two projects together, in order to preserve the mapping.

