###############################################################################
#          Copyright (c) 0000 TAZ          #
#                            All rights reserved.                             #
###############################################################################
"""
    test
"""
# Standard Library


def convert_tex_to_txt(line, conversions):
    """lol"""
    for replacement in conversions:
        line = line.replace(replacement['old'], replacement['new'])
    #print line
    return line


if __name__ == '__main__':
    with open('latex.tex', 'r') as tex_file, open('latex_to_txt.txt', 'w') as txt_file:
        tex_conversions = [#{'old' : '\\', 'new' : "\n"},
                           {'old' : "quad", 'new' : "\t"}]
                           #{'old' : "\n", 'new' : ""}]
        new_text = ''
        for tex_line in tex_file:
            #print tex_line
            tex_new_lines = tex_line.split('\\')
            print(tex_new_lines)
            new_text_list = []
            for new_tex_line in tex_new_lines:
                new_tex_line += '\n'
                new_text_list.append(convert_tex_to_txt(new_tex_line, tex_conversions))
                
            new_text_list = new_text_list[::2]
            print (new_text_list)
            for item in new_text_list:
                new_text += item
                
                #new_text += '\n'

        txt_file.write(new_text)