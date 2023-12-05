library(magrittr)
library(stringr)
library(tidyr)
library(dplyr)
library(tibble)
library(purrr)

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

# 
# prueba <- df %>% 
#   tidyr::separate_wider_delim(cols = V1,
#                               delim =  stringr::regex("; "),
#                               names_sep = "_",
#                               too_few = "align_start") %>% 
#   dplyr::mutate(game_id = stringr::str_extract(V1_1, "\\d+(?=:)"),
#                 V1_1 = stringr::str_remove(V1_1, ".*:\\s")) %>% 
#   dplyr::mutate(across(.cols = starts_with("V1"),
#                        .fns = ~purrr::map_chr(stringr::str_extract_all(.x, "\\d+"),
#                                               ~ stringr::str_c(.x, collapse = ", "))))


data <- df %>% 
  tidyr::separate_wider_delim(cols = V1,
                              delim =  stringr::regex(", |; "),
                              names_sep = "_",
                              too_few = "align_start") %>% 
  dplyr::mutate(game_id = stringr::str_extract(V1_1, "\\d+(?=:)"),
                V1_1 = stringr::str_remove(V1_1, ".*:\\s")) %>% 
  dplyr::select(-game_id)



probando <- function() {
max_red <- 0
max_green <- 0
max_blue <- 0

matrix_out <- matrix(nrow = nrow(data),
                     ncol = 3)

for (i in 1:nrow(data)) {
  for (j in 1:ncol(data)) {
    
    if(is.na(data[[i, j]])) {
      next  
    }
    if (stringr::str_detect(data[[i, j]], "red")) {
      new_value <- as.numeric(stringr::str_extract(data[[i, j]], "\\d+"))
      if(max_red < new_value) {
        max_red = new_value
      }
    }
    if (stringr::str_detect(data[[i, j]], "green")) {
      new_value <- as.numeric(stringr::str_extract(data[[i, j]], "\\d+"))
      if(max_green < new_value) {
        max_green = new_value
      }
    }
    if (stringr::str_detect(data[[i, j]], "blue")) {
      new_value <- as.numeric(stringr::str_extract(data[[i, j]], "\\d+"))
      if(max_blue < new_value) {
        max_blue = new_value
      }
    }
  }
  matrix_out[i, 1] <- max_red
  matrix_out[i, 2] <- max_green
  matrix_out[i, 3] <- max_blue
  max_red <- 0
  max_green <- 0
  max_blue <- 0
  
}
return(matrix_out)
}

part2_mat <- probando()

part2_mat %>% as.tibble() %>% 
  dplyr::mutate(multiply = V1*V2*V3) %>% 
  dplyr::summarise(suma = sum(multiply))