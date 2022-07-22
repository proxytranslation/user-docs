# Translation memory

![Translation memory settings](/img/dashboard2/translation_memory.png) 

Translation memories (TM) are used to store existing translations for segments. You can import translations from *.tmx files or populate the translation memory with translations you have added in the Workbench.

Translation memories are linked to your account and *not* your project. This way, if you want to, you can have one gigantic translation memory for all of your projects. This is useful if you have multiple projects of the same topic. 

Clicking the floating action button brings up the **Create & assign Translation Memory** dialog. You can create a new TM or assign any other that you previously created. While you can add multiple memories to a project, only one of them can be the default for writes.

The memories added (created or assigned) to the project will show up in the list on the top card. You have multiple options for all of them:

- **Import/export**: Opens the dialog where you can upload a TMX file or request an export. Exports will be emailed to you.

- **Edit**: Brings up the Edit TM dialog where you have the same options you had when creating the memory.

- **Populate**: Allows you to add the content from this projet to the TM.

- **Remove**: Unassigns the memory from the project. The memory isn't deleted. You can reassign it or assign it to any other project.

The screen is furnished with a search field you can use to look up segments in a TM.

**IMPORTANT NOTE!**

The TMs you manage on this screen and the Workbench are different from the Translation Memory that is billed: they are used for concordance lookups and automatic translation, and they are completely free to create and use.

On the other hand, the proxy TM associated with a project is a database in the cloud that holds translations of segments. When you reimport your XLIFF files or run auto-pretranslate, you are writing to this project TM, which is billed the first time around.
