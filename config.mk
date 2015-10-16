SIM_SRC=./LNKMODEL/mprostest.py

#SIM_EXE=bash ./LNKMODEL/launch.sh
SIM_EXE=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python $(SIM_SRC)"

PLOT_SR=./clusterV.py

#PLOT_EXE=bash launch_clusterV.sh
PLOT_EXE=export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/tsl/software/testing/gsl/1.16/x86_64/bin/lib; \
bsub -q TSL-Prod128 -We 1 "source python-2.7.4; python $(PLOT_SR)"
