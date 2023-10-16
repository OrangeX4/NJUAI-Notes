% set the random number seed to 0 for reproducibility
rand('seed', 0);
% rng(0);
avg = [1 2 3 4 5 6 7 8 9 10];
scales = [1 0.5 0.1 0.05 0.01 0.005 0.001 0.0005 0.0001];
rawdata = randn(5000, 10);
for index = 1:length(scales)
    scale = scales(index);
    % generate 5000 examples, each 10 dim
    data = rawdata + repmat(avg*scale, 5000, 1); % plus i*scale for ith dim
    m = mean(data); % average for each dim
    m1 = m/norm(m); % norm(m) = sqrt(sum(m.^2)), normalized average

    % do PCA, but without centering
    [~, S, V] = svd(data);
    S = diag(S);
    e1 = V(:, 1); % first eigenvector

    % do correct PCA with centering
    newdata = data - repmat(m, 5000, 1);
    [~, S, V] = svd(newdata);
    S = diag(S);
    new_e1 = V(:,1); % first eigenvector

    % correlation between first eigenvector
    avg_mean = avg - mean(avg);
    avg_normalized = avg_mean/norm(avg_mean);

    e1 = e1 - mean(e1);
    e1 = e1/norm(e1);

    new_e1 = new_e1 - mean(new_e1);
    new_e1 = new_e1/norm(new_e1);

    corr1 = avg_normalized * e1;
    corr2 = e1'* new_e1;
    sprintf("scale is %f, correlations are %f and %f", scale, corr1, corr2)
end