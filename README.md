# CGM-Work
The recent/ useful notebooks I have used for Werk SQuAD

## [StatTest notebook](/stattest_ColDen.ipynb)

This notebook plots the comparative results for statistical significance of H I and O VI Column Density separately. The tests included are: Mann Whiteney U Test, Student T, and KS 2 Sample. The plots are created by testing a variety of limits for the polar and disk regions. Initially we separated the disk and polar regions by polar being where the azimuthal angle is <45 and azimuthal angle in the disk>45. I range the possible polar region from 25-45 degrees and the possible disk region from 45-65 degrees to find the optimized angles to define each region. The notebook then displays the results as a function of the maximum (or edge) degree that defines the polar region, which is why the plots on the x axis will range from 25-45 degrees.

This specific notebook plots the statistical significance of column density for the detections of each ion at 3 different virial radius limits: 0.5,1, and 2. Look for the pink text in this notbook to change the "column" parameter and compare statistical significance of other parameters in the data. I have done so already for: N_comps, sqrtM, v_span, and column density.

## [Crazyplot](/crazyplot.ipynb)

This is the plot I created to display a triple subplot of: $\sqrt{M}$ values for H I and O VI and the corresponding Kaplan Meier Plot.
