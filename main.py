import curses
from app.textart import *
from app.terminalstyle import StyleText




class OpeaningScreen:
    def __init__(self,stdscr) -> None:
        self.stdscr = stdscr
        self.stdscr.clear()
        


# curses.COLOR_BLACK
# curses.COLOR_BLUE
# curses.COLOR_CYAN
# curses.COLOR_GREEN
# curses.COLOR_MAGENTA
# curses.COLOR_RED
# curses.COLOR_WHITE
# curses.COLOR_YELLOW


class TextColor:
    TEXT_STYLE = {}
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.start_color()

    def style(self,type='MENU-SELECT',inverse:bool=False, row=1, col=1, text='Test'):
        # Initialize curses
        # curses.start_color()
        # Define color codes
        # GREEN_PAIR = 2
        color_pair_name = len(self.TEXT_STYLE.keys())+1
        # Initialize color pair (foreground color green, default background)
        curses.init_pair(len(self.TEXT_STYLE.keys())+1, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Turn on the green color attribute
        self.stdscr.attron(color_pair_name)

        if inverse:
            self.stdscr.addstr(row, col , text ,  curses.color_pair(color_pair_name) | curses.A_REVERSE )
        else: 
            self.stdscr.addstr(row, col , text ,  curses.color_pair(color_pair_name) )
       
        # Turn off the green color attribute
        self.stdscr.attroff(color_pair_name)



class MenuApp:
    def __init__(self, stdscr,TextStyle):
        self.stdscr = stdscr
        self.textstyle_ =TextStyle
        self.stdscr.clear()
        curses.curs_set(1)


        #* Reset the selection button 
        self.reset_button_selector(max_row=3,max_col=1)
    
        
        self.menu = ["Home", "Settings", "Exit"]
        # self.current_row = 0

    def reset_button_selector(self,default_row:int=1, default_col:int=1, max_row:int=None, max_col:int=None) -> None:
        self.current_row , self.current_col = default_row, default_col
        self.min_row , self.max_row = 1 , max_row if max_row else 1
        self.min_col , self.max_col = 1 , max_col if max_col else 1



    def fancy_text(self,name,align='center'):
        if name.lower().strip() == 'intro':
            text_ = INTRO_TEXT
        for index_ , each_line_ in enumerate(text_.split('\n')):
            self.stdscr.addstr(2+index_, (self.w//2 - len(each_line_)//2) , each_line_)
        self.press_to_continue(index_+2)




    def press_to_continue(self,line_number):
        text = f'Press Enter to Continure.Esc to exit. Row:{str(self.current_row)}  Col:{str(self.current_col)}'
        self.textstyle_.style(row=2+line_number    , col=(self.w//2 - len(text)//2), text=text, type='MENU-SELECT', inverse= True if self.current_row==1 else False)
        self.textstyle_.style(row=2+line_number+1  , col=(self.w//2 - len(text)//2), text=text, type='MENU-SELECT', inverse= True if self.current_row==2 else False)
        self.textstyle_.style(row=2+line_number+2  , col=(self.w//2 - len(text)//2), text=text, type='MENU-SELECT', inverse= True if self.current_row==3 else False)
        
        

    def app_developer_info(self):
        developer_email = 'asad@gfoundries.com'
        app_version = 'v0.0.01 - May 2024'

        self.stdscr.addstr(self.h-2-1, self.w-1-len(developer_email)-1, developer_email)
        self.stdscr.addstr(self.h-2-1, 2 , app_version)

    def app_frame(self):
        
        self.stdscr.addstr(0, 0, f"{'▄'*(self.w)}")
        [(self.stdscr.addstr(i, 0, f"{'▌'}") , self.stdscr.addstr(i, self.w-1, f"{'▐'}")) for i in range(1,self.h-2)]           
        # [ for i in range(1,self.h-2)]
        self.stdscr.addstr(self.h-2, 0, f"{'▀'*(self.w)}")
        



    def print_menu(self):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        for idx, row in enumerate(self.menu):
            x = w//2 - len(row)//2
            y = h//2 - len(self.menu)//2 + idx
            if idx == self.current_row:
                self.stdscr.attron(curses.A_REVERSE)
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.A_REVERSE)
            else:
                self.stdscr.addstr(y, x, row)
        # self.stdscr.refresh()

    def run(self):
        while True:
            self.stdscr.clear()
            self.h, self.w = self.stdscr.getmaxyx()

            self.app_frame()
            self.app_developer_info()
            self.fancy_text('intro')
            # self.print_menu()

            self.stdscr.refresh()


            key = self.stdscr.getch()





            if key == curses.KEY_UP and self.current_row  > self.min_row :
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < self.max_row:
                self.current_row += 1
            elif key == curses.KEY_LEFT and  self.current_col > self.min_col:
                self.current_col -= 1
            elif key == curses.KEY_RIGHT and self.current_col < self.max_col:
                self.current_col += 1

    
            elif key == ord('\n'):
                # self.current_row , self.current_col
                # if self.menu[self.current_row] == "Exit":
                #     break
                self.stdscr.clear()
                self.stdscr.addstr(0, 0, f"Selected 'Row:{str(self.current_row)}  Col:{str(self.current_col)}'")
                self.stdscr.refresh()
                self.stdscr.getch()

def main(stdscr):
    TextStyle = TextColor(stdscr)
    
    app = MenuApp(stdscr,TextStyle)
    app.run()

curses.wrapper(main)
# print(str(StyleText("sample text").bg_red.fg_yellow.strikethrough))
