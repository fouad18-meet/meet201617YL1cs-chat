from turtle_chat_client import Client
import turtle
from turtle_chat_widgets import Button , TextInput
class TextBox(TextInput):
    def draw_box(self):
        d_t_b=turtle.clone() #d_t_b = drawing the box
        d_t_b.penup()
        d_t_b.goto(self.width, self.height)
        d_t_b.pendown()
        d_t_b.goto(self.width, 0)
        d_t_b.goto(0, 0)
        d_t_b.goto(0, self.height)
        d_t_b.goto(self.width, self.height)
    def write_msg(self):
        self.setup_listeners()
        print(self.new_msg)
        self.writer.goto(10, self.height - 15)
        self.writer.clear()
        self.writer.write(self.new_msg)
        if len(self.get_msg()) % self.letters_per_line == 0:
            self.new_msg=self.new_msg+ "\r"
        print(self.get_msg())
        
        

db = TextBox()





        
