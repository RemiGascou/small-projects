# DirConf

A small utility to use custom configuration files in directories.

## Install

You can install the dirconf utility with the automated installer :

```
chmod +x install.sh
./install.sh
```

Or manually by adding this to your `.bashrc` :

```
if [[ -f "/path/to/dirconf/.ba.dirconf" ]]; then
    source /path/to/dirconf/.ba.dirconf
fi
```

## Use

### dirconf_init

Creates a `.dirconf` file in current folder

### dirconf_nearest

Loads the nearest `.dirconf` in current or parents folders

### dirconf_cd

Autoload nearest `.dirconf` when cd (need to overwrite cd : `alias cd="dirconf_cd"`)
