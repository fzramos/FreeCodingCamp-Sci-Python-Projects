import operator

def arithmetic_arranger(problems, ans=False):
    #error checking
    if len(problems)>5:
        return('Error: Too many problems.')
        
    final_list = list()
    ops = { "+": operator.add, "-": operator.sub}
    for prob in problems:
        comp = prob.split()
        if comp[1] not in "+-":
            return("Error: Operator must be '+' or '-'.")
            
        if (not comp[0].isdigit()) or (not comp[2].isdigit()):
            return('Error: Numbers must only contain digits.')
            
        if (len(comp[0])>4) or (len(comp[2])>4):
            return('Error: Numbers cannot be more than four digits.')
            
        result = str(ops[comp[1]](int(comp[0]), int(comp[2])))
        tot_len = max(len(comp[0]), len(comp[2]))+2
        final_list.append([comp[0], comp[1], comp[2], result, tot_len])

    count = len(final_list)
    output = str()
    for eqn in final_list:
        count -= 1
        spaces = ' ' * (eqn[4] - len(eqn[0]))
        output += spaces + eqn[0]
        if count > 0:
            output += '    '
        else:
            output += '\n'

    count = len(final_list)
    for eqn in final_list:
        count -= 1
        spaces = ' ' * (eqn[4] - len(eqn[2]) - 1)
        output += eqn[1] + spaces + eqn[2]
        if count > 0:
            output += '    '
        else:
            output += '\n'
    
    count = len(final_list)
    for eqn in final_list:
        count -= 1
        output += '-' * eqn[4]
        if count > 0:
            output += '    '

    
    if ans == True:
        count = len(final_list)
        output += '\n'
        for eqn in final_list:
            count -= 1
            spaces = ' ' * (eqn[4] - len(eqn[3]))
            output += spaces + eqn[3]
            if count > 0:
                output += '    '

    
    arranged_problems = output
    
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))