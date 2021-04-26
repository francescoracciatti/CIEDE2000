# CIEDE2000

CIEDE2000 provides utility functions to:
 * calculate the distance between two Lab colors;
 * convert a BGR color to a Lab color.

## Function `distance`
Calculates the distance between two Lab colors in terms of ΔE<sub>00</sub>. 
```python
from ciede2000 import CIEDE2000
...
deltaE_00 = CIEDE2000.distance(lab_color_1, lab_color2)
```

## Function `bgr_to_lab`
Converts a BGR color to a Lab color.
```python
from ciede2000 import CIEDE2000
...
lab_color = CIEDE2000.bgr_to_lab(bgr_color)
```

## Test data
The folder `data` contains spreadsheets with test data:
 * [lab-distances.xlsx](data/lab-distances.xlsx) contains test data for the function `distance`;
 * [bgr-to-lab.xlsx](data/bgr-to-lab.xlsx) contains test data for the function `bgr_to_lab`;

# Author
Francesco Racciatti

# Acknowledgments
The implementation of Lab colors difference is based on the paper 
[The CIEDE2000 Color-Difference Formula: Implementation Notes, Supplementary Test Data, and Mathematical Observations](
doc/ciede2000-color-difference.pdf), by G. Sharma, W. Wu, E. N. Dalal.

# License
This project is licensed under [MIT license](LICENSE).