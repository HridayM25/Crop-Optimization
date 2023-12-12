# Overview

This project deals with the optimization solution for optimal farming. Have used the Crop Dataset for predicting the probabilities for the top 3 crops.

Then, we take
1) The farmers budget
2) The farmers area of land
3) Crop Time to grow
4) Buying Price
5) Selling Price
6) Produce per unit area

Here we find the selling price based on forecasting using Meta's Prophet. The buying price is taken as the last entry and the selling price will be taken as (last date + time to grow). We assume the farmer sells the crop as soon as it has grown.

Here, we want to maximize the objective function:

$$\[
\text{Maximize} \quad \sum_{i} a_i \cdot sp_i \cdot gpa_i \cdot \left(\frac{t_{\text{max}}}{t_i}\right)
\]

Subject to the constraints:

\[
\sum_{i} a_i = A
\]

\[
\sum_{i} a_i \cdot bp_i \cdot gpa_i \cdot \left(\frac{t_{\text{max}}}{t_i}\right) \leq B
\]$$

where:
- \(a_i\) is the area for each crop \(i\).
- \(sp_i\) is the selling price for each crop \(i\).
- \(gpa_i\) is the growth per area for each crop \(i\).
- \(t_i\) is the time taken for each crop \(i\).
- \(t_{\text{max}}\) is the maximum time taken.
- \(A\) is the total land area.
- \(B\) is the budget.

## Personal Notes

Things yet to do:

**Look into how the rainfall can be found based on the pressure and moisture given by our IoT device. If not, time series is always there. Can add these as features to them.** ---> Have to focus on this.

**- Get data for the prices of the crops and store them in the correct formatting.** Will have to verify this. (Not too much of a task)

~~1) Fetch the time series for all the crops listed. Run LGBM Prediction for forecasting or Prophet.~~

~~2) Buying Price is the price for the last entry~~

~~3) Selling Price is the price according to the average time growth, so average_time_growth + last entry.~~

~~4) After collecting this data, make changes to allocateArea.py~~

5) After we have n farmers' data, we can cluster them. The optimal clusters finding process will be automated, and hence we can cluster the farmers together. Dummy data of the marketplace from the blockchain side or something like that. (Not too much of a task)
