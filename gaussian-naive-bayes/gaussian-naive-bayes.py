import math

def gaussian_naive_bayes(X_train: list, y_train: list, X_test: list) -> list:
    """
    Returns a predicted class label for every test sample.
    """
    # Write code here
    prediction = []
    classes = sorted(set(y_train))
    
    means = []
    vars = []
    prior = []
    for c in classes:
        nc = y_train.count(c)

        prob = nc / len(y_train)

        mean = []
        var = []
        for j in range(len(X_train[0])):
            summ = 0
            sum_diff = 0
            for sample in range(len(X_train)):
                if y_train[sample] == c:
                    summ += X_train[sample][j]
            
            feat_mean = summ / nc
            mean.append(feat_mean)

            for sample in range(len(X_train)):
                if y_train[sample] == c:
                    sum_diff += (X_train[sample][j] - feat_mean) ** 2

            feat_var = sum_diff / nc
            var.append(feat_var)

        prior.append(prob)
        means.append(mean)
        vars.append(var)

    for i in range(len(X_test)):
        scores = []
        for c in range(len(classes)):
            log_posterior = math.log(prior[c])
            for j in range(len(X_train[0])):
                normalization = -0.5 * math.log(2 * math.pi * vars[c][j] + 1e-9)
                distance = -((X_test[i][j] - means[c][j]) ** 2) / (2 * (vars[c][j] + 1e-9))
                log_posterior += normalization + distance

            scores.append(log_posterior)
        best_idx = scores.index(max(scores))
        
        predicted_class = classes[best_idx]
        prediction.append(predicted_class)

    return prediction

    