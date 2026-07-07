"""
Problem Statement:

A cloud storage service uploads multiple files submitted
by users.

Before starting the upload process, the system should
automatically establish a secure cloud connection.

The uploaded files should be generated one by one using
a generator function instead of storing all uploaded files
for processing.

After all files are uploaded, the system should verify
the uploaded files one by one using an iterator.

If an invalid file size (less than or equal to zero MB)
is entered, display:

Invalid File Size

The cloud connection must still close automatically even
if an exception occurs.

Requirements:
1. Create a Context Manager using __enter__() and __exit__().
2. Use a generator function with yield.
3. Use an iterator using iter() and next().
4. Use Exception Handling.
5. Store file details using a dictionary.
6. Automatically close the cloud connection.

Input Format:
First line contains the number of files.

Next N sets contain:

File Name
File Size (MB)

Output Format:

Connecting to Cloud Storage...
Uploading Files:
Report.pdf -> 20 MB
Image.png -> 15 MB

Verifying Uploaded Files:
Report.pdf -> 20 MB
Image.png -> 15 MB

Cloud Connection Closed

If the file size is invalid, display:

Invalid File Size

Sample Input:
2
Report.pdf
20
Image.png
15

Sample Output:
Connecting to Cloud Storage...
Uploading Files:
Report.pdf -> 20 MB
Image.png -> 15 MB

Verifying Uploaded Files:
Report.pdf -> 20 MB
Image.png -> 15 MB

Cloud Connection Closed

case=1
input=2
Report.pdf
20
Image.png
15

output=
Connecting to Cloud Storage...
Uploading Files:
Report.pdf -> 20 MB
Image.png -> 15 MB

Verifying Uploaded Files:
Report.pdf -> 20 MB
Image.png -> 15 MB
Cloud Connection Closed

case=2
input=1
Project.zip
100

output=
Connecting to Cloud Storage...
Uploading Files:
Project.zip -> 100 MB

Verifying Uploaded Files:
Project.zip -> 100 MB
Cloud Connection Closed

case=3
input=3
Resume.pdf
5
Photo.jpg
12
Video.mp4
200

output=
Connecting to Cloud Storage...
Uploading Files:
Resume.pdf -> 5 MB
Photo.jpg -> 12 MB
Video.mp4 -> 200 MB

Verifying Uploaded Files:
Resume.pdf -> 5 MB
Photo.jpg -> 12 MB
Video.mp4 -> 200 MB
Cloud Connection Closed

case=4
input=0

output=
Invalid Number of Files

case=5
input=-2

output=
Invalid Number of Files

case=6
input=2
Image.png
-5
Report.pdf
20

output=
Connecting to Cloud Storage...
Cloud Connection Closed
Invalid File Size
"""
class InvalidFiles(Exception):
    pass
class InvalidSize(Exception):
    pass
class CloudSession:
    def __enter__(self):
        print("Connecting to Cloud Storage...")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Cloud Connection Closed")
        return False
        
def generate(d):
    for i in d.values():
        if i<=0:
            raise InvalidSize("Invalid File Size")
    print("Uploading Files:")
    for i in d.items():
        yield f"{i[0]} -> {i[1]} MB"
try:
    n=int(input().strip())
    if n<=0:
        raise InvalidFiles("Invalid Number of Files")
        
    d={}
    for i in range(n):
        fname=input().strip()
        fsize=int(input().strip())
        d[fname]=fsize
    with CloudSession():
        res=list(generate(d))
        it=iter(res)
        for i in res:
            print(i)
        print("\nVerifying Uploaded Files:")
        while True:
            try:
                print(next(it))
            except StopIteration:
                break
except Exception as e:
    print(e)

