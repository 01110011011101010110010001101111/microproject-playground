## Separating row values into columns based on a separator

library(tidyr)
new_df <- as.data.frame(separate_rows(old_df, COLUMN_NAME, sep = "SEP"))

## Merging two dfs based on a column

new_df <- merge(df1, df2, by.x=DF1_COLNAME, by.y=DF2_COLNAME)

