# PyFILE CLI

___
 #`About PyFile CLI`

  This is a command line interface, created to help programmers
to perform various file operations in a simple way using commandline 
commands with a simple syntax. We all have difficult times to be 
navigating back and forth to create a file we need to use 
in either the current directories/folders or some other folder deep
inside other folders.

That is why I feel this is a nice tool for most of the programmers
since you just only need to get the simple syntax then you're 
good to go👌🚀.

___
## Current status
This project is still under development and improvement to even make it more
friendly and intractable as possible. But for the basic building blocks are 
already established. This makes the tool operational even though there are 
some `bugs` and `errors` that are under debugging. But You are encouraged to 
give feedback for improvements and addition of the features that you feel if
added could make the tool super cool👌. The tool is also underway in development
for any malfunction please contact through `gesoranthony@gmail.com` or WhatsApp me 
through `+254796899444`

___
## Development

This tool is developed using Python. It has no complexity but its execution feels 
like the code is complicated, but it uses most of the control flows to perform the file 
operations and obtain the needed commands from the commandline commands. But the whole 
program is based on python logics such us the file operation `'+a'` into `-a` for appends, 
`'r'` into `-r` for read, `'w'` into `-w` for writing a file. But for any improvement
or inclusion of some programming/coding style, you are encouraged to give your feedback
to make the tool advanced and more efficient.
___
## Screenshots
dafdfegvs vasdvf avv vqeve fvv

___
## Features
This tool is built to be executing in the terminal of your IDE so as not to reduce navigation's
to other windows. When this tool is executed it runs in the terminal continuously until
you quit its execution. This makes the tool more relevant and friendly to the current working 
directory. Since it is too messy to use the mouse all around the screen you can use the IDE shorthand 
combination to open the terminal `ctrl + `` ` for `VS code` where the tool is executing, and they  perform 
the file operations you need to perform. After which you can use the same command `ctrl + `` ` for `VS code`

This tool can also help you even append or write to the external file without need to append 
content one by one. Instead you can use the `.nn` escape secuence for creating a new line wherever 
you may have felt like adding a new line
> _Example_

> Suppose you wanted to create a simple `HTML` file and append some besic code immediately
> as: <br>
> > < !DOCTYPE html> <br>
>   < html lang="en"> <br >
>   < title> Simple Web Page </ title> <br >
>   < body> <br>
>   < h1> Welcome </ h1> <br>
>   < /body> <br>
>   </ html > <br>

`Syntax:`

      index.html -w  d=< !DOCTYPE html> .nn < html leng="en"> .nn < title> Simple Web Page </ title> .nn < body> .nn < h1> Welcome </ h1> .nn < /body> .nn </ html > .nn
      

### Images:
When you open the file you created it will appear as:

![code](./images/simple%20html%20file.png)

And on the browser it will appear as:

![code](./images/file%20on%20browser.png)


_____
## Prerequisites and Installation


For now the program executes when invoked once but will continuously be
waiting and listening for incoming commands it executes it as it is
expected to behave.

But for the program to execute properly in your machine you must have 
installed the following packages:
1) Python interpreter  `version >= 3.12 `
2) Code editor of your choice ``e.g Pycharm, VS code e.t.c``
> _Usage_
>>   This is not really essential, but I believe this tool is mostly used by
>   programmers to the most. But if note I think you cn use the `cmd` then
>    you can navigate to the destination where you cloned/unzipped this project
>    then execute/compile and run, and you'll be able to use this tool.
3) Code Runner
    > **NOTE**: This is to be downloaded on the code editor you are using, or you want to use
   > just incase you may have forgotten the commandline command to run the tool a
   > python code. Then you may use it to initiate the program 

___

### `# Tutorials `

To use the tool the following are the snippet code syntax you need to know:
 For one to create a file in a file in a file:
 1. You can just type the file name alone with its extension as or add the flag for 
creting new file that is `-cr` as:<br>
 
         home.txt or home.txt -cr 

2. If you want to create and write to the file at the same time you can type the 
file name then followed by the `-w` flag for creating then another `d=` flag to specifie
the beginning of the data to be entered then you click enter. The syntax is as:
         
         home.txt -w d=I have created this file and immediatelly provided this content 
         
