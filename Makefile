YELLOW = \033[33m
GREEN = \033[32m
RED = \033[31m
RESET = \033[0m

all: tests

tests: test2 test1 test0 comments

comments: 
	@echo -n "${YELLOW}comments: " && grep -E "//|/\*" main.c | wc -l && echo "${RESET}"
	
test2: main
	@echo -n "Testing setting the alarm: "
	@echo "1 23 59 58 2 23 59 59 3 4" | timeout 5 ./main > Results/result_2.txt || echo -n "${YELLOW}program returned error ${RESET}"
	@grep -iEq "alarm|goodbye|quit" Results/result_2.txt && echo "${GREEN}pass${RESET}" || echo "${RED}fail${RESET}"

test1: main
	@echo -n "Testing setting the time: "
	@echo "1 23 59 59 3 4" | timeout 5 ./main > Results/result_1.txt || echo -n "${YELLOW}program returned error ${RESET}"
	@grep -iEq "goodbye|quit" Results/result_1.txt && echo "${GREEN}pass${RESET}" || echo "${RED}fail${RESET}"

test0: main
	@echo -n "Testing Error checking: "
	@echo "0 4" | timeout 5 ./main > Results/result_0.txt || echo -n "${YELLOW}program returned error ${RESET}"
	@grep -iEq "invalid|goodbye|quit" Results/result_0.txt && echo "${GREEN}pass${RESET}" || echo "${RED}fail${RESET}"

main: main.c
	@cc main.c -o main 2>> compile_log.txt
	@echo "Code compiled with " && grep -iEq "warning" compile_log.txt | wc -l | tr -d '\n' && echo " warnings and " && grep -iEq "error" compile_log.txt | wc -l | tr -d '\n' && echo " errors"
