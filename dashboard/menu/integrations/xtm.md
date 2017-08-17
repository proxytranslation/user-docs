# XTM

## Overview

The proxy can export content in XLIFF format into XTM, creating projects as necessary, and listen for workflow completions to commence import. XTM has also integrated the preview functionality, allowing live verification of translations.

## Using

After configuring XTM access under the Account screen, submitting to XTM as an external system becomes available at export-time, or from the Previous Exports dialog. Upon submission, the proxy creates the relevant project within XTM and imports the XLIFF into the project. Afterwards, a listening service starts, periodically polling XTM for the workflow state of the project. When the project is set to completed, the proxy detects this during its next polling cycle, and imports the translated XLIFF back into the proxy project.

XTM has also integrated the proxy preview. Using information in the exported XLIFF, XTM's online interface can display the translated page, allowing in-context verification of the translations.

> Nota Bene: the live-updating preview does **not** mean that translations are streamed to the proxy for inclusion! You will still need to save the XLIFF file and import it (either manually or by completing the XTM project) to return the translations to the project!