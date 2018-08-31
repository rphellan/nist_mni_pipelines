#!/bin/bash
set -e -x


output_dir=$1

if [ -z $output_dir ];then
 echo "Usage $0 <output dir> "
 echo "Usefull environment variables:"
 echo "MNI_DATAPATH - location of MNI datasets ( /opt/minc/share )"
 echo "               should include icbm152_model_09c and beast-library-1.1"
 echo "PARALLEL     - number of paralell processes to use"
 exit 1
fi

# setup variables
MNI_DATAPATH=${MNI_DATAPATH:-/opt/minc/share}
PARALLEL=${PARALLEL:-1}

icbm_model_dir=$MNI_DATAPATH/icbm152_model_09c
beast_model_dir=$MNI_DATAPATH/beast-library-1.1

if [ ! -d $icbm_model_dir ];then
    echo "Missing $icbm_model_dir"
    exit 1
fi

if [ ! -d $beast_model_dir ];then
    echo "Missing $beast_model_dir"
    exit 1
fi

data_dir=$(dirname $0)

export OMP_NUM_THREADS=1
export ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS=1

cat - > pipeline_options.json <<END
{
  "model":     "mni_icbm152_t1_tal_nlin_sym_09c",
  "model_dir": "${icbm_model_dir}",
  "t1w_nuc":   {},
  "t2w_nuc":   {},
  "pdw_nuc":   {},
  "beast":     { "beastlib":  "${beast_model_dir}" },
  "tissue_classify": {},
  "lobe_segment": {},
  "nl":        true,
  "lobes":     true,
  "cls"  :     true,
  "qc":        true,

  "t1w_stx":   {
      "type":"elx",
      "resample":false,
      "options":
        { "samples":8000,
          "max_step":3.0,
          "iterations":8000
        }
  },
  "add": {
    "t2w_nuc": {},
    "t2w_stx": {
      "type":"elx",
      "resample":false,
      "options":
        { "samples":    4000,
          "max_step":   0.1,
          "iterations": 3000,
          "optimizer": "AdaptiveStochasticGradientDescent",
          "metric":    "AdvancedNormalizedCorrelation",
          "transform": "EulerTransform"
        }

    }

  },

  "nl_reg": {
      "type":"ants",
      "start": 16,
      "level": 2,
      "options": {
          "conf":{"16":100,"8":100,"4":20,"2":10},
          "blur":{"16":16,"8":8,"4":4,"2":2},
          "shrink":{"16":16,"8":8,"4":4,"2":2},
          "cost_function":"CC",
          "cost_function_par":"1,3,Regular,1.0"
      }
  }
}
END


python3 -m scoop -vvv -n $PARALLEL ../../ipl_preprocess_pipeline.py \
 --output $output_dir \
 --csv $data_dir/subject43.csv \
 --options pipeline_options.json
