# CTD Measurements Analysis

The code in this repository can be used to read, extract and plot data taken with Bruno's CTD. It's an older model, so the newest python packages 
are not going to work with this specific CTD. 
In order to do that, you should do something like that:
1. Download the ruskin app for your computer [ruskin app](https://rbr-global.com/products/software/)
2. Set the different parameters of the CTD
3. Take measurements with the CTD
4. Open the app and download the dataset into your computer
    - You can output the data into different format by right clicking on the filename in the app
    - For this code to work, you need to ouput it in the `.mat` format. (Export -> Legacy -> matlab format)  
5. Run the code in this repo to obtain the raw profiles
6. Do some post-processing to get rid of the unwanted data. 

## Notes about the CTD

- The CTD takes measurements constantly within a time frame at a certain frequency. Be certain of the battery and the storage space available. 