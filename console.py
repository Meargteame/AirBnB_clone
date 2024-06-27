from models import storage
from models.base_model import BaseModel


import cmd 

class HBNBCommand(cmd.Cmd):
    prompt =' (hbnb) '
    
      
    def do_quit():
          pass 
    def do_EOF():
          pass 
    def do_help():
          pass
      
      
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()