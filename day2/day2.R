library(magrittr)
library(stringr)
library(tidyr)
library(dplyr)
library(tibble)

day2_input <- read.delim("day2/day2_input.txt", col.names = "V1", header = FALSE)
df <- day2_input %>% as_tibble()

# The bag contains 12 red cubes, 13 green cubes, and 14 blue cubes
red_cubes <- 12
green_cubes <- 13
blue_cubes <- 14


# PART 1 ------------------------------------------------------------------

df_new <- df %>% 
  tidyr::separate_wider_delim(cols = V1,
                              delim =  stringr::regex(", |; "),
                              names_sep = "_",
                              too_few = "align_start") %>% 
  dplyr::mutate(game_id = stringr::str_extract(V1_1, "\\d+(?=:)"),
                V1_1 = stringr::str_remove(V1_1, ".*:\\s")) %>% 
  dplyr::mutate(across(.cols = starts_with("V1"),
                       .fns = ~if_else(str_detect(.x, "red") & (as.integer(str_extract(.x, "\\d*")) > red_cubes),
                                       TRUE,
                                       if_else(str_detect(.x, "green") & (as.integer(str_extract(.x, "\\d*")) > green_cubes),
                                               TRUE,
                                               if_else(str_detect(.x, "blue") & (as.integer(str_extract(.x, "\\d*")) > blue_cubes),
                                                       TRUE, 
                                                       FALSE))))) %>% 
  dplyr::mutate(impossible_reveals = rowSums(select(., contains("V1")), na.rm = TRUE),
                out = dplyr::if_else(impossible_reveals == 0, as.integer(game_id), 0))

df_new$out %>% sum

# PART 2 ------------------------------------------------------------------



