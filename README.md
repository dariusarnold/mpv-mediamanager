# mpv media manager

View media (images and videos) in mpv, deleting the ones you dont want to keep with just a keypress.

## Requirements

### Python packages

See the `requirements.txt` file. You can install them all at once with `pip install -r requirements.txt`

### Other applications

You need to have mpv and libmpv installed. On debian 9 the libmpv package is called `libmpv1`.

## Usage

Media files should be in a folder called files in the directory where `media-manager.py` is. 

### Keys

While reviewing the files, press 

| Key | Function |
|-----|----------|
|`r`| Mark a file for deletion. Will be deleted after all files are reviewed or if `Enter` is pressed. |
|`k`| Keep this file, go to next file |
|`f`| Toggle fullscreen |
| `Enter` | Delete all files marked for deletion so far ||
