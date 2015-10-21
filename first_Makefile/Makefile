include config.mk

DATA_FILES=$(wildcard ../*.dat)

all : plot output_data

.PHONY : plot
plot : $(PLOT_SR) #output_data was a dependecy here
	$(PLOT_EXE)
#$(PLOT_EXE2)

.PHONY : output_data
output_data : $(SIM_SRC) $(DATA_FILES)
	$(SIM_EXE) 
#$(SIM_EXE2)

#.PHONY : clean
#clean :
#rm -f output_data
#rm -f plot
