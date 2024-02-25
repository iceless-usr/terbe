from terbe import *

efihelp = '''
    Terbe CORE Boot Loader 1.0.3 LTS
    
    IN Terminal
    boot.py            | Shell mode
    boot.py <commmand> | Direct command
    
    IN Shell
    exit               | Exit shell
    cd <dir>           | Change working dir
    efihelp            | View help of boot loader
    tsh <filename(s)>  | Run TSH
    set <name> <value> | Set a value
    bod <command>      | Terbe bash with old dir
    read <name> <tips> | Read user input as name with tips
    writevals <file>   | Write values to file
    readvals <file>    | Read values from file
    
    Notes
    1. "echo $e" Will replace "$e" to value e
    2. View terbe help with command "help"
    '''

def main(cmd=[]):
    od = os.getcwd()
    vals = {}
    cmds = []
    
    
    if os.path.isfile("boot.tsh"):
        cmds.append("tsh boot.tsh")
    elif cmd == []:
        cmds.append("efihelp")
        cmds.append("terbe")
    
    if cmd != []:
        cmds.append(terbe.decodels(cmd))
        cmds.append("exit")
    
    while True:
        if len(cmds) == 0:
            cmds.append(terbe.read(f"{os.getlogin()}@{platform.node()} {os.getcwd()} # "))
        i = terbe.encodels(cmds[0])
        
        tmp1 = terbe.decodels(i)
        
        for tmp in vals:
            if f"${tmp}" in tmp1:
                tmp1 = tmp1.replace(f"${tmp}", vals[tmp])
        
        i = terbe.encodels(tmp1)
        
        if i[0] == "exit":
            break
        elif i[0] == "read":
            if len(i) >= 3:
                vals[i[1]] = terbe.read(terbe.decodels(i[2:]))
            else:
                terbe.bash(["echo", f"read: Arg error: Required 2 args"])
        elif i[0] == "writevals":
            if len(i) >= 2:
                try:
                    cfg["vals"] = vals
                    cfg.write(open(i[1], "w"))
                except:
                    terbe.bash(["echo", f"writevals: cannot write values to '{i[1]}': Permission denied"])
            else:
                terbe.bash(["echo", f"writevals: Arg error: Required file name"])
        elif i[0] == "readvals":
            if len(i) >= 2:
                if os.path.isfile(i[1]):
                    cfg.read(i[1])
                    vals = cfg["vals"]
                else:
                    terbe.bash(["echo", f"readvals: cannot read values from '{i[1:]}': No such file"])
            else:
                terbe.bash(["echo", f"readvals: Arg error: Required file name"])
        elif i[0] == "set":
            if len(i) >= 3:
                vals[i[1]] = terbe.decodels(i[2:])
            else:
                terbe.bash(["echo", f"set: Arg error: Required 2 Args"])
        elif i[0] == "tsh":
            if len(i) >= 2:
                cont = []
                for tmp in i[1:]:
                    if os.path.isfile(tmp):
                        for tmp1 in terbe.readfile(tmp):
                            cont.append(tmp1)
                    else:
                        terbe.bash(["echo", f"tsh: cannot read file content '{tmp}': No such file"])
                for tmp in cont:
                    cmds.insert(cont.index(tmp) + 1, tmp)
            else:
                terbe.bash(["echo", f"tsh: Arg error: Required file name(s)"])
        elif i[0] == "bod":
            if len(i) >= 2:
                od2 = os.getcwd()
                os.chdir(od)
                terbe.bash(i[1:])
                os.chdir(od2)
            else:
                terbe.bash(["echo", f"bod: Arg error: Required command"])
        elif i[0] == "cd":
            if len(i) >= 2:
                try:
                    os.chdir(terbe.decodels(i[1:]))
                except:
                    terbe.bash(["echo", f"cd: cannot change working dir to '{terbe.decodels(i[1:])}': No such file or directory"])
            else:
                terbe.bash(["echo", f"cd: Arg error: Required dir"])
        elif i[0] == "efihelp":
            terbe.bash(["echo", efihelp])
        else:
            terbe.bash(i)
        
        cmds.pop(0)
        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1:])