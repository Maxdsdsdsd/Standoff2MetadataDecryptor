import MetadataManager, Il2cppManager, os

os.system( "cls||clear" )

xorKeys = []

class Utils:
    def AutoXorKeys( path : str ):
        mask = [ 0xC8, 0xC1, 0xBB, 0xD4, 0xBF, 0xF5, 0x47, 0x46, 0x94, 0x95, 0x2E, 0x5C, 0x0F, 0x20, 0xF7, 0x5D, 0xFF, 0xFF, 0xFF, 0xFF, 0x03 ]
        xorkeys = [ 0 ] * 2048

        streak, offset = 0, 0

        il2cpp = Il2cppManager.Il2Cpp( path )
        il2cpp.open( )

        buffer = il2cpp.getBuffer( )

        il2cpp.close( )

        for letter in buffer:
            if ( letter == mask[ streak ] ):
                streak += 1
            else:
                streak = 0
            if ( streak == len( mask ) ):
                break
            
            offset += 1

        for i in range( 0, 2048 ):
            xorkeys[ i ] = buffer[ offset + 16 + i ]

        return xorkeys

class Modes:
    def Input( ):
        xorkeys_t = input( "Input xorkeys: " )
        for xorkey in xorkeys_t.split( ", " ):
            xorKeys.append( int( xorkey, 0 ) )
        
        metadata_path = input( "Input global-metadata.dat path: " )
        metadata_save_path = input( "Input save path: " )

        os.system( "cls||clear" )

        metadata = MetadataManager.Metadata( metadata_path )
        metadata.open( )
        print( "[LOG] Initialized metadata" )

        print( "[LOG] Initializing xorkeys... (Input)" )
        xorkeys = MetadataManager.XorKeys( xorKeys )
        print( "[LOG] Initialized xorkeys" )

        print( "[LOG] Decrypting metadata..." )
        decryptedMetadata = MetadataManager.DecryptedMetadata( metadata, xorkeys )
        print( "[LOG] Metadata decrypted!" )

        print( "[LOG] Decrypted metadata version - %d" % ( decryptedMetadata.getMetadataVersion( ) ) )
        print( "[LOG] Saved bytes %d from %d" % ( len( decryptedMetadata.getBuffer( ) ), metadata.getSize( ) ) )

        decryptedMetadata.save( metadata_save_path )
        metadata.close( )
    def Auto( ):
        
        metadata_path = input( "Input global-metadata.dat path: " )
        metadata_save_path = input( "Input save path: " )
        il2cpp_path = input( "Input libil2cpp.so path: " )

        os.system( "cls||clear" )

        metadata = MetadataManager.Metadata( metadata_path )
        metadata.open( )
        print( "[LOG] Initialized metadata" )

        print( "[LOG] Initializing xorkeys... (Auto)" )
        xorKeys = Utils.AutoXorKeys( il2cpp_path )
        xorkeys = MetadataManager.XorKeys( xorKeys )
        print( "[LOG] Initialized xorkeys" )

        print( "[LOG] Decrypting metadata..." )
        decryptedMetadata = MetadataManager.DecryptedMetadata( metadata, xorkeys )
        print( "[LOG] Metadata decrypted!" )

        print( "[LOG] Decrypted metadata version - %d" % ( decryptedMetadata.getMetadataVersion( ) ) )
        print( "[LOG] Saved bytes %d from %d" % ( len( decryptedMetadata.getBuffer( ) ), metadata.getSize( ) ) )

        decryptedMetadata.save( metadata_save_path )
        metadata.close( )

def main( ):
    print("""
    Standoff 2 Metadata Decryptor
""")

    print("    Select mode: ")
    print("""
    1 - Input Mode
    2 - Auto Mode
""")

    mode = input( "> " )
    print( )

    if ( int( mode ) == 1 ):
        Modes.Input( )
    elif ( int(mode) == 2 ):
        Modes.Auto( )

    input( )

if __name__ == '__main__':
    main( )
