This project 1 is to let you explore the socket programming interface in
and some other basic aspects of the Python language.

This exercise serves as the foundation for the upcoming programming project. 

A sample working code is given to you in proj0.py. 

The program consists of server code and client code written as two separate threads.

(1) Understand the functionality implemented in the program. First, download,
    save and execute the program as is in your environment. Make sure it executes
    successfully and according to how you would expect.

Then attempt the changes suggested below. It will help subsequent projects if you try playing around with the program as follows.

(2) Try running the program immediately again when it finishes
    successfully. What do you see? Why? What happens when you remove the various
    sleep()s in the program?
    It successfully establishes connection between server and client.The programme would initiate the server thread first.
    Then the program use time.sleep function to delay the execution of the thread ,function random.random() * 5 implies
    the wait time is within 5 seconds.The programme started the client thread , once the connection established between
    client and server the server would send corresponding message to the client.Finally, the program would delay for 5 seconds
    before printing the final line of the program.

    If we remove time.sleep(random.random()*5) from our program the two threads would be started at the same time.
    This might cause some problem if the server is not established before the client programme thread started.
    If we remove the code time.sleep(5) the finally line of the program would be execute before client and server thread finished.


(3) Separate the server code and client code into two different programs,
    server.py and client.py. Execute the server program first and then execute
    the client program. You should still get the same set of print messages as
    in the combined threaded code (proj0.py)

(4) In the given code, the server just sends a message string to the client
    after it connects. Modify the program so that the client sends a string to
    the server and then the server reverses the string and sends it back to the
    client with the original string. For example, if the client sends "HELLO" to the server, the client should receive "OLLEHHELLO". Your program should print the string sent by the client and the
    corresponding string received by the client. Your client program should be
    able to read a string (each line is a string) from a test file (say,
    in-proj0.txt). Similarly, the output of your program should be written to a
    file (say, out-proj0.txt).
