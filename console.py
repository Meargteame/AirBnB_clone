import cmd 
class HBNBCommand(cmd.Cmd):
      prompt ='( hbnb )'
      def do_quite(self,line):
            """ 
            
            """
            return True 
      def do_EOF(self,line):
            """
            
            """ 
            return True 
      
      # override the default empty line 
      def emptyline(self):
            """
            
            """ 
            pass 

if __name__ == '__main__':
      HBNBCommand().cmdloop()
      
      