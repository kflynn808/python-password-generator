<h1>python-password-generator</h1>

<h2>Description</h2>
<p>This is a very simple CLI tool that I made to get used to the GitHub workflow. It's purpose is to create a random string of characters that you could use as a password. The flags passed allow you to change what type of characters are used in the string, as well as how long the string will be.</p>

<h2>How To Install</h2>

- Make sure you have python installed
- In the top right click the green '<>code' button and download the .zip file
- Extract the zip file and you're ready to go!

<h2>How To Use</h2>

Inside of your terminal navigate to the directory containing ppg.py and run this command > `python ppg.py [flag you want to use]`

<h2>Flags</h2>

```
usage: Python Password Generator [-h] [-s] [-c] [-n] [-r] [-l LENGTH]

options:
  -h, --help           show this help message and exit
  -s, --special        Use special characters in the string (!,@,#,etc.)
  -c, --capitals       Use capital letters in the string
  -n, --numbers        Use numbers in the string
  -r, --random         Create a strong random string using all character
                       types (default: 16 char long)
  -l, --length LENGTH  Length of the string
```

<h2>Example Usage</h2>

```
# creates a 10 character string with capitals and numbers
python ppg.py -c -n -l 10 
[*] Generated String:> MlAcHkdRZrkpSxpL
```
