'''OpenGL extension ARM.pixmap_multisample_discard

This module customises the behaviour of the 
OpenGL.raw.EGL.ARM.pixmap_multisample_discard to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARM/pixmap_multisample_discard.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.ARM.pixmap_multisample_discard import *
from OpenGL.raw.EGL.ARM.pixmap_multisample_discard import _EXTENSION_NAME

def glInitPixmapMultisampleDiscardARM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION