# upi2csv

## Motivation

Simple Python script to help my father export his POIs collected over many 
years into a CSV file from the proprietary UPI format used by old Sygic
GPS navigation systems.

Unfortunately Sygic never really bothered to document the UPI file format and only
offers a very old [software](https://www.sygic.com/de/company/poi) (runs on Win7 32bit)
to convert a CSV POI file into an UPI file. Fortunately, the UPI POIs [seems to be very
simular to OV2 POIs](https://code.google.com/archive/p/poiman-for-sygic/wikis/UpiFormat.wiki)
used by TomTom.

## How-To

Usage: `upi2csv.py <upi-file-to-convert> <2-letter-country-code>`  

CSV output format: `longitude,latitude,location,comment`

The 2-letter code is used as a prefix for the location field in the CSV 
file to make it easier to sort the file by country. The file `ADAC.upi`
can  be used to verify your setup.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to
discuss what you would like to change.

## License

Copyright (c) 2024 Lars Wessels  
This software was published under the MIT license.  
Please check the [license file](LICENSE).
