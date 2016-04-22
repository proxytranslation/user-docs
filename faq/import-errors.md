##XLIFF import errors##
  
When you import your translated XLIFF file back to easyling, you will receive an e-mail notification when the process is ready. This mail contains the URL of the import log, and an overview of the log entries:  
- Error:  
- Warning:  
- Info:  
  
If you see other than ‘**Error: 0**’ in your notification mail, the XLIFF file needs fixing. Usually these are tag placement errors that can be easily fixed in a text editor like Notepad++ or Sublime (the ones that have syntax highlighting, to make this fixing job easier), yet they do need attention, as the corresponding translation will not show up on the website.  
- Open the XLIFF in your text editor  
- Open the log file and check the error message(s)  
- Do the necessary corrections in your XLIFF (see ‘Troubleshooting’)  
- Save & upload the corrected XLIFF  
  
In very serious cases the import might fail completely, but this is very rare. These cases include: attempt to upload an XLIFF related to another project, XLIFF with target language that doesn't exist in the project, and fully invalid XML in the file. In most cases the file is imported, only the faulty entries are omitted.  
  
Please note that you need XLIFF files. Ideally, the export format of the CAT-tool should be the same as the import format, and as you import an XLIFF file for translation, the output should also be a standard XLIFF file. However, some versions of Studio tend to create an **SDLXLIFF** file upon exporting the translation. In this case, simply use the "**Finalize**" batch task or open the document in the **Editor**, press **SHIFT+F12** and select the target file location. This will create the XLIFF file for you (instead of SDLXLIFF).  
You might also need to disable segment info storage in Studio (***Options -> File Types -> XLIFF -> Settings -> 'Do not store segmentation information in the translated file'*** should be checked). This may require creating a new project.

### Troubleshooting   
**Error**:  
***The xml structure has been changed so much that it is now unmappable from the source***  
  
**Fixing**:  
1) Open both the **XLIFF file** and the **error log** in a text editor  
2) Select & copy the ***TM-key*** of the faulty entry, the part after ‘(trans-unit id="xxxxx)_tm:’ in parenthesis right after the error message  

[[https://github.com/easyling/public/wiki/img/select_ID.jpg|alt=Select TM-key]]   

3) Search for this key in the **XLIFF file** by pasting it into the ‘Find’ field. Only 1 translation unit will match.  
  
[[https://github.com/easyling/public/wiki/img/find_ID.jpg|alt=Find TM-key]]   

4) Compare the tags in the source and target languages, and fix the mismatch by editing the **target text**.  
(You can also use an online text comparison tool for this task: copy-paste `<source>  …  </source> `in one pane and `<target> … </target>` in the other one.)  
5) Save the corrected XLIFF file and upload again. It should give no error message now.  

***OR, alternatively,***  
1. Go back to your CAT tool, where you did the translation and open the faulty file for editing  
2. Run QA. It will list you all the tag mismatches  
3. Navigate to the faulty segment(s) and fix the tags  
4. Export the corrected file and upload it. It should give no error message now.


**Error**:  
***Content found outside of outermost element***  
  

**Fixing**:  
Practically this means that there is an extra space before the starting `<target><g*> `or after the closing `</g></target>`  
  
1) Open both the **XLIFF file** and the **error log** in a text editor  
2) Select & copy the ***TM-key*** of the faulty entry, the part after ‘(trans-unit id="xxxxx)_tm:’ in parenthesis right after the error message  

[[https://github.com/easyling/public/wiki/img/select_ID.jpg|alt=Select TM-key]]   

3) Search for this key in the **XLIFF file** by pasting it into the ‘Find’ field. Only 1 translation unit will match.  
  
[[https://github.com/easyling/public/wiki/img/find_ID.jpg|alt=Find TM-key]]  

4) Delete the extra space around the tags  
5) Save the corrected XLIFF file and upload again. It should give no error message now.  


***OR, alternatively,***  
1. Go back to your CAT tool, where you did the translation and open the faulty file for editing  
2. Run QA. It will list you all the tag mismatches  
3. Navigate to the faulty segment(s) and fix the tags  
4. Export the corrected file and upload it. It should give no error message now.  
  
  

###IMPORTANT!  
**Most of these issues can be avoided if the QA parameters of your CAT tool are set up properly, and you run QA before exporting your XLIFF files. Please make sure to check your translation for tag consistency and extra spaces; these are critical errors in website translation that can spoil the code.**
  
**Error**:  
***Illegal character***  
  

**Fixing**:  
The reason for this error is usually a coding mismatch: all our XLIFF files are exported using the world-standard UTF-8 codepage. However, your CAT tool may save the file using another codepage, depending on the language, which may cause certain characters to appear as invalid.  
  
1) Open both the **XLIFF file** and the **error log** in a text editor  
2) Select & copy the ***TM-key*** of the faulty entry, the part after ‘(trans-unit id="xxxxx)_tm:’ in parenthesis right after the error message  

[[https://github.com/easyling/public/wiki/img/select_ID.jpg|alt=Select TM-key]]   

3) Search for this key in the **XLIFF file** by pasting it into the ‘Find’ field. Only 1 translation unit will match.  
  
[[https://github.com/easyling/public/wiki/img/find_ID.jpg|alt=Find TM-key]]  

4) Check if you see any strange characters, like squares or other meaningless characters.  
  
5) Go back to your CAT tool and change the export options to use UTF-8 encoding. (As UTF-8 is a universal standard, it should be available.)  
  
6) Re-export the XLIFF with UTF-8 encoding and upload it. It should give no error message now.  
  
 