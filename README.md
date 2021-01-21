# pdf-to-mp3
​	A project focused on learning, wich the goal is to turn a .PDF file into a .MP3 file, using text-to-speech mechanisms.

​	The file "main.py" has the main functionality: to turn a .PDF file into  a .MP3 file. It is able to do this due to two other archives: "pdf_to_str.py" and "str_to_mp3.py". The first one, with help of the library "Tika", is able to turn a .PDF file into a string. And as expected, the second one is able to turn a string into a .MP3 file.