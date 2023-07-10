## Reading CSVs (without libraries)

csv <- read.csv("/path/to/file.csv")

## Writing CSVs

write.csv(csv, "/path/to/file.csv")

## Reading TSVs (without libraries)

tsv <- read.csv("/path/to/file.tsv", sep="\t")

## Writing TSVs

write.csv(tsv, "/path/to/file.tsv", sep="\t")

## Reading Excel Files (needs tidyverse's readxl file)

library(readxl)

excel <- as.data.frame(read_excel("/path/to/file.xlsx"))



