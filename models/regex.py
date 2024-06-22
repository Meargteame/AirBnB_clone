# # import unittest
# import re
#
# # explain_letter = '~\b(?<![\d.])\d*\.?\d+\s*A\b~'
# #
# # r'''
# #     matches strings that start with ~ after that make sure its standing alone \b
# #     then group (?) which means the grouping is optional then match this sign <!
# #     open character set match numbers and every single character also
# #     after that \d* this matches every zero or more occurrences of numbers
# #     after that \.? an optional period is also included
# #     after that match one or more occurrences of numbers
# #     after that match or more occurrences  of space is matched
# #     followed by capital A with \b for block showing it should be standalone
# #     then lastly a tilde matching ~ at the end.
# #
# #     so the regex would look like this
# #
# #     text = '~<!45343432.423424 A!~'
# #
# # '''
#
#
#
# #
# # class TestRegex(unittest.TestCase):
# #     def test_email_matching(self):
# #         pattern = r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3}$\b'
# #         emails = [
# #             "wexample@example.co",
# #             "john.doe@example.co",
# #             "test123@example.co",
# #             "missing@tld.co"
# #         ]
# #         regex = re.compile(pattern)
# #         for email in emails:
# #             with self.subTest(email=email):
# #                 match = regex.match(email)
# #                 self.assertIsNotNone(match, f"{email} should match the email pattern")
# #
# # if __name__ == '__main__':
# #     unittest.main()
# #
# # text = '''
# #
# # abc123abc123abc123ABC
# # '''
# #
# # pattern = r'abc'
# #
# # regex = re.compile(pattern)
# #
# # matches = regex.finditer(text)
# #
# # print(bool(matches))
# #
# # for match in matches:
# #     print(match)
#
# # text2 = input('input your digit: ')
# # text = 'BaseModel 49faff9a-6318-451f-87b6-910505c55907'
#
# # pattern = r'([A-Za-z]+)\s((\w{8}-\w{4}-\w{4}-\w{4}-\w{12})?)'
# # pattern = r'([A-Za-z]+)\s(?:(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}))?'
#
# # text = '''
# # Mr Simpson
# # Mrs Simpson
# # Mr. Simpson
# # Ms Smith
# # Mr. T
# # '''
#
# # # pattern = r'(\d{4})-(\d{2})?-\d{4}-(\d{2})'
# # text = 'kj'
# #
# # pattern = r'(abc)(def)'
# #
# # regex = re.compile(pattern)
# #
# # # matches = regex.finditer(text)
# #
# # matches = regex.finditer(text)
# #
# #
# # # a=None
# # # b = None
# # # print(matches.groups())
# # # print(matches)
# # #
# # for match in matches:
# #    a, b = match.groups()
# #
# # print(a)
# # print(b)
#
# list_of_matches = ['BaseModel 49faff9a-6318-451f-87b6-910505c55907 emai5l "kellyayo413@gmail.com"',
#                    '49faff9a-6318-451f-87b6-910505c55907 email "kellyayo413@gmail.com"',
#                    'BaseModel email "kellyayo413@gmail.com"',
#                    'BaseModel 49faff9a-6318-451f-87b6-910505c55907 "kellyayo413@gmail.com"',
#                    'BaseModel 49faff9a-6318-451f-87b6-910505c55907 email',
#                    'BaseModel',
#                    '49faff9a-6318-451f-87b6-910505c55907']
#
# text = 'BaseModel 49faff9a-6318-451f-87b6-910505c55907 ei8mail "kellyayo413@gmail.com'
#
# pattern = r'([a-zA-Z]+)?\s?(\w{8}[-]\w{4}[-]\w{4}[-]\w{4}[-]\w{12})?\s?([a-zA-Z]+)\s?(\S+)?'
#
# regex = re.compile(pattern)
# #
#
# for match in list_of_matches:
#     result = regex.match(match)
#     if result:
#         print(result.groups())
#
#
#
# matches = regex.finditer(text)
#
# for matche in matches:
#     print(matche.groups())
# #
# # text = '434bo5ok'
# #
# # pattern = r'(^[0-9]+)'
# #
# # regex = re.compile(pattern)
# #
# # matches = regex.match(text)
# #
# # print(matches)

# its time to demystify this pattern


rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'

'''
    ^ makes sure its starts with alphanumeric, all characters that are not whitespace characters.
    group1 == (\S+) matches alphanumeric, all characters that are not whitespace characters one or more. 
    
    this line (?:\s(\S+) (?:\s(\S+)
    opens an non-capturing group that matches a white space, all non-white space characters
   
    
    (?:\s(".*"|[^"]\S*)? )?
     another non capturing group that matches a white space, all non-white space characters
    then a sub group is opened  and it matches letters starting with " and also every other character using . and *
    with an or  pipe | to either match the first set or the second set with is a character set that matches every 
    character that is not " followed by mathcing every non-white space character all of them are now optional   
    
'''

import re
#
# text = input("please input your text: ")
# pattern = r'\S+\s'
#
# regex = re.compile(pattern)
#
# matches = regex.match(text)
#
# if matches:
#     print('yes matched')
# else:
#     print("Try Again")

import re

from uuid import uuid4
# # Regular expression pattern to match the format
# # pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
# pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
#
# # Sample string to test
# sample_string = '49faff9a-6318-451f-3876-910505c55907'
#
# # Check if the sample string matches the pattern
# if re.match(pattern, sample_string):
#     print("Match found!")
# else:
#     print("No match found.")

# print(uuid4())
import re
# #
# pattern = r'\b(\w{8}[-]\w{4}[-]\w{4}[-]\w{4}[-]\w{12})\b'
# #
# text = '49faff9a-6318-451f-87b6-910505c55907'
#
# # pattern = r'\b(word)'
#
# # text = 'wordwordwordword  word word word bookbook'
#
# regex = re.compile(pattern)
#
# match = regex.search(text)
#
# if match:
#     print(match.groups())
#     print(match)
# else:
#     print('no match')



#
#
# text = "cat dog"
# pattern = r'(cat|dog)'  # Match either "cat" or "dog" and capture them separately
#
# matches = re.match(pattern, text)
# print(matches.groups())




# for match in matches:
#     print(match)  # Output: 'cat', 'dog'



pattern = r"(['\"]?\w+['\"])"

text = "This is a 'test' string with 'words' \"bo\"ok\" like 'these'."

matches = re.findall(pattern, text)
print(matches)
# update BaseModel 7cec092c-83c0-4c56-9415-e60219debabe DOB "oij"


"""
def check_arg(self, obj_name, obj_id, obj_attri, obj_value) -> str:

         # check for object class name
        if obj_name:
            if obj_name not in self.ALL_CLASSES:
                print('** class doesn\'t exist ** ')
                return
        else:
            print('** class name missing **')
            return
        if obj_attri is None:
            print('** attribute name missing **')
            return
        elif obj_value is None:
            print('** value missing **')
            return
        # return  key
"""

"""

    def do_update(self, arg) -> None:
        
            update <class name> <id> <attribute name> "<attribute value>"
        
        obj_dict = self.all_obj
        matches = self.match_pattern(arg)

        obj_name, obj_id, obj_attri, obj_value = matches.groups()
    # 
    # 
    #     key = f"{obj_id}.{obj_name}"
    #     if obj_id:
    #         key = f"{obj_id}.{obj_name}"
    #         if key not in obj_dict.keys():
    #             print('** no instance found **')
    #             return
    #     else:
    #         print('** instance id missing **')
    #         return
    # 
    #     print(matches.groups())
    # 
    #     self.check_arg(arg, obj_dict, obj_name, obj_id, obj_attri, obj_value)
    #     # call method to check for argument
    #     model = obj_dict[key]
    # 
    #     if  obj_attri is None:
    #         return
    #     if  hasattr(model, obj_attri):
    #         # only update str, int and float
    #         if not isinstance(getattr(model, obj_attri), (str, int, float)):
    #             print(f"Sorry can't update attribute of type {type(getattr(model, obj_attri))}")
    #             return
    # 
    #         if obj_attri not in ['name', 'age', 'email', 'DOB']:
    #             print('sorry you can only update your name, age and email only! ')
    #             return
    #         else:
    #             try:
    #                 if obj_attri == 'age':
    #                     if self.strip_quotes(obj_value):
    #                         obj_value = self.strip_quotes(obj_value) # strip method.
    #                         obj_value = int(obj_value)
    #                         # self.calc_updated_at_last(model)         # updated_at time differece method
    #                         setattr(model, obj_attri, obj_value)
    #                         self.Storage.save_obj() # call the save method of the FileStorage to write object back to file.json.
    #                         model.save()            # update the updated_at from the BaseModel save method.
    #                         print(f'({obj_attri}) Updated successfully!')
    #                         return
    #                 else:
    #                     obj_value = self.strip_quotes(obj_value)
    #                     # self.calc_updated_at_last(model)
    #                     setattr(model, obj_attri, obj_value) # strip out ("") from the value.
    #                     self.Storage.save_obj() # call the save method of the file storage to write back object to file_db
    #                     model.save()
    #             except ValueError:
    #                 print(f'Input <{obj_value}> not a valid format for attribute [age],'
    #                       f' must be type int!, eg: (18, 19 40)')
    #                 return
    #     else:
    #         print(f"attribute <{obj_attri}> does not exist")
    #         return
"""
