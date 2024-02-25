# Terbe CORE

Terbe is only a core for your script to import
Ex. You can build a shell frame and import terbe, it will be a terminal

So, there is a shell frame "boot.py" can import terbe and make it a terminal

Now you can build a dir for Terbe

```
terbe/
    boot.py
    terbe.py
```

And run `python boot.py` for shell mode or `python boot.py <cmd>` for direct command

Shell mode like `root@host / # `, ya it is just a terminal.

Now, you can type `efihelp` to get help of `boot.py`, or `help` to get help of `terbe.py`.

`boot.py` DOs

- import terbe > terbe.bash( YOUR INPUT ) > terbe
- `root@host / # `
- Change working dir
- Read, Write, Set values
- Run TSH file (Just like a batch file)
- Exit terminal

`terbe.py` DOs

- import what it needed > recvice boot.py command > do script
