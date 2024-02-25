#!/usr/bin/python3
ver = '1.1.3'

from terbe import *



#Docs

hlp = '''
    Terbe binary apps manager {ver}
      [] optional <> replace your
    
    help                 | View help
    output_help <file>   | Write help to file
    
    ins <appname(s)>     | Install app(s)
    ins --new            | Install only app not installed
    ins --all            | Install all apps
    customins <file(s)>  | Install custom app(s)
    
    rm <appname(s)>      | Remove app(s)
    
    list [filter]        | List online apps
    insed [filter]       | List installed apps
    '''

def url_list():
    url, url_dir, url_getlist, install_to, file_type, insed = chk()
    
    onls = []
    
    tmp_ls = terbe.readurl(f"{url}{url_dir}{url_getlist}")
    
    for tmp in tmp_ls:
        for tmp1 in [url, url_dir, "http://"]:
            if tmp1 in tmp:
                tmp = tmp.replace(tmp1, "", 1)
        onls.append(tmp)
    
    onls2 = []
    
    for tmp in onls:
        if file_type in tmp:
            onls2.append(tmp.replace(file_type, ""))
    
    return onls2

def chk():
    #Configs
    
    url = "watercup.ddns.net:5999"
    url_dir = "/prmenu/srv/terbe/bin/"
    url_getlist = "?get=list&folders=*"
    install_to = "./bin/"
    file_type = ".py"
    
    required_dir = [install_to]
    
    for tmp in required_dir:
        if False == os.path.isdir(tmp):
            terbe.bash(["mk", "--dir", tmp])
    
    insed = []
    
    for tmp in os.listdir(install_to):
        if file_type in tmp:
            insed.append(tmp.replace(file_type, ""))
    
    return url, url_dir, url_getlist, install_to, file_type, insed
    
    

#Main

def help(cmd=[]):
    terbe.bash(["echo", hlp])

def output_help(cmd=[]):
    if cmd == []:
        terbe.bash(["echo", f"[Output Help] Error: Required app name"])
    else:
        terbe.bsah(["echo", f"Writing help to file {cmd[0]}"])
        terbe.writefile(hlp, cmd[0])
        terbe.bsah(["echo", "--Done--"])

def ins(cmd=[]):
    url, url_dir, url_getlist, install_to, file_type, insed = chk()
    onls = url_list()
    
    if cmd == []:
        terbe.bash(["echo", f"[Internet Installation] Error: Required 1 or more app name(s)"])
    else:
        req, arg, cfg = terbe.args(cmd)
        
        if len(arg) >= 1 and arg[0] == "all":
            inls = onls
        elif len(arg) >= 1 and arg[0] == "new":
            inls = []
            
            for tmp in onls:
                if tmp not in insed:
                    inls.append(tmp)
        else:
            inls = []
            
            for tmp in cmd:
                if tmp in onls:
                    inls.append(tmp)
                else:
                    terbe.bash(["echo", f"[Internet Installation] App not found: {tmp}"])
    
        for tmp in inls:
            terbe.bash(["echo", f"[Internet Installation] Installing {inls.index(tmp) + 1} / {len(inls)}: {tmp}..."])
            terbe.bash(["webget", "-o", os.path.join(install_to, f"{tmp}{file_type}"), f"{url}{url_dir}{tmp}{file_type}"])

def rm(cmd=[]):
    url, url_dir, url_getlist, install_to, file_type, insed = chk()
    
    if cmd == []:
        terbe.bash(["echo", f"[Remove] Error: Required 1 or more app name(s)"])
    
    for tmp in cmd:
        if os.path.isfile(os.path.join(install_to, f"{tmp}{file_type}")):
            terbe.bash(["echo", f"[Remove] Removing {cmd.index(tmp) + 1} / {len(cmd)}: {tmp}..."])
            terbe.bash(["rm", os.path.join(install_to, f"{tmp}{file_type}")])
        else:
            terbe.bash(["echo", f"[Remove] App not found {cmd.index(tmp) + 1} / {len(cmd)}: {tmp}"])

def list(cmd=[]):
    onls = url_list()
    
    for tmp in onls:
        if cmd == [] or cmd[0] in tmp:
            terbe.bash(["echo", tmp])

def insed(cmd=[]):
    url, url_dir, url_getlist, install_to, file_type, insed = chk()
    
    for tmp in insed:
        if cmd == [] or cmd[0] in tmp:
            terbe.bash(["echo", tmp])

def customins(cmd=[]):
    url, url_dir, url_getlist, install_to, file_type, insed = chk()
    
    if cmd == []:
        terbe.bash(["echo", f"[Custom Installation] Error: Required 1 or more file name(s)"])
    
    for tmp in cmd:
        if os.path.isfile(tmp):
            terbe.bash(["echo", f"[Custom Installation] Installing {cmd.index(tmp) + 1} / {len(cmd)}: {tmp}..."])
            if tmp in os.listdir(install_to):
                terbe.bash(["rm", os.path.join(install_to, tmp)])
            terbe.bash(["cp", tmp, install_to])
        else:
            terbe.bash(["echo", f"[Custom Installation] File not found {cmd.index(tmp) + 1} / {len(cmd)}: {tmp}"])