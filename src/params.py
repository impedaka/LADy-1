seed = 0

no_extremes = {
    'no_below': 10,    # happen less than no_below number in total
    'no_above': 0.9,    # happen in no_above percent of reviews
}
doctype = 'snt' # 'rvw' ==> if 'rvw': review = [[review]] else if 'snt': review = [[subreview1], [subreview2], ...]
iter = 100
cores = 0


train_ratio = 0.85 # 1 - train_ratio goes to test
nfolds = 10 # on the train, nfold x-valid

topk = 10
