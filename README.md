
# Simple Python Optical Character Recognition using PyTesseract, to extract date stamps from scanned photos

This is a hobby project to try and better organise a large batch of old family photos I scanned a while back. The desired end goal is for all of the scanned photos which have a red date stamp in the corner to have a filename containing that date.

As this is a non-trivial computer vision problem, this may be a total failure, but the idea is to try and narrow down the problem with as many reasonable assumptions as possible.

For example, hopefully:
- we only need to detect 10 characters - digits 0-9
- we only need to support the single 7-segment digit font used in those old image date stamps
- we can assume the date stamp was imprinted in a (hopefully fairly consistent) shade of red

If these prove to be trye, we should then be able to apply various image transforms and filters first to leave only the digit segments, binarize this and put it through tesseract with a carefully trained model just for these digits to do the actual OCR.

## Getting Started

### Prerequisites

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki#installation)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone git@github.com:beveradb/scanned-photos-date-stamp-ocr.git
```

2. Check into the cloned repository
```
$ cd scanned-photos-date-stamp-ocr
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Run the script to process the example images
```
python ocr.py
```

## Contribution

This is a low commitment personal hobby project - feel free to fork and do whatever you like, contributions will be gratefully accepted and merged, but please don't expect much from me!