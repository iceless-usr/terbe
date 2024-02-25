This is a most detailed help for `boot.py` and `terbe.py`

`terbe.py`

```

      [] optional <> required

    BASICS
    
    terbe                           | Terbe information
    
    help                            | View help
    
    uname                           | Check system information

    
    ls [dir]                        | Get list for target dir
    
    tree [dir]                      | Get tree view for target dir
    
    pwd                             | Get now pwd
    
    cat <file>                      | Print file content
    
    output_docs <docs> <tofile>     | Output docs to a file
    
    echo <message>                  | Print message on shell
    
    webget -o <save as> <url>       | Get file from url, custom filename
    
    webget <url>                    | Get file from url
    
    about <dir(s) / file(s)>       | Get file or dir information
    
    cp <dir / file> <dir / file>    | Copy file or dir
    
    rm <dir(s) / file(s)>           | Remove dir or file
    
    mk <dir(s) / file(s)>           | Make dir or file, dir needed "/" ex "example/"
    
    mk --dir <dir(s)>               | Make dir
    
    mv <dir / file> <dir / file>    | Move file or dir
    
    tar <args> <file(s) / dir(s)>   | Usage like Linux TAR
    
    app <file> <funcation> [args]   | Run funcation in file with args
        OK, this command may complicated.
        Example:
        
        - File system
        
        /
            boot.py
            terbe.py
            dir/
                hello.py

        - Content of /dir/hello.py

        class e:
            def main(cmd):
                print(terbe.decodels(cmd))
        
        - To call e.main() in /dir/hello.py:

        app dir.hello e.main Hello world

        - And get result:
        
        Hello world

        - Notes:

        You see, terbe.encodels(string, t) and terbe.decodels(list, t) can make string to list or list to string, "t" decides how to encode or decode, default is " "

        >>> terbe.encodels("Hello.world", ".")
        ['Hello', 'world']

        >>> terbe.decodels(['Hello', 'world'], "/")
        'Hello/world'
        
    
    systembash <command>            | Enforce system command
        What is command, what will run.
        If you run "edeeede" and it is not a correct command, terbe will run "systembash edeeede".
    
    bash <command>                  | Run a Terbe CORE command
        If you run "bash help", it will run "help".
        
    pyrun <command>                 | Run a python command
        Python exec().
        
```

`boot.py`

```
    IN Terminal
    boot.py            | Shell mode
    boot.py <commmand> | Direct command

    IN Shell
    exit               | Exit shell
    cd <dir>           | Change working dir
    efihelp            | View help of boot loader
    tsh <filename(s)>  | Run TSH
    bod <command>      | Terbe bash with old dir

    environmental variables DOs
    read <name> <tips> | Read user input as name with tips
        Like "set /p" on Windows or "read" on Linux
    set <name> <value> | Set a value
        Like "set" on Windows or "=" on Linux
    writevals <file>   | Write values to file
        Values is save on RAM (Random Access Memory), it will be cleared when closed.
        So, you can use this to save values to a file(.ini).
    readvals <file>    | Read values from file
        You can use this to read values from a file(.ini).

    Notes
    1. "echo $e" Will replace "$e" to value e
    2. View terbe help with command "help"
    3. If
```
