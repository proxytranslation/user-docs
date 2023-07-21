# Resource Translation

Resources are binary content found on the sites, such as images,
PDFs, CSS and JS files, etc.  Please note that the content of these
resources is not extracted for translation, so you have to translate /
edit them separately.

## Replacing Images with Localized Versions

You have the option to replace images, downloadable files and other
resources with their localized version.

1. Please make sure that you see the appropriate target language (flag) selected on the top     navigation bar.

2. Navigate to the original image in the Pages list.

3. Click on the thumbnail image.

4.	Click on the blue MARK LINK AS TRANSLATABLE or the MANAGE TRANSLATIONS button on the right.

5. Click on the SELECT A FILE button, open the desired image and then click on the blue UPLOAD button.

6. The original image will be replaced and the new image shown on the translated site immediately.

7. Check the Preview to see if the image was replaced properly.

8. Repeat these steps for all images and all target languages that
   need localized versions.

**Please note that you can replace only 1 resource, for 1 target
language at one time.**

## Extraction Issues with `data-image` Attribute

Images might be inside a "data-image" attribute in the source code. In
such cases you have to set the "data-image" attribute up to be
translated as a link in the Advanced Settings screen.  The `<img src>`
attributes are recognized by default as URLs, while data-* attributes
are not, as they can contain any sort of data, and must be configured
manually to tailor the behavior to the current project's needs.

The image might also be drawn from a subdomain. In this case you have
to create a second project for the subdomain, mutually link the two
projects together, and add the resource in the subdomain's project. In
this case you have to publish the two projects together, in order to
preserve the mapping.
