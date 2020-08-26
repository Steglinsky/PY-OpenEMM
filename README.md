# PY-OpenEMM
### A set of functions to automate your OpenEMM 2015 R3 application.

#### Required libraries:

- os
- time
- selenium

#### Other requirements:

- Any selenium driver (chrome recommended)

------------


##  Functions (in development):

### Login
 `login()`


**Possible arguments:**

`address = 'domain'`
`password = 'password'`

**Example:**
`login(address = 'thic-cat.com', password = 'lazycat')`


=========================================================

### Password change
`change_password()`

**Possible arguments:**

`old = 'oldpasswd'`
`new = 'newpasswd'`

**Example:**
`change_password(old = 'lazycat', new = 'baldcat')`


=========================================================

### Adding a new mailing list
`new_list()`

**Possible arguments:**
`name = 'name'`

**Example:**
Adds a new e-mail list. The name must be indicated in the 'name' argument. Otherwise, the list will take the default value.
`new_list(name = 'Cat food 01.01.2020')`


=========================================================

### Data import
`data_import()`

**Possible arguments:**

`list_path = 'C:\location\of\file.txt'`
`checklist = 'name_or_part_of_a_list_name'`

**Example:**
This command will load the e-mail list file located in the specified location to the list named '01.01.2020' or to the list that contains '01.01.2020'.

`data_import(list_path = 'C:/Funny Cats/sleepingcats.txt', checklist = '01.01.2020')`

**Important:** The name of the list does not have to coincide, it only has to contain the indicated string. In case the string is not unique, the data will be loaded to the first list you meet. This is useful when the name of the list is always the same and the identifier is only the date.


=========================================================

### Deleting data
`remove_data()`


**Example:**
Simply remove the contents of all mailing lists

`remove_data()`




=========================================================

