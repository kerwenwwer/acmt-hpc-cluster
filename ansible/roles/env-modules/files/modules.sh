shell=$(/usr/bin/basename $(/bin/ps -p $$ -ocomm=))

if [ -f /usr/share/modules/init/$shell ]; then
   . /usr/share/modules/init/$shell
else
   . /usr/share/modules/init/sh
fi

export MODULEPATH=$MODULEPATH:/opt/intel/oneapi/modulefiles:/opt/modulefiles:/opt/intel/modulefiles:/opt/cuda/modulefiles:/opt/nvidia/hpc_sdk/modulefiles
