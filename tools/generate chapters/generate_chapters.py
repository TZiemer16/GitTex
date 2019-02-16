###############################################################################
#          Copyright (c) 0000 TAZ          #
#                            All rights reserved.                             #
###############################################################################
"""
    test
"""
# Standard Library


class parser():

    def __init__(self):
        """asd"""
        self.number = 1
        self.char_code = "a"
        
    def generate_chapter(self, chapter_name):
        """asd"""

        list_of_words = chapter_name.split(' ')
        string_of_lc_words = ''
        for word in list_of_words:
            word_lc = word.lower()
            word_appended = word_lc + "_"
            string_of_lc_words = string_of_lc_words + word_appended
        string_of_lc_words = string_of_lc_words[:-1]
        chapter_section = ''
        chapter_section = chapter_section + "% "
        chapter_section = chapter_section + str(self.number) + "\n"
        chapter_section = chapter_section + "\\newcommand{\chapter"
        chapter_section = chapter_section + self.char_code
        chapter_section = chapter_section + "}{../../poem/"
        chapter_section = chapter_section + string_of_lc_words
        chapter_section = chapter_section + ".tex}"
        chapter_section = chapter_section + "\n"
        chapter_section = chapter_section + "\\begin{poem}{"
        chapter_section = chapter_section + chapter_name
        chapter_section = chapter_section + "}{}"
        chapter_section = chapter_section + "\n"
        chapter_section = chapter_section + "\input{\chapter"
        chapter_section = chapter_section + self.char_code
        chapter_section = chapter_section + "}"
        chapter_section = chapter_section + "\n"
        chapter_section = chapter_section + "\\end{poem}"
        
        self.number = self.number + 1
        self.char_code = chr(ord(self.char_code) + 1)
        return chapter_section


if __name__ == '__main__':
    parser_singleton = parser()
    with open('chapter_list.txt', 'r') as tex_file, open('gen_chapter_list.tex', 'w') as txt_file:

        new_text = ''
        for tex_line in tex_file:
            print(tex_line)
            tex_line = tex_line[:-1] # remove line end char

            chapter_section_text = parser_singleton.generate_chapter(tex_line)
            new_text = new_text + chapter_section_text + "\n\n"

        txt_file.write(new_text)
        print(new_text)