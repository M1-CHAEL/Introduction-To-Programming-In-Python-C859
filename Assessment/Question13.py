""" Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done

the output is:

ereht olleH
yeH

 """
text_input = str(input())
while text_input != 'Done' and text_input != 'done' and text_input != 'd':
    reverse_text = text_input[::-1]
    print(reverse_text)
    text_input = str(input())