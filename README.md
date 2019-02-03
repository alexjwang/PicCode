# PicCode

This project was created at DevFest 2019 at Columbia University by Alexander Wang, Ursula Ott, Joheen Chakraborty, and Michael Jan.

### Project Overview
Whiteboarding/coding by hand/reading code in the form of physical text (via textbook or otherwise) is a common practice among programmers/CS students. It would then be helpful to convert code in the form of literal text to a more usable form.

PicCode would enable anyone to take a picture of code and then text the picture to a certain phone number. Then, they would receive a return text that either contains the output of the function or any errors in the code. This is extremely useful as all of it can be done via only a phone, and whiteboarding often results in buggy code that is hard to verify without compiling. Here, one can quickly verify any handwritten code by simply taking a picture.

### Description
We set up the entire program on the Google cloud platform so the app is always running without needing to be hosted by a local machine. A python/flask/ngrok program was used to receive the image from Twilio and to send the response back to the user (also via Twilio). The Google Vision cloud API was utilized to help with the physical text to code translation. Within the Google cloud virtual machine, we wrote a shell script that would compile the programs, determine any errors/outputs, and then send it back to Twilio via the aforementioned python program. This works for multiple mediums, including printer paper, lined paper, blackboards, and whiteboards.

### Examples

<img src="./img/test1.jpg" height=750/> 
<img src="./img/test2.jpg" height=750/> 
<img src="./img/test3.jpg" height=750/> 
<img src="./img/test4.jpg" height=750/> 
Example of error feedback to help debug.
<img src="./img/test5.jpg" height=750/> 
<img src="./img/test6.jpg" width=750/> 

### Future Direction
-Expand the possible code to more than just C. First steps would probably be Python and Java, which are among the most popular programming languages today.

-Look at ways to improve the accuracy of the machine learning text to code algorithm. Currently, we've coded some basic algorithms that correct simple compiler mistakes (missing semicolons for example). But the Google Cloud OCR tool is trained on English grammar and vocabulary, which is less accurate than training a model on code from the ground up. There are also a number of research papers (ex. https://arxiv.org/pdf/1801.10467.pdf) that use deep learning text investigating to correct code for syntax errors after the fact, and, given a dataset of programs, we'd be able to  better train our own text recognition machine learning model.

### Technologies Used
Google Cloud, Twilio API, Python, Flask, ngrok
