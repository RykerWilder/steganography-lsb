# LSB (Least Significant Bit) Steganography

This project implements a basic steganography technique to hide secret messages inside images using the LSB (Least Significant Bit) method.

---

### What is LSB steganography?

LSB steganography is a technique that hides information in the least significant bits of an image's pixels. Since altering the least significant bit of a color channel causes changes that are imperceptible to the human eye, the message remains hidden in the normal image.

---

### Limitations and warnings

**Capacity**: The amount of data that can be hidden depends on the image size, approximate formula: (width × height × 3) / 8 characters (3 RGB channels per pixel).

**Image formats**: Works best with lossless formats like PNG, lossy formats like JPEG may corrupt the message.

**Security**: This is a basic method, not suitable for advanced security purposes, can be detected by steganalysis tools. For more security, combine with encryption before hiding the message.

---

### Requirements

- Python 3.x
- Libraries:
```bash
pip install pillow numpy
```