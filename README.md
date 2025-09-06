````markdown
# PNG to ICO Converter

A simple Python script that converts all **PNG images** inside a `png/` folder into **ICO files** with multiple icon sizes.  
The script automatically creates required folders on the **Desktop** and saves converted `.ico` files in the `ico/` folder.  
It uses the [Pillow](https://pillow.readthedocs.io/) library.

---

## Features

- Converts all `.png` files in the `png/` folder into `.ico` format  
- Generates multiple icon sizes: **16x16, 32x32, 64x64, 128x128, 256x256**  
- Automatically creates required folders (`png` and `ico`) on the Desktop  
- Clear logging for each conversion (success or failure)  
- Uses **Pillow (PIL fork)** for image processing  

---

## Requirements

- **Python 3.8+**
- **Pillow** (Python Imaging Library fork)

Install Pillow:
```bash
pip install pillow
````

---

## How It Works

1. On the Desktop, the script creates the following structure:

   ```
   Desktop/
   └── png-to-ico-converter/
       ├── png/   ← Place your .png files here
       └── ico/   ← Converted .ico files will be saved here
   ```

2. Place your PNG images inside the `png/` folder.

3. Run the script:

   ```bash
   python converter.py
   ```

4. The converted ICO files will appear in the `ico/` folder.

---

## Example

* Input:

  ```
  Desktop/png-to-ico-converter/png/logo.png
  ```

* Output:

  ```
  Desktop/png-to-ico-converter/ico/logo.ico
  ```

The `.ico` file will include multiple icon sizes: 16x16, 32x32, 64x64, 128x128, and 256x256.

---

## Notes

* If an image cannot be processed, the script prints an error message but continues with other files.
* Only `.png` files are processed.
* You can change the default Desktop path in the code if needed.


## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request.

```
:)
```
