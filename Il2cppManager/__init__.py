
class Il2Cpp:
    def __init__(self, path : str ):
        self.il2cpp_path = path
        self.il2cpp = None
        self.il2cpp_buffer = None
    
    def open( self ):
        if ( self.il2cpp == None ):
            self.il2cpp = open( self.il2cpp_path, "rb" )
            self.il2cpp_buffer = self.il2cpp.read()
            return self.il2cpp
        else:
            return False
    
    def close( self ):
        if ( self.il2cpp != None ):
            self.il2cpp.close( )
            self.il2cpp = None
            return True
        else:
            return False
    
    def getBuffer( self ):
        return bytearray(self.il2cpp_buffer)
    
    def getBufferV( self ):
        return self.il2cpp_buffer
