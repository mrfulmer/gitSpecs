# gitSpecs

gitSpecs is a method of tracking, creating, and updating bid specifications using the power of git, markdown, Microsoft word, and python. Source documentation is created and tracked in markdown to facilitate the usage of git. This allows for easy version tracking, branch creation, and an approval process. When time comes to compile the source bid specifications, gitSpecs converts the markdown to a strict set of styles to create a .docx file. The docx file is preferable to markdown as it is more easily understand to a wider range of individuals. Finally, any changes to the word document can easily be converted back to markdown to allow for version tracking. The backward compatibility allows for changes in the master specifications to be push to project specifications after creation and modifications through git merging.


## Workflow

The main repository will include a prod, a spec_dev, and code_dev branches. The branches will correlate to the three workflows of the project.

### Prod Branch

The prod branch will handle the project specification request. When an engineer request specs, python code is run to compile the specification documents to a word document. The engineer is free to modify the specification as they see fit. If a change is later published to the prod branch, the project spec can be decompiled to markdown, merged with the prod branch, review the changes, and compile back to word.

### spec_dev

The spec_dev branch is not a single branch, but any number of branches which will affect the spec documents. The nomenclature of these branches is spec_dev_#### where #### is short descriptor of the changes. Merges to the prod_branch from the spec_dev will be reviewed prior.

### code_dev

## Specification Documents

How to write the spec documents, include style syntax, and form input data.

The code_dev branch is where changes to the python code will occur.


## UI

When specifications need to be compiled for a project, the software will ask question to better gauge which specification section will be required in the document. The engineer will have the option at the end to override this functionality. 

### Engineer Inputs

Not sure yet if I want the engineer to answer questions related to form data inside of the spec documents. Probably not all information, but a portion of the form data can be asked, and filled in prior to compiling.

