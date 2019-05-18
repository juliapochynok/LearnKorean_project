# LearnKorean Project

### Description
This program is based on the National Institute of Korean Language Basic/Learner's Dictionary Open API(한국어기초사전 오픈 API 서비스), it allows you to learn Korean words and test the knowledge you gain.

### Incoming and outgoing data
For receiving the necessary data, a number of requests wad made by using API of National Institute of Korean Language.After each request, the data was returned in XML format. After that, the processing of the received data was carried out.

The outgoing data is displayed on clients screen as information about a certain Korean word, its translation, and definition. The way these are shown for the client depends on the action he/she is making.

### Program structure
The program consists of several modules. Module arrays.py contains DynamicArray class which is used as the main data structure in this program. Classes User and WordController that represent a client are in classes.py module. Class User has some methods that represent his ability: learning a new word, testing knowledge, watching learned words and setting users original file. Class WordController is responsible for reading and writing words into a file, it has methods that read information from the file, write information to file, convert all information in the file to a string and displays it. 
Modules get_xml.py and make_main_wordlist.py is responsible for getting XML file (data.xml)  by using API and parsing this file to get needed information about Korean words (that is placed in the translations.txt file).
And the main module is flask_main.py which contains a number of functions responsible for the interface and final result of the program.
Also, there is another folder - templates, that contains all HTML documents for successful program representation.
To implement the program, import of some Python modules were needed. Specifically,  requests, xml.etree.ElementTree, fileinput, random, ctypes modules.
And also a microframework flask is used to create a working interface.

### Run Dependencies/Usage
You can use this program here on PythinAnywhere:
http://learningkoreanwords.pythonanywhere.com/

Or you can download folder "final_learn_korean" from this repository and run it on your own computer.

### Usage Example
Step 1. 

User needs to enter his/her name without white spaces.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor11.png?raw=true)

If the user enters an appropriate name “Invalid input” will be displayed.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor12.png?raw=true)

Step 2.

If it is client’s first time using this program, a new account will be made.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor2.png?raw=true)

Step 3.

Here is the main menu. The client has 4 different options, he/she can experience.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor3.png?raw=true)

Step 4.

If the client chooses option 1 - learn new word, new word and information about it will be displayed on the screen. To return to the main menu user should press the “Go Back” button.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor4.png?raw=true)

Step 5.

If the client chooses option 2 -test yourself, the test will be displayed on the screen. To return to the main menu user should press the “Go Back” button.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/Screenshot%20from%202019-05-15%2020-33-23.png?raw=true)

If the client answers right, TRUE will be displayed.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor13.png?raw=true)

If the client answers wrong, FALSE will be displayed.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor8.png?raw=true)

Step 6.

If the client chooses option 3 - see wordlist, all words learned by this user will be displayed on the screen. To return to the main menu user should press the “Go Back” button.
![](https://github.com/juliapochynok/LearnKorean_project/blob/master/images/kor9.png?raw=true)

Step 7.

If client wants to log Out of the ptrongram, he/she should press the “Log Out” button.


### Unittests
Unittests to test the performance of the developed implementation of abstract types is located in the folder “test” in the repository. 
IMPORTANT: Because User and WordController classes work with files and modify them, most of the developed unittests for these classes will work correctly only one (first) time. So, after the first use, the files that are used are already modified and, accordingly, if the repetitive passage of unittests is performed, the results will already be different.

### License
Apache License

### Developer
Julia Pochynok 
