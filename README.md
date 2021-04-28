# CIEDE2000

CIEDE2000 provides utility functions to:
 * calculate the distance between two Lab colors;
 * convert colors from BGR to Lab.

## Function `distance`
Calculates the distance between two Lab colors in terms of ΔE<sub>00</sub>.

Usage example:
```python
from ciede2000 import CIEDE2000

lab1 = (50.0, 2.5, 0.0)
lab2 = (50.0, -1.0, 2.0)
deltaE_00 = CIEDE2000.distance(lab1, lab2)
```

## Function `bgr_to_lab`
Converts a BGR color to a Lab color.

Usage example:
```python
from ciede2000 import CIEDE2000

bgr = (125, 125, 125)
lab_color = CIEDE2000.bgr_to_lab(bgr)
```

## Test data
The folder `data` contains spreadsheets with test data:
 * [lab-distances.xlsx](data/lab-distances.xlsx) contains test data for the function `distance`;
 * [bgr-to-lab.xlsx](data/bgr-to-lab.xlsx) contains test data for the function `bgr_to_lab`;

# Author
Francesco Racciatti

# Acknowledgments
The implementation of Lab colors difference, and the related tests, are based on the paper 
[The CIEDE2000 Color-Difference Formula: Implementation Notes, Supplementary Test Data, and Mathematical Observations](
doc/ciede2000-color-difference.pdf), by G. Sharma, W. Wu, E. N. Dalal.

The tests of the BGR to Lab conversion function were built by using  
[https://www.easyrgb.com/en/convert.php](https://www.easyrgb.com/en/convert.php) (checked on April 27, 2021).

# License
This project is licensed under [MIT license](LICENSE).