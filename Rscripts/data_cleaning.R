# separating row values into columns based on a separator

library(tidyr)
new_df <- as.data.frame(separate_rows(old_df, COLUMN_NAME, sep = "SEP"))


