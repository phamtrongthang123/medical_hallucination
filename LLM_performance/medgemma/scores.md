# Full 
========== Main Results ==========
        Micro-F1-14  Micro-F1-5  Macro-F1-14  Macro-F1-5  Samples-F1-14  Samples-F1-5  Micro-F1-14+  Micro-F1-5+  Macro-F1-14+  Macro-F1-5+  F1-RadGraph     BLEU-1    BLEU-4   ROUGE-L
median     0.276836    0.215190     0.161318    0.146856       0.228349      0.096333      0.292277     0.276740      0.227426     0.263461     0.159851  13.903743  1.354969  0.106339
ci_l       0.211070    0.119314     0.107709    0.083227       0.158927      0.050000      0.221270     0.174523      0.160600     0.157134     0.145264  12.475816  0.906506  0.099628
ci_h       0.338019    0.304505     0.217709    0.206868       0.297429      0.144033      0.361571     0.380159      0.298346     0.366213     0.174509  15.284524  1.745016  0.112758


========== CheXbert F1 (uncertain as positive) ==========
                            f1-score  precision    recall  support
Atelectasis                 0.285714   0.500000  0.200000     40.0
Cardiomegaly                0.238095   0.277778  0.208333     24.0
Consolidation               0.222222   0.250000  0.200000     20.0
Edema                       0.258065   0.250000  0.266667     15.0
Enlarged Cardiomediastinum  0.000000   0.000000  0.000000      1.0
Fracture                    0.000000   0.000000  0.000000      2.0
Lung Lesion                 0.400000   0.250000  1.000000      1.0
Lung Opacity                0.406250   0.433333  0.382353     34.0
No Finding                  0.355556   0.470588  0.285714     28.0
Pleural Effusion            0.338462   0.458333  0.268293     41.0
Pleural Other               0.222222   0.200000  0.250000      4.0
Pneumonia                   0.166667   0.100000  0.500000      4.0
Pneumothorax                0.000000   0.000000  0.000000      0.0
Support Devices             0.375000   0.562500  0.281250     32.0
micro avg                   0.288210   0.311321  0.268293    246.0
macro avg                   0.233447   0.268038  0.274472    246.0
samples avg                 0.240542   0.262381  0.268250    246.0

========== CheXbert F1 (uncertain as negative) ==========
                            f1-score  precision    recall  support
Atelectasis                 0.114286   0.200000  0.080000     25.0
Cardiomegaly                0.235294   0.285714  0.200000     20.0
Consolidation               0.000000   0.000000  0.000000      8.0
Edema                       0.000000   0.000000  0.000000      5.0
Enlarged Cardiomediastinum  0.000000   0.000000  0.000000      1.0
Fracture                    0.000000   0.000000  0.000000      2.0
Lung Lesion                 0.000000   0.000000  0.000000      0.0
Lung Opacity                0.406250   0.433333  0.382353     34.0
No Finding                  0.355556   0.470588  0.285714     28.0
Pleural Effusion            0.392157   0.454545  0.344828     29.0
Pleural Other               0.500000   0.333333  1.000000      1.0
Pneumonia                   0.000000   0.000000  0.000000      2.0
Pneumothorax                0.000000   0.000000  0.000000      0.0
Support Devices             0.375000   0.562500  0.281250     32.0
micro avg                   0.274052   0.301282  0.251337    187.0
macro avg                   0.169896   0.195715  0.183867    187.0
samples avg                 0.225730   0.254500  0.246357    187.0

# Shorten 
========== Main Results ==========
        Micro-F1-14  Micro-F1-5  Macro-F1-14  Macro-F1-5  Samples-F1-14  Samples-F1-5  Micro-F1-14+  Micro-F1-5+  Macro-F1-14+  Macro-F1-5+  F1-RadGraph     BLEU-1    BLEU-4   ROUGE-L
median     0.395137    0.264307     0.165087    0.167980       0.386908      0.091000      0.390999     0.313155      0.224305     0.279754     0.193546  22.104176  2.677546  0.136187
ci_l       0.321141    0.144767     0.127008    0.094174       0.302368      0.042983      0.315979     0.195335      0.160766     0.178779     0.172445  19.817331  1.898402  0.125888
ci_h       0.473257    0.377237     0.200921    0.240594       0.476522      0.142875      0.466058     0.422948      0.282509     0.377776     0.215332  24.266330  3.417568  0.148067

========== CheXbert F1 (uncertain as positive) ==========
                            f1-score  precision    recall  support
Atelectasis                 0.235294   0.545455  0.150000     40.0
Cardiomegaly                0.410256   0.533333  0.333333     24.0
Consolidation               0.160000   0.400000  0.100000     20.0
Edema                       0.181818   0.285714  0.133333     15.0
Enlarged Cardiomediastinum  0.000000   0.000000  0.000000      1.0
Fracture                    0.000000   0.000000  0.000000      2.0
Lung Lesion                 0.000000   0.000000  0.000000      1.0
Lung Opacity                0.315789   0.391304  0.264706     34.0
No Finding                  0.564706   0.421053  0.857143     28.0
Pleural Effusion            0.448276   0.764706  0.317073     41.0
Pleural Other               0.000000   0.000000  0.000000      4.0
Pneumonia                   0.285714   0.333333  0.250000      4.0
Pneumothorax                0.000000   0.000000  0.000000      0.0
Support Devices             0.603774   0.761905  0.500000     32.0
micro avg                   0.392252   0.485030  0.329268    246.0
macro avg                   0.228973   0.316915  0.207542    246.0
samples avg                 0.386524   0.425667  0.383083    246.0

========== CheXbert F1 (uncertain as negative) ==========
                            f1-score  precision    recall  support
Atelectasis                 0.074074   0.500000  0.040000     25.0
Cardiomegaly                0.363636   0.461538  0.300000     20.0
Consolidation               0.000000   0.000000  0.000000      8.0
Edema                       0.000000   0.000000  0.000000      5.0
Enlarged Cardiomediastinum  0.000000   0.000000  0.000000      1.0
Fracture                    0.000000   0.000000  0.000000      2.0
Lung Lesion                 0.000000   0.000000  0.000000      0.0
Lung Opacity                0.315789   0.391304  0.264706     34.0
No Finding                  0.564706   0.421053  0.857143     28.0
Pleural Effusion            0.418605   0.642857  0.310345     29.0
Pleural Other               0.000000   0.000000  0.000000      1.0
Pneumonia                   0.000000   0.000000  0.000000      2.0
Pneumothorax                0.000000   0.000000  0.000000      0.0
Support Devices             0.603774   0.761905  0.500000     32.0
micro avg                   0.396341   0.460993  0.347594    187.0
macro avg                   0.167185   0.227047  0.162300    187.0
samples avg                 0.386637   0.415833  0.392619    187.0