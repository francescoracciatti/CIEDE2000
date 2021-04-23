# CIEDE2000

Python implementation of CIEDE2000 color difference algorithm, to calculate the distance between two colors.

The implementation and the tests are based on the paper [The CIEDE2000 Color-Difference Formula: 
Implementation Notes, Supplementary Test Data, and Mathematical Observations
](doc/ciede2000-color-difference.pdf), by G. Sharma, W. Wu, E. N. Dalal.

# Usage
```python
from ciede2000 import CIEDE2000

delta = CIEDE2000.distance(lab_color_1, lab_color2)
```

# Author
Francesco Racciatti
