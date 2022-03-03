from .stdinc import Sint32
from .scancode import *

SDL_Keycode = Sint32
SDLK_SCANCODE_MASK = 1 << 30
SDL_SCANCODE_TO_KEYCODE = lambda x: (x | SDLK_SCANCODE_MASK)


SDL_Keymod = c_int

KMOD_NONE = 0x0000
KMOD_LSHIFT = 0x0001
KMOD_RSHIFT = 0x0002
KMOD_LCTRL = 0x0040
KMOD_RCTRL = 0x0080
KMOD_LALT = 0x0100
KMOD_RALT = 0x0200
KMOD_LGUI = 0x0400
KMOD_RGUI = 0x0800
KMOD_NUM = 0x1000
KMOD_CAPS = 0x2000
KMOD_MODE = 0x4000
KMOD_SCROLL = 0x8000
KMOD_RESERVED = KMOD_SCROLL
KMOD_CTRL = KMOD_LCTRL | KMOD_RCTRL
KMOD_SHIFT = KMOD_LSHIFT | KMOD_RSHIFT
KMOD_ALT = KMOD_LALT | KMOD_RALT
KMOD_GUI = KMOD_LGUI | KMOD_RGUI


SDL_KeyCode = c_int

SDLK_UNKNOWN = 0

SDLK_RETURN = ord('\r')
SDLK_ESCAPE = ord('\x1B')
SDLK_BACKSPACE = ord('\b')
SDLK_TAB = ord('\t')
SDLK_SPACE = ord(' ')
SDLK_EXCLAIM = ord('!')
SDLK_QUOTEDBL = ord('"')
SDLK_HASH = ord('#')
SDLK_PERCENT = ord('%')
SDLK_DOLLAR = ord('$')
SDLK_AMPERSAND = ord('&')
SDLK_QUOTE = ord('\'')
SDLK_LEFTPAREN = ord('(')
SDLK_RIGHTPAREN = ord(')')
SDLK_ASTERISK = ord('*')
SDLK_PLUS = ord('+')
SDLK_COMMA = ord(',')
SDLK_MINUS = ord('-')
SDLK_PERIOD = ord('.')
SDLK_SLASH = ord('/')

SDLK_0 = ord('0')
SDLK_1 = ord('1')
SDLK_2 = ord('2')
SDLK_3 = ord('3')
SDLK_4 = ord('4')
SDLK_5 = ord('5')
SDLK_6 = ord('6')
SDLK_7 = ord('7')
SDLK_8 = ord('8')
SDLK_9 = ord('9')

SDLK_COLON = ord(':')
SDLK_SEMICOLON = ord(';')
SDLK_LESS = ord('<')
SDLK_EQUALS = ord('=')
SDLK_GREATER = ord('>')
SDLK_QUESTION = ord('?')
SDLK_AT = ord('@')

SDLK_LEFTBRACKET = ord('[')
SDLK_BACKSLASH = ord('\\')
SDLK_RIGHTBRACKET = ord(']')
SDLK_CARET = ord('^')
SDLK_UNDERSCORE = ord('_')
SDLK_BACKQUOTE = ord('`')

SDLK_a = ord('a')
SDLK_b = ord('b')
SDLK_c = ord('c')
SDLK_d = ord('d')
SDLK_e = ord('e')
SDLK_f = ord('f')
SDLK_g = ord('g')
SDLK_h = ord('h')
SDLK_i = ord('i')
SDLK_j = ord('j')
SDLK_k = ord('k')
SDLK_l = ord('l')
SDLK_m = ord('m')
SDLK_n = ord('n')
SDLK_o = ord('o')
SDLK_p = ord('p')
SDLK_q = ord('q')
SDLK_r = ord('r')
SDLK_s = ord('s')
SDLK_t = ord('t')
SDLK_u = ord('u')
SDLK_v = ord('v')
SDLK_w = ord('w')
SDLK_x = ord('x')
SDLK_y = ord('y')
SDLK_z = ord('z')

SDLK_CAPSLOCK = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CAPSLOCK)

SDLK_F1 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F1)
SDLK_F2 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F2)
SDLK_F3 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F3)
SDLK_F4 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F4)
SDLK_F5 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F5)
SDLK_F6 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F6)
SDLK_F7 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F7)
SDLK_F8 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F8)
SDLK_F9 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F9)
SDLK_F10 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F10)
SDLK_F11 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F11)
SDLK_F12 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F12)

SDLK_PRINTSCREEN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PRINTSCREEN)
SDLK_SCROLLLOCK = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_SCROLLLOCK)
SDLK_PAUSE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PAUSE)
SDLK_INSERT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_INSERT)
SDLK_HOME = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_HOME)
SDLK_PAGEUP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PAGEUP)
SDLK_DELETE = ord('\x7F')
SDLK_END = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_END)
SDLK_PAGEDOWN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PAGEDOWN)
SDLK_RIGHT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RIGHT)
SDLK_LEFT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_LEFT)
SDLK_DOWN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_DOWN)
SDLK_UP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_UP)

SDLK_NUMLOCKCLEAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_NUMLOCKCLEAR)
SDLK_KP_DIVIDE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_DIVIDE)
SDLK_KP_MULTIPLY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MULTIPLY)
SDLK_KP_MINUS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MINUS)
SDLK_KP_PLUS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_PLUS)
SDLK_KP_ENTER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_ENTER)
SDLK_KP_1 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_1)
SDLK_KP_2 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_2)
SDLK_KP_3 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_3)
SDLK_KP_4 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_4)
SDLK_KP_5 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_5)
SDLK_KP_6 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_6)
SDLK_KP_7 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_7)
SDLK_KP_8 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_8)
SDLK_KP_9 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_9)
SDLK_KP_0 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_0)
SDLK_KP_PERIOD = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_PERIOD)

SDLK_APPLICATION = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_APPLICATION)
SDLK_POWER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_POWER)
SDLK_KP_EQUALS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_EQUALS)

SDLK_F13 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F13)
SDLK_F14 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F14)
SDLK_F15 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F15)
SDLK_F16 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F16)
SDLK_F17 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F17)
SDLK_F18 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F18)
SDLK_F19 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F19)
SDLK_F20 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F20)
SDLK_F21 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F21)
SDLK_F22 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F22)
SDLK_F23 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F23)
SDLK_F24 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_F24)

SDLK_EXECUTE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_EXECUTE)
SDLK_HELP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_HELP)
SDLK_MENU = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_MENU)
SDLK_SELECT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_SELECT)
SDLK_STOP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_STOP)
SDLK_AGAIN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AGAIN)
SDLK_UNDO = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_UNDO)
SDLK_CUT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CUT)
SDLK_COPY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_COPY)
SDLK_PASTE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PASTE)
SDLK_FIND = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_FIND)
SDLK_MUTE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_MUTE)
SDLK_VOLUMEUP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_VOLUMEUP)
SDLK_VOLUMEDOWN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_VOLUMEDOWN)
SDLK_KP_COMMA = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_COMMA)

SDLK_KP_EQUALSAS400 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_EQUALSAS400)

SDLK_ALTERASE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_ALTERASE)
SDLK_SYSREQ = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_SYSREQ)
SDLK_CANCEL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CANCEL)
SDLK_CLEAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CLEAR)
SDLK_PRIOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_PRIOR)
SDLK_RETURN2 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RETURN2)
SDLK_SEPARATOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_SEPARATOR)
SDLK_OUT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_OUT)
SDLK_OPER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_OPER)
SDLK_CLEARAGAIN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CLEARAGAIN)
SDLK_CRSEL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CRSEL)
SDLK_EXSEL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_EXSEL)

SDLK_KP_00 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_00)
SDLK_KP_000 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_000)

SDLK_THOUSANDSSEPARATOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_THOUSANDSSEPARATOR)
SDLK_DECIMALSEPARATOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_DECIMALSEPARATOR)
SDLK_CURRENCYUNIT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CURRENCYUNIT)
SDLK_CURRENCYSUBUNIT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CURRENCYSUBUNIT)

SDLK_KP_LEFTPAREN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_LEFTPAREN)
SDLK_KP_RIGHTPAREN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_RIGHTPAREN)
SDLK_KP_LEFTBRACE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_LEFTBRACE)
SDLK_KP_RIGHTBRACE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_RIGHTBRACE)

SDLK_KP_TAB = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_TAB)
SDLK_KP_BACKSPACE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_BACKSPACE)

SDLK_KP_A = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_A)
SDLK_KP_B = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_B)
SDLK_KP_C = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_C)
SDLK_KP_D = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_D)
SDLK_KP_E = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_E)
SDLK_KP_F = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_F)

SDLK_KP_XOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_XOR)
SDLK_KP_POWER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_POWER)
SDLK_KP_PERCENT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_PERCENT)
SDLK_KP_LESS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_LESS)
SDLK_KP_GREATER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_GREATER)
SDLK_KP_AMPERSAND = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_AMPERSAND)
SDLK_KP_DBLAMPERSAND = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_DBLAMPERSAND)
SDLK_KP_VERTICALBAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_VERTICALBAR)
SDLK_KP_DBLVERTICALBAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_DBLVERTICALBAR)
SDLK_KP_COLON = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_COLON)
SDLK_KP_HASH = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_HASH)
SDLK_KP_SPACE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_SPACE)
SDLK_KP_AT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_AT)
SDLK_KP_EXCLAM = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_EXCLAM)
SDLK_KP_MEMSTORE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMSTORE)
SDLK_KP_MEMRECALL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMRECALL)
SDLK_KP_MEMCLEAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMCLEAR)
SDLK_KP_MEMADD = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMADD)
SDLK_KP_MEMSUBTRACT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMSUBTRACT)
SDLK_KP_MEMMULTIPLY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMMULTIPLY)
SDLK_KP_MEMDIVIDE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_MEMDIVIDE)
SDLK_KP_PLUSMINUS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_PLUSMINUS)
SDLK_KP_CLEAR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_CLEAR)
SDLK_KP_CLEARENTRY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_CLEARENTRY)
SDLK_KP_BINARY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_BINARY)
SDLK_KP_OCTAL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_OCTAL)
SDLK_KP_DECIMAL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_DECIMAL)
SDLK_KP_HEXADECIMAL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KP_HEXADECIMAL)

SDLK_LCTRL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_LCTRL)
SDLK_LSHIFT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_LSHIFT)
SDLK_LALT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_LALT)
SDLK_LGUI = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_LGUI)
SDLK_RCTRL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RCTRL)
SDLK_RSHIFT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RSHIFT)
SDLK_RALT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RALT)
SDLK_RGUI = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_RGUI)

SDLK_MODE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_MODE)

SDLK_AUDIONEXT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIONEXT)
SDLK_AUDIOPREV = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOPREV)
SDLK_AUDIOSTOP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOSTOP)
SDLK_AUDIOPLAY = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOPLAY)
SDLK_AUDIOMUTE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOMUTE)
SDLK_MEDIASELECT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_MEDIASELECT)
SDLK_WWW = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_WWW)
SDLK_MAIL = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_MAIL)
SDLK_CALCULATOR = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_CALCULATOR)
SDLK_COMPUTER = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_COMPUTER)
SDLK_AC_SEARCH = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_SEARCH)
SDLK_AC_HOME = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_HOME)
SDLK_AC_BACK = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_BACK)
SDLK_AC_FORWARD = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_FORWARD)
SDLK_AC_STOP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_STOP)
SDLK_AC_REFRESH = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_REFRESH)
SDLK_AC_BOOKMARKS = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AC_BOOKMARKS)

SDLK_BRIGHTNESSDOWN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_BRIGHTNESSDOWN)
SDLK_BRIGHTNESSUP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_BRIGHTNESSUP)
SDLK_DISPLAYSWITCH = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_DISPLAYSWITCH)
SDLK_KBDILLUMTOGGLE = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KBDILLUMTOGGLE)
SDLK_KBDILLUMDOWN = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KBDILLUMDOWN)
SDLK_KBDILLUMUP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_KBDILLUMUP)
SDLK_EJECT = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_EJECT)
SDLK_SLEEP = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_SLEEP)
SDLK_APP1 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_APP1)
SDLK_APP2 = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_APP2)

SDLK_AUDIOREWIND = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOREWIND)
SDLK_AUDIOFASTFORWARD = SDL_SCANCODE_TO_KEYCODE(SDL_SCANCODE_AUDIOFASTFORWARD)