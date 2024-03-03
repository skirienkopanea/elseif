import pyperclip

def elseif_to_if(code,syntax_in,syntax_out):    
    output = ''
    lines = code.split('\n')

    if syntax_in == 'py':
        in_if = 'if'
        in_else = 'else'
        in_elseif = 'elif'
        in_endif = '#endif'
        in_then = ':'

    elif syntax_in == 'sql':
        in_if = 'IF'
        in_else = 'ELSE'
        in_elseif = 'ELSEIF'
        in_endif = 'END IF'
        in_then = 'THEN'              

    yes_cond = []
    not_cond = []    
    elseif_number = [0] * 10 #level of indentation, should never be this deep...
    else_number = [0] * 10 #level of indentation, should never be this deep...
    level = 0
    log = []
    condition = ''
    full_cond = ''
    

    for line in lines:
        line = line.strip()
        action = ''
        if line.startswith(in_if):
            condition = line.split(in_if)[-1].split(in_then)[0].strip() # get single condition
            yes_cond.append(condition)									# append condition
            level += 1													# increase indentation level
            elseif_number[level] = 0									# reset elseif_number for indentantion level
            else_number[level] = 0										# reset else_number for indentantion level
			
        elif line.startswith(in_elseif):
            prev_condition = yes_cond.pop()								# pop previous if/elseif "yes" condition
            not_cond.append(prev_condition)								# append previous if/elseif into "not" list
            condition = line.split(in_elseif)[-1].split(in_then)[0].strip() # get single condition
            yes_cond.append(condition)									# append condition
            elseif_number[level] += 1									# increase elsif count   
            
        elif line.startswith(in_else):
            prev_condition = yes_cond.pop()								# pop previous if/elseif "yes" condition
            not_cond.append(prev_condition)								# append previous if/elseif into "not" list
            condition = ''
            elseif_number[level] += 1									# increase elsif count
            else_number[level] += 1										# increase else count
            
        elif line.startswith(in_endif):
            level -= 1													# decrease level
            condition = ''
            if else_number[level+1] == 0:
                 yes_cond.pop()                                         # pop if there were no previous else in the previous level
            for i in range (elseif_number[level+1]):
                not_cond.pop()                                          # clear list of not conditions within same level

        else:
            action = line

        if len(yes_cond) > 0 and len(not_cond) > 0:
             full_cond = ' and '.join(yes_cond) + ' and not (' +' or '.join(not_cond) + ')'
             
        elif len(yes_cond) > 0 and len(not_cond) == 0:
             full_cond = ' and '.join(yes_cond)
             
        elif len(yes_cond) == 0 and len(not_cond) > 0:
             full_cond = 'not (' +' or '.join(not_cond) + ')'
             
        elif len(yes_cond) == 0 and len(not_cond) == 0:
             full_cond = ''
        
        if full_cond == '':
            full_cond = '1 == 1'

        if len(action) > 0:
            if syntax_out == 'py':
                output += f'\nif {full_cond}: {action}'
            if syntax_out == 'sql':
                output += f'\n{action} WHERE {full_cond.upper()}'

        log.append((full_cond,condition,','.join(yes_cond),','.join(not_cond),level,else_number[level] == 1,elseif_number[level], len(yes_cond), len(not_cond),line))
        
    return output
    
code = """
   out = ""
   if a:
      out += ('.a')
      if aa:
         out += ('.aa')
      else:
         out += ('.-aa')
      #endif
      out += ('.a')
   elif b:
      out += ('.b')
      if bb:
         out += ('.bb')
      elif bbb:
         out += ('.bbb')
      elif bbbb:
         out += ('.bbbb')
      #endif
      out += ('.b')
   elif c:
      out += ('.c')
      if cc:
         out += ('.cc')
      elif ccc:
         out += ('.ccc')         
      else:
         out += ('.-cc-ccc')
      #endif
      out += ('.c')
   else:
      out += ('.-a-b-c')
      if d:
         out += ('.d')    
      #endif  
      out += ('.-a-b-c')
   #endif
   out += ('.0')
   return out
"""

parsed_code = elseif_to_if(code,'py','py')
pyperclip.copy(parsed_code)
print('\\n\nCode:',parsed_code, '\nCopied')