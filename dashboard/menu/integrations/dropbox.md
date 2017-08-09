# Dropbox

The Proxy is capable of installing a Dropbox connector in your account, that allows it to export into and import from a specific folder in the account. The proxy root folder needs to be specified once, during account linking, after which the proxy will create new folders within based on the project code as needed.

During export, the option to submit to Dropbox will place the exported ZIP file into the `export` folder of the given project, allowing you to download and handle the file rapidly. After processing, the contents of this folder can be deleted freely.

The `import` folder is used to re-import translated content into the database. Once a file is placed in this folder, the project owner receives an email notification of the fact. From the Import dialog, they can then choose which files they want imported, which are then imported directly from Dropbox. By default, on switching to the Dropbox tab in the import dialog, only files added *after* the last import will be selected, making distinction easy.