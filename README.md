# hbnb - An AirBnB Clone
![hbnb Logo](https://imgur.com/OilEsXV.png "hbnb Logo")

This is a simple copy of the AirBnB website meant to instill the fundamental concepts of high-level programming.

## The Console
This is a command line interpreter that aids the storing/managing/manipulating of site data for development and debugging.
### Starting the Console
Upon cloning or downloading the repo, simply `cd` into the `AirBnB_clone` directory and run `console.py`. You should be able to see the prompt `(hbnb) `.
```
vagrant$ cd AirBnB_clone/
AirBnB_clone$ ./console.py
(hbnb) 
```
### Console Usage
To use the console, type the desired command into the terminal and hit `ENTER`.
#### Command Overview

| Command        | Function           | Usage |
| ------------- |-------------| ------------- |
| `create` | Create object and display its id | `create <OBJ TYPE>` |
| `show` | Show object info      | `show <OBJ TYPE> <OBJ ID>` |
| `destroy` | Delete object      | `destroy <OBJ TYPE> <OBJ ID>` |
| `all` | Show all objects      | `all [OBJ TYPE]` |
| `update` | Update object attribute      | `update <OBJ TYPE> <OBJ ID> <ATTR NAME> <ATTR VALUE>` |
| `help` | Display command info      | `help [COMMAND]` |
| `quit` | Exit the console      | `quit` |

* Required command arguments are denoted with `< >`. Optional arguments are denoted with `[ ]`.
* `OBJ TYPE` can be one of the following: `BaseModel`, `User`, `State`, `City`, `Place`, `Amenity`, `Review`
* `OBJ ID` refers to each object's unique ID, which is stored in its `id` attribute.
* `COMMAND` can be any one of the above commands.

#### Examples
* To create a `City` object, display its info, and delete it:
```
AirBnB_clone$ ./console.py
(hbnb) create City
783b144c-2b43-42c5-9945-e089c966cd9d
(hbnb) show City 783b144c-2b43-42c5-9945-e089c966cd9d
[City] (783b144c-2b43-42c5-9945-e089c966cd9d) {'id': '783b144c-
2b43-42c5-9945-e089c966cd9d', 'updated_at': datetime.datetime(2019, 7, 2, 19, 
57, 29, 868183), 'created_at': datetime.datetime(2019, 7, 2, 19, 57, 29, 
867862)}
(hbnb) destroy City 783b144c-2b43-42c5-9945-e089c966cd9d
(hbnb) show City 783b144c-2b43-42c5-9945-e089c966cd9d
** no instance found **
(hbnb) 
```
* To display all working instances:
```
(hbnb) all
["[City] (06179065-4084-4a4b-88e5-c67d9832bf71) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 52, 63134), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 52, 63134), 'id': '06179065-4084-4a4b-
88e5-c67d9832bf71', '__class__': 'City'}", "[User] (bba5b797-d8e3-42e3-
aa43-10826d06ba39) {'created_at': datetime.datetime(2019, 7, 2, 20, 5, 47, 
863451), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 47, 863688), 
'id': 'bba5b797-d8e3-42e3-aa43-10826d06ba39', '__class__': 'User'}", "[Place] 
(1215e087-0c08-4795-9528-566c111278bb) {'created_at': datetime.datetime(2019, 
7, 2, 20, 5, 54, 664432), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 
54, 665353), 'id': '1215e087-0c08-4795-9528-566c111278bb', '__class__': 
'Place'}", "[Place] (640fb953-9b25-4ab0-ba8f-2be34b887f9d) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 57, 214700), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 57, 214700), 'id': '640fb953-9b25-4ab0-
ba8f-2be34b887f9d', '__class__': 'Place'}"]
(hbnb) 
```
* To display all working instances of the `Place` class:
```
(hbnb) all Place
["[Place] (1215e087-0c08-4795-9528-566c111278bb) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 54, 664432), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 54, 665353), 'id': 
'1215e087-0c08-4795-9528-566c111278bb', '__class__': 'Place'}", "[Place] 
(640fb953-9b25-4ab0-ba8f-2be34b887f9d) {'created_at': datetime.datetime(2019, 
7, 2, 20, 5, 57, 214700), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 
57, 214700), 'id': '640fb953-9b25-4ab0-ba8f-2be34b887f9d', '__class__': 
'Place'}"]
(hbnb) 
```
* To update the `name` attribute of a `User` object:
```
(hbnb) create User
4728ae45-f208-4093-82d4-dfd8ba7b4e25
(hbnb) show User 4728ae45-f208-4093-82d4-dfd8ba7b4e25
[User] (4728ae45-f208-4093-82d4-dfd8ba7b4e25) {'updated_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'created_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'id': '4728ae45-
f208-4093-82d4-dfd8ba7b4e25'}
(hbnb) update User 4728ae45-f208-4093-82d4-dfd8ba7b4e25 name 'juno'
(hbnb) show User 4728ae45-f208-4093-82d4-dfd8ba7b4e25
[User] (4728ae45-f208-4093-82d4-dfd8ba7b4e25) {'updated_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'name': 'juno', 
'created_at': datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'id': 
'4728ae45-f208-4093-82d4-dfd8ba7b4e25'}
(hbnb) 
```
* To show documented commands and get information on the `quit` command:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit
 Quit command to exit the program. 
(hbnb) 
```
* To exit the console:
```
(hbnb) quit
AirBnB_clone$ 
```
