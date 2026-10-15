# Project 4: Image / Text Recognition (OCR Pipeline)

**DecodeLabs Artificial Intelligence Internship | Batch 2026 | Optional Mastery Phase**

Author: Sree Harsha (Bolla Sree Harsha) | [GitHub](https://github.com/SreeHarsha733)

---

## 1. Overview

This project implements a basic **Optical Character Recognition (OCR)** pipeline in Python. It takes a raw image containing printed text, cleans it with classic computer-vision pre-processing, extracts the text using a pre-trained OCR engine, and displays the result with a confidence score for every recognized word.

No model training is involved. The focus is on **model implementation**: integrating pre-trained libraries into a working workflow and interpreting their outputs.

**Chosen path:** Path 1 (OCR) using `pytesseract`.

## 2. Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Google Colab | Execution environment |
| Tesseract OCR 5.x | OCR engine (pre-trained LSTM model) |
| pytesseract | Python wrapper for Tesseract |
| OpenCV (cv2) | Image loading and pre-processing |
| NumPy | Array operations |
| Matplotlib | Displaying results |

## 3. How the Pipeline Works

The pipeline follows the **IPO model** (Input, Process, Output).

```
Upload image
     |
     v
Pre-processing:  Grayscale -> Gaussian Blur -> Adaptive Threshold (+ Otsu for comparison, optional Deskew)
     |
     v
OCR (pytesseract image_to_data), tried with psm 3, 6 and 11 on gray / adaptive / otsu versions
     |
     v
Pick the best combination (highest mean confidence)
     |
     v
Confidence filter: keep only words with confidence >= 80%
     |
     v
Output: extracted text + boxed words with confidence labels + gatekeeper checklist
```

### Step details

1. **Input.** The image is loaded with OpenCV as a 3D array (Height x Width x 3 color channels). Small images are upscaled so Tesseract gets reasonably sized text.
2. **Grayscale conversion.** Collapses the three color channels into one intensity channel and removes distracting color data.
3. **Gaussian blur.** Smooths the image to remove small imperfections and noise.
4. **Adaptive thresholding.** Converts the image to pure black and white using a locally calculated cutoff, which copes with uneven lighting and shadows. Otsu's global threshold is also computed for comparison.
5. **Deskewing (optional).** Tests small rotation angles and straightens tilted text.
6. **OCR.** `pytesseract.image_to_data` returns every word with its position and a confidence score. Three Page Segmentation Modes are tested:
   - `--psm 3`: fully automatic layout
   - `--psm 6`: single uniform block of text
   - `--psm 11`: sparse, scattered text
7. **Confidence filter.** Words below the **80% threshold** are dropped to avoid false positives.
8. **Visual output.** Boxes and confidence labels are drawn on the image, and a six-panel overview is saved.

## 4. Milestone Validation (Gatekeeper Rule)

| # | Requirement | How this project meets it |
|---|---|---|
| 1 | Library integration | `pytesseract` runs error-free on the processed image |
| 2 | Pre-processing integrity | Grayscale conversion and adaptive thresholding are executed and shown |
| 3 | Accuracy benchmarking | Mean confidence is calculated and checked against the 80% minimum |
| 4 | Visual confirmation | Extracted text is printed and recognized words are boxed with labels |

The script prints a `[PASS]` / `[FAIL]` checklist for all four checks at the end of each run.

## 5. How to Run

1. Open [Google Colab](https://colab.research.google.com) and create a new notebook.
2. Install the dependencies in the first cell:

   ```python
   !apt-get update -qq
   !apt-get install -y -qq tesseract-ocr
   !pip install -q pytesseract opencv-python-headless
   ```

3. Paste the pipeline script into a second cell and run it.
4. Click **Choose Files** when prompted and upload a `.png` or `.jpg` image containing printed text.
5. Review the printed text, the overview figure and the gatekeeper checklist.

> Colab sessions reset when they end, so the install cell must be re-run each time the notebook is reopened.

## 6. Output Files

| File | Description |
|---|---|
| `pipeline_overview.png` | Six panels: original, grayscale, blur, adaptive threshold, Otsu threshold, OCR result |
| `ocr_result.png` | Original image with boxes and confidence labels on words at or above 80% |
| `ocr_text.txt` | The extracted text |

## 7. Results

Fill these in after running the script on your image.

| Item | Value |
|---|---|
| Sample image | `<file name>` |
| Best setting | `<image version>, psm <number>` |
| Words detected | `<number>` |
| Words kept (>= 80%) | `<number>` |
| Mean confidence | `<number>%` |
| Gatekeeper checks passed | `<4 / 4>` |

**Screenshots:**

- Pipeline overview: `pipeline_overview.png`
- OCR result: `ocr_result.png`
- Gatekeeper checklist output

## 8. Key Learnings

- To a machine, an image is a numeric array; changing pixel values changes what it "sees".
- Pre-processing (grayscale, blur, thresholding) has a large effect on OCR accuracy.
- Layout configuration (`--psm`) matters: the right mode depends on the type of document.
- OCR does not "know" the text; it estimates probabilities, so every word comes with a confidence score.
- A confidence filter reduces false positives but may drop correct words, so the threshold is a trade-off.

## 9. Limitations and Future Work

- Accuracy drops on blurry, low-resolution, handwritten or heavily stylized text.
- Deskewing handles only small tilts (about 10 degrees).
- Possible extension: **Path 2, object detection** with `cv2.dnn` and MobileNet-SSD, drawing labeled bounding boxes with an 80% confidence filter.

## 10. Acknowledgements

Project brief and learning material provided by **DecodeLabs** (Project 4: Industrial Training Kit, Batch 2026).
