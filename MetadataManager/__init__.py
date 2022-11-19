import os

class Metadata:
    def __init__( self, path : str ):
        self.metadata_path = path
        self.metadata = None
        self.metadata_buffer = None
        self.size = 0
    
    def open( self ):
        if ( self.metadata == None ):
            self.metadata = open( self.metadata_path, "rb" )
            self.metadata_buffer = self.metadata.read()
            return self.metadata
        else:
            return False
    
    def close( self ):
        if ( self.metadata != None ):
            self.metadata.close( )
            self.metadata = None
            return True
        else:
            return False
    
    def verifyMetadata( self ):
        verifyStreak = 0
        buffer = self.metadata_buffer
        signature = [ 0xAF, 0x1B, 0xB1, 0xFA ]

        for i in range( 0, 4 ):
            if ( signature[ i ] == buffer[ i ] ):
                verifyStreak += 1
        
        if ( verifyStreak == 4 ):
            return True
        else:
            return False
    
    def getSize( self ):
        if ( self.verifyMetadata() ):
            self.metadata.seek( 0, os.SEEK_END )

            self.size = self.metadata.tell( )

            self.metadata.seek( 0, os.SEEK_SET )

            return self.size
        
        raise ( ValueError( "Can't get Size with Invalid Metadata Header" ) )

    def getBuffer( self ):
        if ( self.verifyMetadata() ):
            return bytearray(self.metadata_buffer)
        
        raise ( ValueError( "Can't get Buffer with Invalid Metadata Header" ) )
    
    def getBufferV( self ):
        if ( self.verifyMetadata() ):
            return self.metadata_buffer
        
        raise ( ValueError( "Can't get Main Buffer with Invalid Metadata Header" ) )
    
class XorKeys( ):
    def __init__( self, xorkeys : list ):
        self.xorkeys = xorkeys
    
    def getXorKeys( self ):
        return self.xorkeys

class DecryptedMetadata:
    def __init__( self, metadata : Metadata, xorKeys : XorKeys ):
        self.metadata = None
        self.xorKeys = xorKeys.getXorKeys ()

        if ( metadata.verifyMetadata( ) ):
            self.metadata = metadata

            self.buffer = self.metadata.getBuffer( )
            size = self.metadata.getSize( )
            offset = 4
            while (offset < size):
                self.buffer[ offset ] ^= self.xorKeys[ 4 * ( offset & 0x1FF ) ]
                offset += 1

        else:
            raise( ValueError( "Invalid Metadata Header" ) )
    
    def getBuffer( self ):
        return self.buffer

    def save( self, path : str ):
        with open( path, "wb" ) as f:
            f.write( self.buffer )
    
    def getMetadataVersion( self ):
        return self.buffer[ 4 ]
    
