import pyperclip

def parse_code(code):    
    lines = code.split('\n')
    yes_cond = []
    not_cond = []    
    elseif_number = [0] * 10 #level of indentation, should never be this deep...
    else_number = [0] * 10 #level of indentation, should never be this deep...
    level = 0
    log = []
    condition = ''
    full_cond = ''
    output = ''
    

    for line in lines:
        line = line.strip()
        action = ''
        if line.startswith('IF'):
            condition = line.split('IF ')[-1].split(' THEN')[0].strip() # get single condition
            yes_cond.append(condition)									# append condition
            level += 1													# increase indentation level
            elseif_number[level] = 0									# reset elseif_number for indentantion level
            else_number[level] = 0										# reset else_number for indentantion level
			
        elif line.startswith('ELSEIF'):
            prev_condition = yes_cond.pop()								# pop previous if/elseif "yes" condition
            not_cond.append(prev_condition)								# append previous if/elseif into "not" list
            condition = line.split('IF ')[-1].split(' THEN')[0].strip() # get single condition
            yes_cond.append(condition)									# append condition
            elseif_number[level] += 1									# increase elsif count   
            
        elif line.startswith('ELSE'):
            prev_condition = yes_cond.pop()								# pop previous if/elseif "yes" condition
            not_cond.append(prev_condition)								# append previous if/elseif into "not" list
            condition = ''
            elseif_number[level] += 1									# increase elsif count
            else_number[level] += 1										# increase else count
            
        elif line.startswith('END IF'):
            level -= 1													# decrease level
            condition = ''
            if else_number[level+1] == 0:
                 yes_cond.pop()                                         # pop if there were no previous else in the previous level
            for i in range (elseif_number[level+1]):
                not_cond.pop()                                          # clear list of not conditions within same level

        else:
            action = line
        print(action)

        if len(yes_cond) > 0 and len(not_cond) > 0:
             full_cond = ' AND '.join(yes_cond) + ' AND NOT (' +' OR '.join(not_cond) + ')'
             
        elif len(yes_cond) > 0 and len(not_cond) == 0:
             full_cond = ' AND '.join(yes_cond)
             
        elif len(yes_cond) == 0 and len(not_cond) > 0:
             full_cond = 'NOT (' +' OR '.join(not_cond) + ')'
             
        elif len(yes_cond) == 0 and len(not_cond) == 0:
             full_cond = ''
        
        if full_cond == '':
            full_cond = '1 = 1'

        if len(action) > 0:
            output += f'\n{action} WHERE {full_cond}'

        log.append((full_cond,condition,','.join(yes_cond),','.join(not_cond),level,else_number[level] == 1,elseif_number[level], len(yes_cond), len(not_cond),line))
    
    return output
    
code = """
do something 0
IF a THEN
   do something 1
   IF aa THEN
      do something 2
   ELSE
      do something 3
   END IF
      do something 4
ELSEIF b THEN
   do something 5
   IF 1 THEN
      do something 6
   ELSEIF 2
      do something 7
   ELSEIF 3
      do something 8
   END IF
      do something 9
ELSEIF c THEN
   do something 10
   IF cc THEN
      do something 11
   ELSE
      do something 12
   END IF
   do something 13
ELSE
   do something 14
END IF;
do something 15
"""

parsed_code = parse_code(code)
pyperclip.copy(parsed_code)
print('\nCode:',parsed_code, '\nCopied')
