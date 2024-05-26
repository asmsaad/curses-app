
class StyleText:

    STYLE_ = {
        'reset' : '\033[0m',
        'bold' : '\033[01m',
        'disable' : '\033[02m',
        'underline' : '\033[04m',
        'reverse' : '\033[07m',
        'strikethrough' : '\033[09m',
        'invisible' : '\033[08m',

        'bg': {
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'orange': '\033[43m',
            'blue': '\033[44m',
            'purple': '\033[45m',
            'cyan': '\033[46m',
            'lightgrey': '\033[47m',
        },

        'fg': {
            'black' : '\033[30m',
            'red' : '\033[31m',
            'green' : '\033[32m',
            'orange' : '\033[33m',
            'blue' : '\033[34m',
            'purple' : '\033[35m',
            'cyan' : '\033[36m',
            'lightgrey' : '\033[37m',
            'darkgrey' : '\033[90m',
            'lightred' : '\033[91m',
            'lightgreen' : '\033[92m',
            'yellow' : '\033[93m',
            'lightblue' : '\033[94m',
            'pink' : '\033[95m',
            'lightcyan' : '\033[96m',
        }
    }

    

    def __init__(self, text):
        self.text = text
        self.accessed_texts = []  # Initialize a list to store accessed texts

    
    
    def __getattr__(self, attr):
        if attr.startswith('bg') and attr.replace('bg_','') in self.STYLE_['bg'].keys():
            accessed_text = f"{self.STYLE_['bg'][attr.replace('bg_','')]}"
            self.accessed_texts.append(accessed_text)  # Append accessed text to the list
            return self
        elif attr.startswith('fg') and attr.replace('fg_','') in self.STYLE_['fg'].keys():
            accessed_text = f"{self.STYLE_['fg'][attr.replace('fg_','')]}"
            self.accessed_texts.append(accessed_text)  # Append accessed text to the list
            return self
        elif attr in ['bold','disable','underline','reverse','strikethrough','invisible']:
            accessed_text = f"{self.STYLE_[attr]}"
            self.accessed_texts.append(accessed_text)  # Append accessed text to the list
            return self
        else:
            raise AttributeError(f"'CustomText' object has no attribute '{attr}'")
        

        
    
    def end(self):
        # Print all accessed texts followed by "end"
        print([self.STYLE_['reset']+''.join(self.accessed_texts)+self.text+self.STYLE_['reset']])
        return self.STYLE_['reset']+''.join(self.accessed_texts)+self.text+self.STYLE_['reset']

    def __del__(self):
        # print('++')
        # Call end method when the object is deleted
        self.end()


# StyleText(' ').bg_green
# StyleText("sample text").bg_red.fg_yellow.strikethrough
# StyleText("sample text").bg_cyan.fg_yellow.strikethrough
# StyleText("sample text").bg
# StyleText("sample text").bg_orange