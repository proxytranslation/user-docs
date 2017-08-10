# Dropbox

## Overview

The Proxy is capable of installing a Dropbox connector in your account, that allows it to export into and import from a specific folder in the account. The proxy root folder needs to be specified once, during account linking, after which the proxy will create new folders within based on the project code as needed.

During export, the option to submit to Dropbox will place the exported ZIP file into the `export` folder of the given project, allowing you to download and handle the file rapidly. After processing, the contents of this folder can be deleted freely.

The `import` folder is used to re-import translated content into the database. Once a file is placed in this folder, the project owner receives an email notification of the fact. From the Import dialog, they can then choose which files they want imported, which are then imported directly from Dropbox. By default, on switching to the Dropbox tab in the import dialog, only files added *after* the last import will be selected, making distinction easy.

## Registration

To add a new account, you'll be required to log in with a valid Dropbox account, and authorize the Translation Proxy Dropbox app to access your storage. Once complete, you will be redirected to the Dashboard, where you can then link the account to any number of projects (the Dropbox account is keyed to the *user*, being available on all owned projects for linking).

## Using

During export, select the option to submit to an external system, and choose Dropbox from the dropdown. Once the export completes, the file will be automatically uploaded to Dropbox, in the project's `export` folder. Already-existing exports can be submitted from the Previous Exports dialog.

On uploading a file to the `import` folder of a project, you will be notified via email. From the Import Translations dialog, you can view the contents of the project's `import` folder via the Dropbox tab, where the system will automatically designate files uploaded since the last import for processing - you are free to modify this selection, however. On starting the import, the files will be downloaded from your account, and processed through the regular import process.